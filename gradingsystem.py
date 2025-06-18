totalmarks=0
for i in range(5):
    marks=int(input(f"enter values{i}"))
    totalmarks+=marks #every input gets added
    avg=totalmarks/5  #avg is being taken
if avg>=90:
    print("you got A+! Excelent!")#average is being used
elif avg>=80:
    print("You got A! good job!")
elif avg>=60:
    print("You got B! keep it up and try harder next time!")#we can also add c and d
else:#less than 50
    print("F!!")#more grading sytems can be added
print(avg)
