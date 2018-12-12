import random
import string


class RandomEmailGenerator:

    def randomGmail(self):
        return str(self.randomHandle()) + "@gmail.com"

    def randomOutlook(self):
        return str(self.randomHandle()) + "@outlook.com"

    def randomYahoo(self):
        return str(self.randomHandle()) + "@yahoo.com"

    def randomHandle(self):
        val = ''
        i = random.randint(1, 26)
        for n in xrange(1, i):
            val = val + random.choice(string.ascii_lowercase)
        return val

    def randomEmail(self):
        i = random.randint(0, 2)
        if(i == 0):
            return self.randomGmail()
        elif(i == 1):
            return self.randomYahoo()
        else:
            return self.randomOutlook()
