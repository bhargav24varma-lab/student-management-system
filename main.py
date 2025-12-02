import csv
import os
from datetime import datetime


def read_csv(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(file, fieldnames, data):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def append_csv(file, fieldnames, row):
    file_exists = os.path.exists(file) and os.path.getsize(file) > 0
    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)




def add_student():
    print("\n--- Add Student ---")
    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    sclass = input("Class: ")
    section = input("Section: ")

    append_csv("students.csv",
               ["student_id", "name", "age", "class", "section"],
               {"student_id": student_id, "name": name, "age": age, "class": sclass, "section": section})

    print("Student added successfully!")


def view_students():
    print("\n--- All Students ---")
    data = read_csv("students.csv")

    if not data:
        print("No student records found.")
        return

    for s in data:
        print(f"{s['student_id']} | {s['name']} | Age: {s['age']} | Class: {s['class']} | Section: {s['section']}")


def search_student():
    print("\n--- Search Student ---")
    query = input("Enter Student ID or Name: ").lower()
    data = read_csv("students.csv")

    found = False
    for s in data:
        if query in s["student_id"].lower() or query in s["name"].lower():
            found = True
            print(f"{s['student_id']} | {s['name']} | Age: {s['age']} | Class: {s['class']} | Section: {s['section']}")

    if not found:
        print("No matching student found.")


def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter Student ID to update: ")

    data = read_csv("students.csv")
    updated = False

    for s in data:
        if s["student_id"] == sid:
            print("Leave blank to keep old value.")

            name = input(f"Name [{s['name']}]: ") or s["name"]
            age = input(f"Age [{s['age']}]: ") or s["age"]
            sclass = input(f"Class [{s['class']}]: ") or s["class"]
            section = input(f"Section [{s['section']}]: ") or s["section"]

            s["name"] = name
            s["age"] = age
            s["class"] = sclass
            s["section"] = section

            updated = True
            break

    if updated:
        write_csv("students.csv",
                  ["student_id", "name", "age", "class", "section"],
                  data)
        print("Student updated successfully!")
    else:
        print("Student ID not found.")


def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter Student ID to delete: ")

    data = read_csv("students.csv")
    new_data = [s for s in data if s["student_id"] != sid]

    if len(new_data) == len(data):
        print("Student ID not found.")
        return

    write_csv("students.csv",
              ["student_id", "name", "age", "class", "section"],
              new_data)

    print("Student deleted successfully!")



def add_marks():
    print("\n--- Add Marks ---")
    sid = input("Student ID: ")
    subject = input("Subject: ")
    marks = input("Marks: ")

    append_csv("marks.csv",
               ["student_id", "subject", "marks"],
               {"student_id": sid, "subject": subject, "marks": marks})

    print("Marks added.")


def view_marks():
    print("\n--- View Marks ---")
    sid = input("Student ID: ")

    data = read_csv("marks.csv")

    found = False
    for m in data:
        if m["student_id"] == sid:
            found = True
            print(f"{m['subject']} : {m['marks']}")

    if not found:
        print("No marks found.")


def mark_attendance():
    print("\n--- Mark Attendance ---")
    sid = input("Student ID: ")
    date = input("Date (YYYY-MM-DD): ")
    status = input("Status (P/A): ").upper()

    append_csv("attendance.csv",
               ["student_id", "date", "status"],
               {"student_id": sid, "date": date, "status": status})

    print("Attendance marked!")


def view_attendance():
    print("\n--- View Attendance ---")
    sid = input("Student ID: ")

    data = read_csv("attendance.csv")

    found = False
    for a in data:
        if a["student_id"] == sid:
            found = True
            print(f"{a['date']} : {a['status']}")

    if not found:
        print("No attendance records found.")


def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        c = input("Choose: ")

        if c == "1": add_student()
        elif c == "2": view_students()
        elif c == "3": search_student()
        elif c == "4": update_student()
        elif c == "5": delete_student()
        elif c == "6": break
        else: print("Invalid choice.")


def marks_menu():
    while True:
        print("\n--- Marks Menu ---")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Back")

        c = input("Choose: ")

        if c == "1": add_marks()
        elif c == "2": view_marks()
        elif c == "3": break
        else: print("Invalid choice.")


def attendance_menu():
    while True:
        print("\n--- Attendance Menu ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back")

        c = input("Choose: ")

        if c == "1": mark_attendance()
        elif c == "2": view_attendance()
        elif c == "3": break
        else: print("Invalid choice.")


def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Student Management")
        print("2. Marks Management")
        print("3. Attendance Management")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1": student_menu()
        elif ch == "2": marks_menu()
        elif ch == "3": attendance_menu()
        elif ch == "4": break
        else: print("Invalid choice.")


main_menu()
