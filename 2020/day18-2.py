import sys
from pyparsing import *

integer = pyparsing_common.integer

arith_expr = infixNotation(
    integer,
    [
        ('+',2,opAssoc.LEFT),
        ('*',2,opAssoc.LEFT)
    ]
)

with open(sys.argv[1]) as file:
    lines = file.readlines()

def parse(string):
    return eval(str(arith_expr.parseString(string)))

def apply(op,val1,val2):
    x = str(val1) + op + str(val2)
    return str(eval(x))


def evaluate(exp):
    val_stack = []
    op_stack = []

    for x in exp:
        
        if type(x) is str:
            if x in {'+','*'}:
                op_stack.append(x)

        elif type(x) is list:
            val_stack.append(evaluate(x))

        else:
            val_stack.append(str(x))

    for op in op_stack:
        new_vals = []
        new_vals.append(apply(op,val_stack[0],val_stack[1]))
        new_vals += val_stack[2:]
        val_stack = new_vals

    return val_stack[0]

summ = 0

for line in lines:
    exp = parse(line)
    y = int(evaluate(exp))
    #print(y)
    summ = summ + y

print(summ)
