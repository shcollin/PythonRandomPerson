import random
import string


class RandomEmailGenerator:

    def randomGmail(self):
        i = 1
        return str(self.randomHandle()) + "@gmail.com"

    def randomOutlook(self):
        i = 1
        return str(self.randomHandle()) + "@outlook.com"

    def randomHandle(self):
        val = ''
        i = random.randint(1, 26)
        for n in xrange(1, i):
            val = val + random.choice(string.ascii_lowercase)
        return val
