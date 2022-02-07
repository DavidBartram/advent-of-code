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
    cost = distance[h,r] + r_pos

    cost = cost*(10**amphi)

    return cost

def is_final(hall,rooms):
    if any(hall):
        return False
    
    for i in range(0,4):
        if rooms[i] != (i,i):
            return False

    return True

def hall_to_room(amphi,h,hall,rooms):

    room_index = {0:1.5, 1:2.5, 2:3.5, 3:4.5}
    j = room_index[amphi]
    k = int(ceil(j))

    newhall = list(hall)
    newrooms = [list(room) for room in rooms]

    if h<j:
        intervening_hall = [obj!=None for obj in hall[h+1:k]]

    if h>j:
        intervening_hall = [obj!=None for obj in hall[k:h]]
    
    wrong_amphi = [(x!=amphi and x!=None) for x in rooms[amphi]]

    if any(intervening_hall) or any(wrong_amphi):
        return None

    if not (any(intervening_hall) or any(wrong_amphi)):
        r_pos = len(rooms[amphi]) - 1 - sum([x==amphi for x in rooms[amphi]])
        cost = move_cost(amphi,h,amphi,r_pos)
        newhall[h] = None
        newrooms[amphi][r_pos] = amphi
        newhall = tuple(newhall)
        newrooms = tuple([tuple(newroom) for newroom in newrooms])
        return (newhall, newrooms, cost)

def room_to_hall(r,h,amphi,hall,rooms, r_pos):
    room_index = {0:1.5, 1:2.5, 2:3.5, 3:4.5}
    j = room_index[r]
    k = int(ceil(j))

    newhall = list(hall)
    newrooms = [list(room) for room in rooms]

    if h<j:
        intervening_hall = [obj!=None for obj in hall[h:k]]

    if h>j:
        intervening_hall = [obj!=None for obj in hall[k:h+1]]
    
    if r_pos == 0:
        intervening_room = [None]
    
    if r_pos != 0:
        intervening_room = [obj!=None for obj in rooms[r][0:r_pos]]

    if any(intervening_hall) or any(intervening_room):
        return None
    
    if not (any(intervening_hall) or any(intervening_room)):
        cost = move_cost(r,h,amphi,r_pos)
        newhall[h] = amphi
        newrooms[r][r_pos] = None
        newhall = tuple(newhall)
        newrooms = tuple([tuple(newroom) for newroom in newrooms])
        return (newhall, newrooms, cost)

def neighbours(hall,rooms):
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
    
    while not visit.empty():
        (c,_,(hall,rooms)) = visit.get()

        #print(c)

        if hall == final_hall and rooms == final_rooms:
            return c
        

        nbs = neighbours(hall,rooms)

        for nb in nbs:
            newc = c + nb[2]
            if newc < costs[(nb[0],nb[1])]:
                costs[(nb[0],nb[1])] = newc
                visit.put((newc, next(unique),(nb[0],nb[1])))



start_hall = (None,None,None,None,None,None,None)
start_rooms = ((3,3,3,3),(2,2,1,2),(0,1,0,1),(1,0,2,0))

final_hall = (None,None,None,None,None,None,None)
final_rooms = ((0,0,0,0),(1,1,1,1),(2,2,2,2),(3,3,3,3))


start_costs = defaultdict(lambda : inf)
start_costs[(start_hall,start_rooms)] = 0
unique=count()

visit = PriorityQueue()
visit.put((0,next(unique),(start_hall,start_rooms)))


print(dijkstra(visit,start_costs))





























