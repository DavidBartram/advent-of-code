def run(code):
    
    visited = set()

    i=0
    acc = 0

    terminates = False

    while i not in visited:
        visited.add(i)

        if i == len(code):
            terminates = True
            break
        
        else:
            op,arg = code[i].split()
            arg = int(arg)

            if op == "nop":
                i += 1
            elif op == "acc":
                acc += arg
                i += 1
            elif op == "jmp":
                i += arg

    return {'lastline': i, 'acc': acc, 'terminates': terminates }


def findswap(filename):

    with open(filename) as file:
        code = [line.rstrip('\n') for line in file]

    for i in range(0,len(code)):
        
        code2 = code[:]
        
        
        if code2[i].startswith("nop"):
            code2[i] = code2[i].replace("nop", "jmp")
            

        if code2[i].startswith("jmp"):
            code2[i] = code2[i].replace("jmp", "nop")
            

        result = run(code2)
        terminates = result["terminates"]

        if terminates == True:
            acc = result["acc"]
            print("Swapping line", i, "makes the code terminate with acc =", acc)
            break
    

findswap("bootcode.txt")
