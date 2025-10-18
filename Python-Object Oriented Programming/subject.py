# Class Subject

class Subject:
    __numberOfSubjects = 0
    __totalCredits = 0
    __subjectList = []  # Initial List

    def __init__(self, subject_id="", title="", credit=0):
        self.__subject_id = subject_id
        self.__title = title
        self.__credit = credit
        # Compute credits and number of subjects
        Subject.__totalCredits += credit
        Subject.__numberOfSubjects += 1
        self.__subjectList.append([subject_id, title, credit])
        if len(subject_id) != 6:
            raise ValueError("Requires a Subject ID with valid length to avoid violation")

    @classmethod
    def getNumberOfSubjects(cls):
        return cls.__numberOfSubjects

    @classmethod
    def getTotalCredits(cls):
        return cls.__totalCredits

    @classmethod
    def printAll(cls):
        print("+---------------------------------------------------------------+")
        print("| {:<5} | {:<30} | {:>15} |".format("SUBJECT ID", "SUBJECT TITLE", "CREDIT"))
        print("+---------------------------------------------------------------+")
        for i in range(len(cls.__subjectList)):
            print("| {:<10} | {:<30} | {:>15} |".format(cls.__subjectList[i][0],
                                                  cls.__subjectList[i][1], cls.__subjectList[i][2]))
        print("+---------------------------------------------------------------+")
        print(" Total: {:>8}{:>46}".format(f"{cls.getNumberOfSubjects()}", f"{cls.getTotalCredits()}"))


def main():
    Subject("IT0123", "Introduction to Programming", 2)
    Subject("CSC200", "Java Programming", 3)
    Subject("CSC201", "Data Structures & Algorithms", 3)
    Subject("IT0124", "Database Fundamentals", 3)
    Subject("IT0125", "Network Fundamentals", 2)
    # Print everything
    Subject.printAll()


main()
