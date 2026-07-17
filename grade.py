a=int(input("enter a number "))
b=int(input("enter a number "))
c=int(input("enter a number "))
d=int(input("enter a number "))

average=(a+b+c+d)/4
print("the average is ",average)

if average > 90:
  print("the grade is A+")
elif average > 80 and average <= 90:
  print("the grade is A")
elif average > 70 and average <= 80:
  print("the grade is B+")
elif average > 60 and average <= 70:
  print("the grade is B")
elif average > 50 and average <= 60:
  print("the grade is C")
elif average > 40 and average <= 50:
  print("the grade is D")
else:
  print("Failed")
