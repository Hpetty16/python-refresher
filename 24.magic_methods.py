#function
def average(sequence):
    return sum(sequence) / len(sequence)


#Method
class Student:
    def __init__(self):  # method
        self.name = "Rolf"
        self.grades = (79, 90, 95, 99)
    
    def average(self):  # method
        return sum(self.grades) / len(self.grades)