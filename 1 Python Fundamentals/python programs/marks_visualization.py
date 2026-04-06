import matplotlib.pyplot as plt

students = ["Rahul","Aman","Priya","Riya","Karan"]

marks = [78,85,90,67,88]

plt.bar(students, marks)

plt.title("Student Performance")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()