class Student:
    def _init_(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def accept(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        student = Student(roll_no, name)
        self.students.append(student)
        print("Student added successfully!")

    def display(self):
        if not self.students:
            print("No students found!")
        else:
            print("Students:")
            for student in self.students:
                print(f"Roll No: {student.roll_no}, Name: {student.name}")

    def search(self):
        roll_no = input("Enter Roll No to search: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found - Roll No: {student.roll_no}, Name: {student.name}")
                return
        print("Student not found!")

    def delete(self):
        roll_no = input("Enter Roll No to delete: ")
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found!")

    def update(self):
        roll_no = input("Enter Roll No to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter new Name: ")
                print("Student updated successfully!")
                return
        print("Student not found!")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Accept")
        print("2. Display")
        print("3. Search")
        print("4. Delete")
        print("5. Update")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            sms.accept()
        elif choice == '2':
            sms.display()
        elif choice == '3':
            sms.search()
        elif choice == '4':
            sms.delete()
        elif choice == '5':
            sms.update()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()