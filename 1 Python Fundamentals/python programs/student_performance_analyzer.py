marks = []

for i in range(3):

    m = int(input("Enter marks: "))

    marks.append(m)

avg = sum(marks)/len(marks)

print("Average:", avg)

if avg >= 80:

    print("Excellent Performance")

elif avg >= 60:

    print("Good Performance")

else:

    print("Needs Improvement")