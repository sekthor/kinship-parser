
from Kinship import Kinship
from Person import Person


# A population is a list of people and a list of kinships of these people
class Population:
    def __init__(self):
        self.population = []
        self.kinships = []

    # add a list of people
    def add_people(self, people):
        for p in people:
            assert isinstance(p, Person)
            self.population.append(p)

    # add a single person
    def add_person(self, person):
        assert isinstance(person, Person)
        self.population.append(person)

    def add_kinships(self, kinships):
        for k in kinships:
            assert isinstance(k, Kinship)
            self.kinships.append(k)

    def add_kinship(self, kinship):
        assert isinstance(kinship, Kinship)
        self.kinships.append(kinship)

    # returns all kinships of a given person p
    def get_kinships(self, p): 
        ks = []
        person = p 
        for k in self.kinships:
            if k.is_member(person):
                ks.append(k)
        return ks

    def get_camps(self):
        camps = []
        for p in self.population:
            if p.camp not in camps:
                camps.append(p.camp)
        return camps

    def find_person_by_id(self, pid):
        for p in self.population:
            if p.person_id == pid:
                return p

    def marry_by_id(self, pid1, pid2):
        p1 = self.find_person_by_id(pid1)
        p2 = self.find_person_by_id(pid2)

        if p1 == None or p2 == None:
            return

        p1.setSpouse(p2)
        p2.setSpouse(p1)

    # checks if child is actually child of parent
    # check if child has kinship of 0.5 to parent and also to spouse of parent
    # Rule 1: kinship of 0.5
    # Rule 2: kinship of child and spouse of potential parent also 0.5
    def is_child(self, child, parent, kinship):
        assert isinstance(child, Person)
        assert isinstance(parent, Person)
        assert isinstance(kinship, Kinship)

        # if child and parent do not have kinship of 0.5,
        # they aren't actually child and parent
        if kinship.kinship_factor != 0.5:
            return False

        # check if spouse of potential parent is also related
        for ks in self.get_kinships(child):
            if parent.spouse == None:
                continue
            if ks.is_member(parent.spouse):
                if ks.kinship_factor == 0.5:
                    return True

        return False

    def process_kinships_children(self):
        for ks in self.kinships:
            
            if ks.kinship_factor != 0.5:
                continue

            if self.is_child(ks.person_b, ks.person_a, ks) \
                and ks.person_b not in ks.person_a.children:
                ks.person_a.addChild(ks.person_b)

            elif self.is_child(ks.person_a, ks.person_b, ks) \
                and ks.person_a not in ks.person_b.children:
                ks.person_b.addChild(ks.person_a)

    def __str__(self):
        s = ""
        for p in self.population:
            s += p.__str__() + " " \
                    + str(p.spouse) + " [" \
                    + " ".join([str(x) for x in p.children]) \
                    + "]\n"
        return s

    def read_population_from_file(self, file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
            del lines[0]    # skip first line

        self.read_people(lines)
        self.read_kinships(lines)
        self.read_marriages(lines)
        self.process_kinships_children()

    def get_people_by_camp(self, camp):
        people = []
        for p in self.population:
            if p.camp == camp:
                people.append(p)
        return people

    def read_people(self, lines):
        p_ids = []

        for line in lines:
            line = line.split(",")

            # receiver
            if line[0] not in p_ids:
                pid = int(line[0])
                age = int(line[1])
                sex = line[2]
                camp = line[3]
                person = Person(pid, age, sex, camp)
                p_ids.append(line[0])
                self.population.append(person)

            # giver
            if line[4] not in p_ids:
                pid = int(line[4])
                age = int(line[5])
                sex = line[6]
                camp = line[7]
                person = Person(pid, age, sex, camp)
                p_ids.append(line[4])
                self.population.append(person)

    def read_kinships(self, lines):
        for line in lines:
            line = line.strip("\n")
            line = line.split(",")

            p1 = self.find_person_by_id(int(line[0]))
            p2 = self.find_person_by_id(int(line[4]))

            if p1 == None or p2 == None:
                continue

            k = Kinship(p1, p2, float(line[8]))
            self.add_kinship(k)

    def read_marriages(self, lines):
        for line in lines:
            line = line.strip("\n")
            line = line.split(",")

            if line[9] == "0":
                continue

            pid1 = int(line[0])
            pid2 = int(line[9])

            self.marry_by_id(pid1, pid2)