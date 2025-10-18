# Class Abstract Document
from abc import ABC, abstractmethod
from datetime import datetime


class Document(ABC):
    def __init__(self, fileName="Document1",
                 createdDate=datetime.today().strftime('%Y-%m-%d'), lastModifiedDate=None):
        self.__filename = fileName
        self.__createddate = createdDate
        self.__lastmoddate = lastModifiedDate
        self.__content = ""

    @property
    def Content(self):
        return self.__content

    @Content.setter
    def Content(self, input_content):
        self.__content = input_content

    @property
    def fileName(self):
        return self.__filename

    @fileName.setter
    def fileName(self, filename):
        self.__filename = filename

    @property
    def CreateDate(self):
        return self.__createddate

    @CreateDate.setter
    def CreateDate(self, date):
        self.__createddate = date

    @property
    def LastModDate(self):
        return self.__lastmoddate

    @LastModDate.setter
    def LastModDate(self, date):
        self.__lastmoddate = date

    @abstractmethod
    def inputContent(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def saveAs(self, name):
        pass

    @abstractmethod
    def open(self):
        pass


class TextPad(Document):
    def __init__(self):
        super().__init__(fileName="NoName")
        self.__words = 0
        self.__size = 0

    def getWords(self):
        return len(self.Content.split())

    def getSize(self):
        return len(self.Content.replace(" ", ""))

    def inputContent(self):
        self.Content = input("Enter Content: ")

    def save(self):
        word = self.getWords()
        size = self.getSize()
        lastmoddate = datetime.today().strftime('%Y-%m-%d')
        test_file = open(f"{self.fileName}.txt", "w")
        line = [f"{self.Content} \n",
                f"Date Created: {self.CreateDate} \n",
                f"Data Modified: {lastmoddate} \n",
                f"Words: {word} \n",
                f"Size: {size} \n"]
        test_file.writelines(line)
        return f"{self.fileName}.txt"

    def saveAs(self, new_name):
        self.fileName = new_name
        word = self.getWords()
        size = self.getSize()
        lastmoddate = datetime.today().strftime('%Y-%m-%d')
        test_file = open(f"{new_name}.txt", "w")
        line = [f"{self.Content} \n",
                f"Date Created: {self.CreateDate} \n",
                f"Data Modified: {lastmoddate} \n",
                f"Words: {word} \n",
                f"Size: {size} \n"]
        test_file.writelines(line)
        return f"{new_name}.txt"

    def open(self):
        # Read Files
        test_file = open(f"{self.fileName}.txt", "r")
        print(f"{self.fileName}.txt")
        print(test_file.read())


def main():
    document = None  # Store initial document
    print(" [1]. New TextPad\n "
          "[2]. Input TextPad\n "
          "[3]. Save TextPad\n "
          "[4]. Save as TextPad\n "
          "[5]. Open TextPad\n "
          "[6]. Exit")
    while True:
        try:
            user = int(input("Select function number [1-6]: "))
            if user == 6:
                print("Exit the program")
                break
            elif user == 1:
                print("New Textpad created!!")
                document = TextPad()
                print()
            elif user == 2:
                document.inputContent()
                print()
            elif user == 3:
                print("Saved:", document.save())
                print()
            elif user == 4:
                name = input("Save as: ")
                print("Saved as:", document.saveAs(name))
            elif user == 5:
                document.open()
            else:
                print("Exit the program")
                break
        except AttributeError:
            print("No document exists\n")


main()
