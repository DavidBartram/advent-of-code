import sys

#read the input data to find the boundaries of the target area
with open(sys.argv[1]) as file:
    data = file.read().strip()

data = data.replace('target area: x=','').replace('y=','').replace('..',', ').split(', ')

x_min = int(data[0])
x_max = int(data[1])
y_min = int(data[2])
y_max = int(data[3])

def on_target(vx, vy):
    #determine whether an initial velocity (vx,vy) results in the probe
    #being inside the target area after any step
    x=0
    y=0
    while y>=y_min: #while the probe is above the bottom of the target area
                    #once it goes below the target area it will never be on target
                    #as y-velocity is always decreasing
        x += vx
        y += vy

        if x_min <= x <= x_max  and y_min <= y <= y_max: #if the position is in the target area
            return True
        
        if vx > 0:
            vx -= 1

        if vx == 0:
            if x<x_min or x>x_max:
                return False    #if the probe is left or right of the target area and has x-velocity zero
                                #it will never reach the target area
        
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




