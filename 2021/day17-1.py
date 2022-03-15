import sys

#parse the input data to find the target area
with open(sys.argv[1]) as file:
    data = file.read().strip()

data = data.replace('target area: x=','').replace('y=','').replace('..',', ').split(', ')

x_min = int(data[0])
x_max = int(data[1])
y_min = int(data[2])
y_max = int(data[3])

def get_height(vx, vy):
    x=0
    y=0
    height = 0
    on_target = False

    while y>=y_min:
        x += vx
        y += vy

        if x_min <= x <= x_max  and y_min <= y <= y_max:
            on_target = True

        if y > height:
            height = y
        
        if vx > 0:
            vx -= 1
        
        if vx < 0:
            vx += 1
        
        vy -= 1
    
    return height, on_target

max_height=0
for ux in range(1,x_max):
    for uy in range(y_min,500):
        height, on_target = get_height(ux,uy)
        if on_target == True and height > max_height:
            max_height = height

print(max_height)




