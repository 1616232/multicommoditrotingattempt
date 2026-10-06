from max_disjoint_path_solve_method import solve_max_disjoint_path_problem

edges = [(0, 1, 1), (1, 2, 1)]
commodoties = [(0, 2), (1, 2)]  # source, destination
vertices = list(range(0, 3))
solve_max_disjoint_path_problem(edges,commodoties,vertices)
