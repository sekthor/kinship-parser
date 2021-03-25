from Population import Population
from Person import Person
import matplotlib.pyplot as plt

file_path = "dataset.csv"

class PopulationGraph():
    def __init__(self, population):
        assert isinstance(population, Population)
        self.population = population

    def cluster_by_age(self, people):
        assert isinstance(people, list)
        ages = []
        clusters = []
        for p in people:
            assert isinstance(p, Person)

            if p.age not in ages:
                ages.append(p.age)

            index = ages.index(p.age)

            if len(clusters) <= index:
                clusters.append([])
            
            clusters[index].append(p)

        return clusters
            

    def compute_coordinates(self):
        DISTANCE_BETWEEN_CAMPS = 2
        generation_start = 0
        max_x = 0
        coordinates = []

        for camp in self.population.get_camps():
            people = self.population.get_people_by_camp(camp)
            people = self.cluster_by_age(people)

            # find generation with most people
            # it's the maximum with of this camp
            max_x = max([len(x) for x in people])

            for generation in people:
                current_x = 0
                for person in generation:
                    coordinates.append([person.person_id, generation_start + current_x, person.age])
                    current_x += 1

            generation_start += max_x + DISTANCE_BETWEEN_CAMPS

        return coordinates

    def plot_graph(self):
        coordinates = self.compute_coordinates()

        # specify size of graph
        plt.xlim([0, max([x[1] for x in coordinates])])
        plt.ylim([0, max([x[2] for x in coordinates])])

        x_coords = []
        y_coords = []

        for person in coordinates:
            x_coords.append(person[1])
            y_coords.append(person[2])
            plt.annotate(str(person[0]), (person[1], person[2]))

            # draw lines to coordinates of kids
            kids = self.population.find_person_by_id(person[0]).children
            if kids == None:
                continue

            for child in kids:
                index = [x[0] for x in coordinates].index(child.person_id)
                x_coord = [person[1], coordinates[index][1]]
                y_coord = [person[2], coordinates[index][2]]

                plt.plot(x_coord, y_coord, color="gray")

        plt.scatter(x_coords,y_coords)
        plt.show()

        pass
            
