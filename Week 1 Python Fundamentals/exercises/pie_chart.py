import matplotlib.pyplot as plt

subjects = ["Maths","Science","English"]

marks = [78,82,75]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')

plt.title("Subject Marks Distribution")

plt.show()