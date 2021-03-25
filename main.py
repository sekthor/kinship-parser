from Population import Population
from Kinship import Kinship


# main method
def main():
    file_path = "dataset.csv"

    population = Population()
    population.read_population_from_file(file_path)

    print(population)


    
# entry point of program
if __name__ == "__main__":
    main()
