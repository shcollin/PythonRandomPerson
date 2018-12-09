import random


class RandomNameGenerator:

    def __init__(self, firstNames, middleNames, lastNames):
        self.firstNames = firstNames
        self.middleNames = middleNames
        self.lastNames = lastNames

    def getLineCount(self, filename):
        file = open(filename, 'r')
        n = len(file.readlines())
        file.close()
        return n

    def getRandomNumber(self, mod):
        return random.randint(0, mod)

    def randomFirstNameGenerator(self):
        n = self.getLineCount(self.firstNames)
        file_object = open(self.firstNames, 'r')
        lines = file_object.readlines()[self.getRandomNumber(n)]
        file_object.close()
        lines = lines.rstrip()
        return lines + " "

    def randomMiddleNameGenerator(self):
        n = self.getLineCount(self.middleNames)
        fileObject = open(self.middleNames, 'r')
        lines = fileObject.readlines()[self.getRandomNumber(n)]
        fileObject.close()
        lines = lines.rstrip()
        return lines + " "

    def randomLastNameGenerator(self):
        n = self.getLineCount(self.lastNames)
        file_object = open(self.lastNames, 'r')
        lines = file_object.readlines()[self.getRandomNumber(n)]
        file_object.close()
        lines = lines.rstrip()
        return lines

    def randomName(self):
        return self.randomFirstNameGenerator() + self.randomLastNameGenerator()

    def randomNameMiddleIn(self):
        i = self.randomMiddleNameGenerator()[0] + ". "
        return self.randomFirstNameGenerator() + i + self.randomLastNameGenerator()

    def randomNameMiddleFull(self):
        return self.randomFirstNameGenerator() + self.randomMiddleNameGenerator() + self.randomLastNameGenerator()

    def randomNameRandom(self):
        i = random.randint(0, 2)
        if(i == 0):
            return self.randomName()
        elif(i == 1):
            return self.randomNameMiddleIn()
        else:
            return self.randomNameMiddleFull()

    def function(self):
        return randomFirstNameGenerator(firstNames)
