from RandomNameGenerator import RandomNameGenerator
from RandomPhoneNumberGenerator import RandomPhoneNumberGenerator
from RandomEmailGenerator import RandomEmailGenerator


class RandomPerson:

    def __init__(self):
        self.phoneNumber = RandomPhoneNumberGenerator(1).randomPhone()
        self.name = RandomNameGenerator("RandomNameGenerator/first-names.txt",
                                        "RandomNameGenerator/middle-names.txt", "RandomNameGenerator/names.txt").randomNameRandom()
        self.email = RandomEmailGenerator().randomEmail()

    def printPerson(self):
        print(self.name + " " + self.phoneNumber + " " + self.email)

    def getJSON(self):
        d = "{phoneNumber: \""
        d += self.phoneNumber + "\", "
        d += "name: \"" + self.name + "\", "
        d += "email: \"" + self.email + "\"}"
        return d

for x in xrange(1, 10):
    person = RandomPerson()
    # person.printPerson()
    print(person.getJSON())
