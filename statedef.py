import json

# read file
f =  open("file.json", "r")
data = json.loads(f.read())
f.close()

# declare variabless
states = data["matrix"]
eventNames = data["order"]
stateNames = []

# get state names
for i in range(len(states)):
    stateNames.append(states[i]["name"])

print(stateNames)
print(eventNames)

# create matrix
matrix = []
for i in range(len(stateNames)):
    matrix.append([])
    for j in range(len(eventNames)):
        matrix[i].append(0)

# fill matrix
for i in range(len(stateNames)):
    for event in states[i]["transitions"]:
        matrix[i][eventNames.index(event)] = stateNames.index(states[i]["transitions"][event])

realMatrix = tuple(matrix)
print(realMatrix)
