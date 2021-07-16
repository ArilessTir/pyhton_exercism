class School(dict):
    def __init__(self):
        self = dict()

    def add_student(self, name, grade):
        self[name] = grade

    def roster(self):
        roos = []
        tri = dict(sorted(self.items(), key= lambda x: (x[1],x[0])))
        for key in tri.keys():
            roos.append(key)
        return roos

    def grade(self, grade_number):
        gra = []
        tri = dict(sorted(self.items(), key=lambda x: (x[1], x[0])))
        for key,value in tri.items():
            if grade_number == value:
                gra.append(key)
        return gra