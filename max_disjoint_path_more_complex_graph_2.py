from pulp import *
# graph based on image from https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/NetFlow/max-flow-lp.html
edges = [(0, 1, 3), (0, 2, 2), (0, 3, 2), (1,4,5), (1,5,1), (2,4,1), (2,5,3,), (2,6,1), (3,5,1), (4,7,4), (5,7,2), (6,7,4)]
edges_without_capacity = list(map(lambda e: (e[0], e[1]), edges)) + list(map(lambda e: (e[1], e[0]), edges))
print(edges_without_capacity)
# edges = []
commodoties = [(0, 4)]  # source, destination
vertices = list(range(0, 8))

model = LpProblem(name="max-disjoint-paths", sense=LpMaximize)
# set of variables; total number is edges times commodoties
# directed or undirected graph?
# x = {(e[0], e[1], c): LpVariable(name=f"x{e[0]}" + f"{e[1]}" + f"{c}", lowBound=0) for e in edges for c in
#      range(len(commodoties))}
x = {}
for e in edges:
    for c in range(len(commodoties)):
        x[(e[0], e[1], c)] = LpVariable(name=f"x{e[0]}" + f"{e[1]}" + f"{c}", lowBound=0)
        x[(e[1], e[0], c)] = LpVariable(name=f"x{e[1]}" + f"{e[0]}" + f"{c}", lowBound=0)

# objective: maximize flows to destination
model += (
    lpSum(x[(v,commodoties[c][1],c)] for c in range(len(commodoties)) for v in vertices if ((v,commodoties[c][1]) in edges_without_capacity)),
    "sum of flow to destination"
)
print(commodoties[0][1])
print(model.constraints())
print(model.objective)
# capacity restriction
for e in edges:
    model += (lpSum((x[(e[0], e[1], c)]+x[(e[1], e[0], c)]) for c in range(len(commodoties))) <= e[2])
print(model.constraints())

#flow restriction
for j in range(len(vertices)):
    for k in range(len(commodoties)):
        if j != commodoties[k][0] and j != commodoties[k][1]:
            model += lpSum(x[(j,v,k)] for v in vertices if (j,v) in edges_without_capacity) == lpSum(x[(v,j,k)] for v in vertices if (v,j) in edges_without_capacity)
print(model.constraints())
#for each commodity outflow from source is equal to inflow at destination
for k in range(len(commodoties)):
    model+=  lpSum(x[(v,commodoties[k][1],k)] for v in vertices if (v,commodoties[k][1]) in edges_without_capacity) == lpSum(x[(commodoties[k][0],v,k)] for v in vertices if (commodoties[k][0],v) in edges_without_capacity)
print(model.constraints())
# to enforce vertex disjoint paths, for each commodity, inflow into a node is capped at 1 unless the node is the destination
# flow from the destination is zero for that commodity
for k in range(len(commodoties)):
    for v in range(len(vertices)):
        if commodoties[k][1] !=v:
            model += lpSum(x[(i,v,k)] for i in vertices if ((i,v) in edges_without_capacity)) <=1
        else:
            model += lpSum(x[(v,i,k)] for i in vertices if ((i,v) in edges_without_capacity)) == 0
print(model.constraints())
model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Status:", LpStatus[model.status])