import sys

with open(sys.argv[1]) as file:
    data = file.read().strip()

data = data.replace('target area: x=','').replace('y=','').replace('..',', ').split(', ')

x_min = int(data[0])
x_max = int(data[1])
y_min = int(data[2])
y_max = int(data[3])

print(data)

def on_target(vx, vy):
    x=0
    y=0
    while y>=y_min:
        x += vx
        y += vy

        if x_min <= x <= x_max  and y_min <= y <= y_max:
            return True
        
        if vx > 0:
            vx -= 1

        if vx == 0:
            if x<x_min:
                return False
        
        if vx < 0:
            vx += 1
        
        vy -= 1
    
    return False

on_target_probes = 0
for ux in range(1,x_max+1):
    for uy in range(y_min,-y_min):
        is_on_target = on_target(ux,uy)
        if is_on_target == True:
            on_target_probes += 1

print(on_target_probes)




