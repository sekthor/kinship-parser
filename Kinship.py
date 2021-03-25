from Person import Person

# a kinship consists of two people and a kinship factor
class Kinship:
    def __init__(self, person_a, person_b, kinship):
        assert isinstance(person_a, Person)
        assert isinstance(person_b, Person)
        assert isinstance(kinship, float)
        self.person_a = person_a
        self.person_b = person_b
        self.kinship_factor = kinship

    def get_kinship_factor(self):
        return self.kinship_factor

    def is_member(self, person):
        if person == None:
            return False
        assert isinstance(person, Person)
        return self.person_a.person_id == person.person_id \
                or self.person_b.person_id == person.person_id

    def __str__(self):
        return "" + str(self.person_a) \
            + " <" + str(self.kinship_factor) + "> " \
            + str(self.person_b)