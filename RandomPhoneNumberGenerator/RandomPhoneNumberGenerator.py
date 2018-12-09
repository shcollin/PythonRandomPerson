import random


class RandomPhoneNumberGenerator:

    def __init__(self, country):
        self.country = country

    def randomPhoneNumberDash(self):
        temp = str(self.country)
        temp = temp + "-"
        temp = temp + str(random.randint(100, 999)) + "-"
        temp = temp + str(random.randint(100, 999)) + "-"
        temp = temp + str(random.randint(1000, 9999))
        return temp

    def randomPhoneNumber(self):
        temp = str(self.country)
        temp = temp + str(random.randint(100, 999))
        temp = temp + str(random.randint(100, 999))
        temp = temp + str(random.randint(1000, 9999))
        return temp

    def randomPhone(self):
        temp = random.randint(0, 1)
        if(temp == 0):
            return self.randomPhoneNumberDash()
        else:
            return self.randomPhoneNumber()
