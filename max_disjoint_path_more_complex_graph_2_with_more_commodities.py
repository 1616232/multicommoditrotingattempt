# graph based on image from https://www.cs.emory.edu/~cheung/Courses/253/Syllabus/NetFlow/max-flow-lp.html
from max_disjoint_path_solve_method import solve_max_disjoint_path_problem

edges = [(0, 1, 3), (0, 2, 2), (0, 3, 2), (1,4,5), (1,5,1), (2,4,1), (2,5,3,), (2,6,1), (3,5,1), (4,7,4), (5,7,2), (6,7,4)]

commodoties = [(0, 4), (3,6)]  # source, destination
vertices = list(range(0, 8))
solve_max_disjoint_path_problem(edges,commodoties,vertices)
