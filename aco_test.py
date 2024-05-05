from ant_colony_optimization import *
from read_test import *

def test_custom(test_name):
    print(test_name)
    distance, opt_tour, opt_cost = read_test_case(test_name)
    n = distance.shape[0]
    graph = Graph(n, distance)
    tour = ant_colony_optimization(graph, iterations=200)
    cost = calculate_cycle_length(distance, tour)
 
    print("Optimal tour:", opt_tour)
    print("Optimal cost:", opt_cost)
    print("Predict tour:", tour)
    print("Predict cost:", cost)
    print("-"*50)   


if __name__ == "__main__":
    test_custom("berlin52")
    test_custom("bier127")
    test_custom("tsp225")
