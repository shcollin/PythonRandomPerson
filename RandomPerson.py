from RandomNameGenerator import RandomNameGenerator
from RandomPhoneNumberGenerator import RandomPhoneNumberGenerator

phone = RandomPhoneNumberGenerator(1)
name = RandomNameGenerator("RandomNameGenerator/first-names.txt",
                           "RandomNameGenerator/middle-names.txt", "RandomNameGenerator/names.txt")
print(name.randomNameRandom() + " " + phone.randomPhone())
