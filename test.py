from problem import Problem
from search import LocalSearchStrategy
from itertools import chain

if __name__ == "__main__":
    problem = Problem('monalisa.jpg')  
    search_strategy = LocalSearchStrategy()
    
    path = search_strategy.random_restart_hill_climbing(problem, 10)
    problem.draw_path([(x, y) for x, y, z in path],"Random Restart Hill-Climbing")
    
    print("Đường đi tìm được bằng phương pháp Random Restart Hill Climbing:")
    for state in path:
        print(state)
        
    schedule = lambda t: max(100 - 0.5 * t, 0)
    path_sa = search_strategy.simulated_annealing_search(problem, schedule)
    problem.draw_path([(x, y) for x, y, z in path_sa],"Simulated Annealing Search")
    
    print("\nĐường đi tìm được bằng phương pháp Simulated Annealing:")
    for state in path_sa:
        print(state)
        
    k = 10
    path_lb = search_strategy.local_beam_search(problem, k)
    problem.draw_path([(x, y) for x, y, z in path_lb],"Local Beam Search")
   
    print("\nĐường đi tìm được bằng phương pháp Local Beam Search:")
    for step in path_lb:
        print(step)