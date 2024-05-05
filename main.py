# Import model
from aco_tsp import SolveTSPUsingACO

def read_tsp_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    node_coord_section_index = lines.index('NODE_COORD_SECTION\n')

    # Extracting node coordinates
    nodes = []
    for line in lines[node_coord_section_index + 1:]:
        if line.strip() == 'EOF':
            break

        node_id, x, y = map(float, line.strip().split())
        nodes.append((x, y))
    
    return nodes

def test(mode, test_file, number_of_runs=10):
    print(f"Test {mode} - {test_file}")
    # Setup parameters
    _colony_size = 15
    _steps = 200

    # Select mode
    # ['ACS', 'Elitist', 'MaxMin']
    _mode = mode

    # Nodes (latitude and longitude)
    _nodes = read_tsp_file(test_file)

    res = []
    for i in range(number_of_runs):
        # Model setup and run
        model = SolveTSPUsingACO(
            mode = _mode,
            colony_size = _colony_size,
            steps = _steps,
            nodes = _nodes
        )

        runtime, distance, tour = model.run()
        print("Run ", i)
        print("Tour", tour)
        print("Distance", distance)
        print("-"*50)
        res.append(distance)
        
    print("Min: ", min(res))
    print("Max: ", max(res))
    print("Avg: ", sum(res)/len(res))

if __name__ == "__main__":
    # ACS berlin52.tsp
    test("ACS", "berlin52.tsp")
    
    # # ACS bier127.tsp
    # test("ACS", "bier127.tsp")
    
    # # ACS tsp225.tsp
    # test("ACS", "tsp225.tsp")
    
    # # MMAS berlin52.tsp
    # test("MaxMin", "berlin52.tsp")
    
    # # MMAS bier127.tsp
    # test("MaxMin", "bier127.tsp")
    
    # # MMAS tsp225.tsp
    # test("MaxMin", "tsp225.tsp")
    