class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_exam(self, grade):
        self.grades.append(float(grade))

    def get_mean(self):
        if not self.grades:
            return 0.0
        else:
            return sum(self.grades) / len(self.grades)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_mean(self):
        averages = []
        for student in self.students:
            averages.append(student.get_mean())
        return sum(averages) / len(self.students)

    def get_best_student(self):
        highest_avg = 0
        best = ""
        for student in self.students:
            avg = student.get_mean()
            if avg > highest_avg:
                highest_avg = avg
                best = student
            else:
                pass
        return best

class City:
    def __init__(self, name):
        self.name = name
        self.schools = []

    def add_school(self, school):
        self.schools.append(school)

    def get_mean(self):
        averages = []
        for school in self.schools:
            averages.append(school.get_mean())
        return sum(averages) / len(self.schools)

    def get_best_school(self):
        best = ""
        highest_avg = 0
        for school in self.schools:
            avg = school.get_mean()
            if avg > highest_avg:
                best = school
                highest_avg = avg
            else:
                pass
        return best

    def get_best_student(self):
        best_student = ""
        max_avg = 0
        for school in self.schools:
            current_best_student = school.get_best_student()
            avg = current_best_student.get_mean()
            if avg > max_avg:
                best_student = current_best_student
                max_avg = avg
            else:
                pass
        return best_student.name


#Test case

s1 = Student("Alice")
s1.add_exam(90)
s1.add_exam(95)

s2 = Student("Bob")
s2.add_exam(80)

school = School("High School")
school.add_student(s1)
school.add_student(s2)

city = City("Springfield")
city.add_school(school)

print("City average:", city.get_mean())
print("Best student:", city.get_best_student())