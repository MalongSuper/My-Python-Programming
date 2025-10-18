# Class of multiple instances - OCP (Open Closed Principles)

class Student1:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def save_to_sql(self):
        return f"{self.name} saved to SQL"

    def save_to_csv(self):
        return f"{self.name} saved to CSV"

    def save_to_txt(self):
        return f"{self.name} saved to TXT"


class Student2:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def save(self):
        return f"{self.name} saved"


class SaveSQL(Student2):
    def save(self):
        return f"{self.name} saved to SQL"


class SaveTXT(Student2):
    def save(self):
        return f"{self.name} saved to TXT"


class SaveCSV(Student2):
    def save(self):
        return f"{self.name} saved to CSV"


def main():
    s1 = Student1("John A", "123")
    print(s1.save_to_sql())
    print(s1.save_to_csv())
    print(s1.save_to_txt())

    s2 = [SaveSQL("Martha B", "124"),
          SaveCSV("Martha B", "124"),
          SaveTXT("Martha B", "124")]
    for i in s2:
        print(i.save())


main()
