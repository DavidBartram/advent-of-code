from collections import defaultdict
from math import inf, ceil
from queue import PriorityQueue
from itertools import count

#distance (h,r) = distance from hallway position h to front of room r or vice-versa
distance ={
    (0,0):3,(0,1):5,(0,2):7,(0,3):9,
    (1,0):2,(1,1):4,(1,2):6,(1,3):8,
    (2,0):2,(2,1):2,(2,2):4,(2,3):6,
    (3,0):4,(3,1):2,(3,2):2,(3,3):4,
    (4,0):6,(4,1):4,(4,2):2,(4,3):2,
    (5,0):8,(5,1):6,(5,2):4,(5,3):2,
    (6,0):9,(6,1):7,(6,2):5,(6,3):3
    }

def move_cost(r,h,amphi,r_pos):
    #calculate the energy cost to move an amphipod
    #from hallway position h to room position r_pos inside room r
    #or vice-versa
    cost = distance[h,r] + r_pos

    cost = cost*(10**amphi)

    return cost

def hall_to_room(amphi,h,hall,rooms):
    #given an amphipod of type amphi in hallway position h
    #with the current hall and room occupations given by hall and rooms
    #return None if the amphipod cannot be moved to its destination room
    #return (newhall, newrooms, cost) representing the new hall and room occupations
    #and the cost of moving that amphipod to its destination room


    room_index = {0:1.5, 1:2.5, 2:3.5, 3:4.5}
    j = room_index[amphi]
    k = int(ceil(j))

    newhall = list(hall)
    newrooms = [list(room) for room in rooms]

    #check if there are any amphipods between this amphipod and its destination room
    if h<j:
        intervening_hall = [obj!=None for obj in hall[h+1:k]]

    if h>j:
        intervening_hall = [obj!=None for obj in hall[k:h]]
    
    #check if there are any amphipods of the wrong type in the destination room
    wrong_amphi = [(x!=amphi and x!=None) for x in rooms[amphi]]

    if any(intervening_hall) or any(wrong_amphi):
        #if the hallway is blocked or there are any wrong-type amphipods in the room
        return None

    if not (any(intervening_hall) or any(wrong_amphi)):
        #calculate the position inside the destination room that the amphipod will move to
        r_pos = len(rooms[amphi]) - 1 - sum([x==amphi for x in rooms[amphi]])
        #calculate the energy cost of the move
        cost = move_cost(amphi,h,amphi,r_pos)
        #update the state of the hallway and rooms to account for the move
        newhall[h] = None
        newrooms[amphi][r_pos] = amphi
        newhall = tuple(newhall)
        newrooms = tuple([tuple(newroom) for newroom in newrooms])
        return (newhall, newrooms, cost)

def room_to_hall(r,h,amphi,hall,rooms, r_pos):
    #given an amphipod of type amphi in room r
    #with the current hall and room occupations given by hall and rooms
    #return None if the amphipod cannot be moved to hallway position h
    #return (newhall, newrooms, cost) representing the new hall and room occupations
    #and the cost of moving that amphipod to hallway position h

    room_index = {0:1.5, 1:2.5, 2:3.5, 3:4.5}
    j = room_index[r]
    k = int(ceil(j))

    newhall = list(hall)
    newrooms = [list(room) for room in rooms]

    #check if there are any amphipods in the hallway between this amphipod and hallway position h
    if h<j:
        intervening_hall = [obj!=None for obj in hall[h:k]]

    if h>j:
        intervening_hall = [obj!=None for obj in hall[k:h+1]]
    
    #check if there are any amphipods in the room between this amphipod and the hallway
    if r_pos == 0:
        intervening_room = [None]
    
    if r_pos != 0:
        intervening_room = [obj!=None for obj in rooms[r][0:r_pos]]

    if any(intervening_hall) or any(intervening_room):
        #if there is an amphipod blocking this path
        return None
    
    if not (any(intervening_hall) or any(intervening_room)):
        #calculate the cost of moving to hallway position h
        cost = move_cost(r,h,amphi,r_pos)
        #update the state of the hallway and rooms to account for the move
        newhall[h] = amphi
        newrooms[r][r_pos] = None
        newhall = tuple(newhall)
        newrooms = tuple([tuple(newroom) for newroom in newrooms])
        return (newhall, newrooms, cost)

def neighbours(hall,rooms):
    #find the legal board states one move away from the current board
    #helper function for Dijkstra
    neighbours = []

    for h,amphi in enumerate(hall):
        if amphi!=None:
            result = hall_to_room(amphi,h,hall,rooms)
            if result:
                neighbours.append(result)
    
    for h,_ in enumerate(hall):
        for r,room in enumerate(rooms):
            for r_pos, amphi in enumerate(room):
                if amphi!=None:
                    result = room_to_hall(r,h,amphi,hall,rooms, r_pos)
                    if result:
                        #print(result)
                        neighbours.append(result)
    
    return neighbours

def dijkstra(visit,costs):
    #dijkstra's algorithm
    
    while not visit.empty():
        (c,_,(hall,rooms)) = visit.get() #get the next board state in the queue

        if hall == final_hall and rooms == final_rooms:
            #if the final state has been reached, return the cost
            return c
        
        #identify neighbouring board states
        nbs = neighbours(hall,rooms)

        #dijkstra procedure
        for nb in nbs:
            #update the cost with the cost of the move to that neighbour state
            newc = c + nb[2]
            if newc < costs[(nb[0],nb[1])]:
                #update label if new cost is lower than current cost
                costs[(nb[0],nb[1])] = newc
                #add the new board state to the queue
                visit.put((newc, next(unique),(nb[0],nb[1])))


#starting board state - hard-coded from my puzzle input
start_hall = (None,None,None,None,None,None,None)
start_rooms = ((3,3,3,3),(2,2,1,2),(0,1,0,1),(1,0,2,0))

#destination board state
final_hall = (None,None,None,None,None,None,None)
final_rooms = ((0,0,0,0),(1,1,1,1),(2,2,2,2),(3,3,3,3))

#initialise variables for dijkstra
start_costs = defaultdict(lambda : inf) #cost to reach all board states is initialised at infinity
start_costs[(start_hall,start_rooms)] = 0 #cost to reach initial board state is zero
unique=count() #a unique index for each board state, purely to break ties in the priority queue

visit = PriorityQueue() #priority queue of board states to visit
visit.put((0,next(unique),(start_hall,start_rooms))) #initially, queue contains only the starting board state


print(dijkstra(visit,start_costs)) #print puzzle answer





























