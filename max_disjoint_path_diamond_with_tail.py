# graph based on suggestion from Aljawharah
from max_disjoint_path_solve_method import solve_max_disjoint_path_problem

edges = [(0, 1, 3), (1, 2, 3), (1, 3, 3), (2,4,3), (3,4,3)]

commodoties = [(0, 4), (0,3)]  # source, destination
vertices = list(range(0, 5)) # lowest index, highest index + 1
solve_max_disjoint_path_problem(edges,commodoties,vertices)
