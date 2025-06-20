'''
Write a function telling apart accepted and refused students according to a threshold.

The function should be called select_student and takes as arguments:

A list where each element is a list of a student name, and his grade.
A grade. The student grade must be superior or equal to the given grade to be accepted.
Your function must return a dictionary with two entries:

Accepted which list the accepted students sorted by grades in the descending order.
Refused which list the refused students sorted by grades in ascending order.

https://genepy.org/exercises/select-students
'''

def select_student(students, threshold):
    results = {"Accepted": [], "Refused": []}

    for student in students:
        name, grade = student
        if grade >= threshold:
            results["Accepted"].append(student)
        else:
            results["Refused"].append(student)

    results["Accepted"] = sorted(results["Accepted"], key=lambda student: student[1], reverse=True)
    results["Refused"] = sorted(results["Refused"], key=lambda student: student[1])

    return results

'''
TEST
my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

select_student(my_class, 20)
'''