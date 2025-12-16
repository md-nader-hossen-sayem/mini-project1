
#I am starting learning Python. 

student_details = {
    "001" : {"name" : "Sayem", "marks" : [89, 68, 80, 93]},
    "002" : {"name" : "Sakib", "marks" : [77, 83, 92, 55]},
    "003" : {"name" : "Fateha", "marks" : [88, 95, 54, 76]}
}

print("What do you want?")
print("1. Print Students Details")
print("2. Add New Student")
choice = input("Enter your choice : ")

if choice == "1":
    for key, values in student_details.items():
        print("------------------")
        print("\nID : ", key)
        print("------------------")
        print("Name : ", values["name"])

        marks = values["marks"]
        avg = sum(marks) / len(marks)
        print("Average : ", avg)

        if avg < 50:
            grade = "F"
        elif avg < 65:
            grade = "C"
        elif avg < 80:
            grade = "B"
        else:
            grade = "A"

        print("Grade :", grade)

elif choice == "2":
    id = input("Enter a new ID : ")
    name = input ("Enter student name : ")

    marks = []
    for i in range(4):
        m = int(input(f"Enter mark {i+1} : "))
        marks.append(m)

    student_details[id] = {
        "name" : name,
        "marks" : marks
    }

    print("Student added successfully!")

else:
    print("Invalid choice")