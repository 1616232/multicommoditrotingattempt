from max_disjoint_path_solve_method import solve_max_disjoint_path_problem

edges = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (1,4,1), (2,4,1), (3,4,1)]

# edges = []
commodoties = [(0, 4)]  # source, destination
vertices = list(range(0, 5))

solve_max_disjoint_path_problem(edges,commodoties,vertices)

