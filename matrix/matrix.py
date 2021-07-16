class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
    

    def row(self, index):
        self.row = self.matrix.split('\n')
        self.row = [e.split() for e in self.row]
        self.row = [[int(j) for j in i]for i in self.row]
        return self.row[index-1]

    def column(self, index):
        self.row = self.matrix.split('\n')
        self.row = [e.split() for e in self.row]
        self.row = [[int(j) for j in i]for i in self.row]
        return [i[index-1] for i in self.row]
