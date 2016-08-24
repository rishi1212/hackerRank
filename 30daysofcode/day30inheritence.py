class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = []
        for s in scores:
            self.scores.append(int(s))
    def calculate(self):
        a = float(sum(self.scores))/len(self.scores)
        if a < 40:
            return 'T'
        elif a < 55:
            return 'D'
        elif a < 70:
            return 'P'
        elif a < 80:
            return 'A'
        elif a < 90:
            return 'E'
        else:
            return 'O'