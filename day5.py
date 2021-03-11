import sys

with open(sys.argv[1]) as file:
    lines = [line.rstrip('\n') for line in file]

rows = []
cols = []
IDs = []

for line in lines:
    rows.append(line[:7])
    cols.append(line[-3:])

rows = [row.replace("F","0").replace("B","1") for row in rows]
rows = [int(row,2) for row in rows]

cols = [col.replace("L","0").replace("R","1") for col in cols]
cols = [int(col,2) for col in cols]


for i in range(len(rows)):
    IDs.append(rows[i]*8 + cols[i])

#part 1
print(max(IDs))

#part 2
IDs.sort()

for i in range(len(rows)):
    if IDs[i] + 1 != IDs[i+1]:
        print(IDs[i] + 1)
        break
