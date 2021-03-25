from Population import Population
from Kinship import Kinship
from PopulationGraph import PopulationGraph


# main method
def main():
    file_path = "dataset.csv"

    population = Population()
    population.read_population_from_file(file_path)

    graph = PopulationGraph(population)
    graph.plot_graph()




    
# entry point of program
if __name__ == "__main__":
    main()
