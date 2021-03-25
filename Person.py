# definition of what a person is
class Person:
    def __init__(self, person_id, age, sex, camp):

        assert isinstance(person_id, int)
        assert isinstance(age, int)
        self.person_id = person_id
        self.age = age
        self.sex = sex
        self.camp = camp
        self.children = []
        self.spouse = None

    def setSpouse(self, person):
        assert isinstance(person, Person)
        self.spouse = person

    def addChild(self, person):
        assert isinstance(person, Person)
        self.children.append(person)

    def __str__(self):
        return "(" + format(self.person_id, "03d") + ", " \
                + str(self.age) + ", " \
                + str(self.sex) + ", " \
                + str(self.camp) + ")"