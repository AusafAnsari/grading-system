import firebase_admin
from firebase_admin import credentials ,db
cred = credentials.Certificate("C:/Users/adminb/Desktop/python/new-python-b010f-firebase-adminsdk-fbsvc-e4e0096baf.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app (cred,{"databaseURL":"https://new-python-b010f-default-rtdb.firebaseio.com/"})

totalmarks=0
for i in range(5):
    marks=int(input(f"enter values of {i} "))
    totalmarks+=marks #every input gets added
    avg=totalmarks/5  #avg is being taken
if avg>=90:
    z="you got A+! Excelent!"#average is being used
elif avg>=80:
    z="You got A! good job!"
elif avg>=60:
    z="You got B! keep it up and try harder next time!"#we can also add c and d
else:#less than 50
    z="F!!"#more grading sytems can be added
print(avg)
print(z)

ref=db.reference('Ansari')
ref.push({
"grade":z,
"average":avg
}  )
print("data sent successfull")