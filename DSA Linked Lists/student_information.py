# Student Information using Linked List
import random
import time


class Student:
    def __init__(self, sid, name, major, gpa):
        self.sid = sid
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return "{:<6} | {:<20} | {:<15} |{:<15}".format(self.sid, self.name, self.major, self.gpa)


class Node:
    def __init__(self, student):
        self.student = student
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, sid, name, major, gpa):
        student = Student(sid, name, major, gpa)
        temp = Node(student)
        # Empty list
        if not self.head:
            self.head = temp
            return

        if sid < self.head.student.sid:
            temp.next = self.head
            self.head = temp
            return

        prev = None
        current = self.head

        while current and current.student.sid < sid:
            prev = current
            current = current.next

        # Add new student
        prev.next = temp
        temp.next = current

    def remove_student(self, sid):  # Delete Student by SID
        if not self.head:
            print("Empty List")
            return

        # If the Head is deleted
        if self.head.student.sid == sid:
            self.head = self.head.next

        prev = None
        current = self.head

        while current and current.student.sid != sid:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
        else:
            print("Student not found")

    def display_student(self):
        current = self.head
        while current:
            print(current.student)
            current = current.next


def main():
    print("Student Information")
    number = random.randint(35, 42)
    students = StudentLinkedList()
    sid_list = []
    last_name = ["Nguyễn", "Đào", "Ngô", "Phan", "Lâm", "Phùng"]
    middle_name = ["Thị", "Hoàng", "Văn", "Trung", "Gia"]
    first_name = ["Dũng", "Đạt", "Nam", "Tâm", "Xuân", "Bảo"]
    major_list = ["IT", "AI", "CSC", "RES", "NID", "DIG"]
    for n in range(number):
        sid = random.randint(10000, 19999)
        name = (random.choice(last_name) + " " + random.choice(middle_name)
                + " " + random.choice(first_name))
        major = random.choice(major_list)
        gpa = random.randint(1, 10)
        students.add_student(sid, name, major, gpa)
        sid_list.append(sid)
    # Original Student List
    print("{:<10} {:<20} {:<15} {:<15}".format("SID", "Name", "Major", "GPA"))
    students.display_student()

    # Delete some students
    print("Delete Student")
    for i in range(number // 2):
        remove_sid = random.choice(sid_list)
        print(f"Delete Student {remove_sid}")
        students.remove_student(remove_sid)
        time.sleep(2)

    # New Student List
    print("Student List:")
    print("{:<10} {:<20} {:<15} {:<15}".format("SID", "Name", "Major", "GPA"))
    students.display_student()


main()
