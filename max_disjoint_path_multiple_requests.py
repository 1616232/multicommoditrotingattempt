from pulp import *

edges = [(0, 1, 3), (0, 2, 2), (6, 3, 4), (0, 3, 2), (1, 4, 5),
         (1, 5, 1), (2, 4, 1), (2, 5, 3), (2, 6, 1), (3, 5, 1), (4, 7, 4), (5, 7, 2), (6, 7, 4)]

# edges = []
commodoties = [(0, 3), (6,2)]  # source, destination
vertices = list(range(0, 8))

sum_incoming = [[None] * len(vertices)] * len(commodoties)
sum_outgoing = [[None] * len(vertices)] * len(commodoties)
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
# capacity restriction; do we need to account for both directions?
for e in edges:
    model += (lpSum((x[(e[0], e[1], c)]+x[(e[1], e[0], c)]) for c in range(len(commodoties))) <= e[2])

for c in range(len(commodoties)):
    for j in range(len(vertices)):
        sum_incoming[c][j] = lpSum(x[(s, d, com)] for (s, d, com) in x if vertices[j] == d and com == c)
        sum_outgoing[c][j] = lpSum(x[(s, d, com)] for (s, d, com) in x if vertices[j] == s and com == c)

for j in range(len(vertices)):
    model += (lpSum(sum_outgoing[0][j] <=1))

model += (lpSum(sum_incoming[0][len(vertices)-1]))

model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Status:", LpStatus[model.status])