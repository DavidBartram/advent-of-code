def run(code):
    
    visited = set()

    i=0
    acc = 0

    while i not in visited:
        visited.add(i)
        op,arg = code[i].split()
        arg = int(arg)
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg
        
    return {'lastline': i, 'acc': acc}

def runfile(filename):
    
    with open(filename) as file:
        code = [line.rstrip('\n') for line in file]
    
    return run(code)

print(runfile("testbootcode.txt"))

print(runfile("bootcode.txt"))
