# Book App in Object-Oriented Programming


class Book:
    __book_id = 10
    __book_data = []

    def __init__(self, Title="Unknown", Author="Unknown",
                 Published_Year="Unknown", Genre="Unknown", Available_Copies=0):
        self.__book_id = str(Book.__book_id).zfill(6)
        Book.__book_id += 1
        self.__Title = Title
        self.__Author = Author
        self.__Published_Year = Published_Year
        self.__Genre = Genre
        self.__Available_Copies = int(Available_Copies)
        self.__book_data.append([self.__book_id, Title, Author, Published_Year, Genre, Available_Copies])

    def __str__(self):
        return (f"Book ID: {self.__book_id}, Title: {self.__Title}, Author: {self.__Author}, "
                f"Published Year: {self.__Published_Year}, Genre: {self.__Genre}, "
                f"Available Copies: {self.__Available_Copies}")

    @classmethod
    def getInfo(cls):
        print("{:<8} {:<25} {:<20} {:<15} {:<35} {:<17}".format("ID", "Title", "Author", "Published Year",
                                                                "Genre", "Available Copies"))
        print("-----------------------------------------------------------------------------"
              "-------------------------------------------------")
        for book in cls.__book_data:
            print("{:<8} {:<25} {:<20} {:<15} {:<35} {:<17}".format(book[0], book[1],
                                                                    book[2], book[3], book[4], book[5]))

    @classmethod
    def insert(cls, Title="Unknown", Author="Unknown",
               Published_Year="Unknown", Genre="Unknown", Available_Copies=0):
        Book(Title, Author, Published_Year, Genre, Available_Copies)

    @classmethod
    def delete(cls, book_id):
        # Ensure it matches stored ID format
        book_id = str(book_id).zfill(6)
        for i, book in enumerate(cls.__book_data):
            if book[0] == book_id:  # Delete the book with match ID
                del cls.__book_data[i]
                print(f"Book with ID {book_id} has been deleted.")
                return
        print(f"No book found with ID {book_id}.")

    # Find the book based on given information
    # Use **kwargs instead of **arg to accept parameter
    @classmethod
    def search(cls, **kwargs):
        if not kwargs:
            print("Search parameter is empty")
            return

        print("{:<8} {:<25} {:<20} {:<15} {:<35} {:<17}".format(
            "ID", "Title", "Author", "Published Year", "Genre", "Available Copies"
        ))
        # Or just print("-" * 120)
        print("-----------------------------------------------------------------------------"
              "-------------------------------------------------")
        found = False
        for book in cls.__book_data:  # Use this instead of range(len(cls.__book_data))
            match = True
            for key, value in kwargs.items():  # Retrieve Book.search(Key='Value')
                # lower() for easy searching, avoid cases when
                # there are upper and lower at the same time
                if key == 'ID' and str(value) != str(book[0]):
                    match = False
                elif key == 'Title' and value.lower() != str(book[1]).lower():
                    match = False
                elif key == 'Author' and value.lower() != str(book[2]).lower():
                    match = False
                elif key == 'Published_Year' and str(value) != str(book[3]):
                    match = False
                elif key == 'Genre' and value.lower() != str(book[4]).lower():
                    match = False
            if match:
                found = True
                print("{:<8} {:<25} {:<20} {:<15} {:<35} {:<17}".format(book[0], book[1],
                                                                        book[2], book[3], book[4], book[5]))

        if not found:
            print("No books found with the given search parameters.")


def main():
    books_data = [
        ('The_Great_Gatsby', 'F_Scott_Fitzgerald', '19250410', 'Tragedy', 10000),
        ('ULYSSES', 'James_Joyce', '19220202', 'Modernist_Novel', 10000),
        ('Lolita', 'Vladimir_Nabokov', '19552001', 'Novel', 10000),
        ('Brave_New_World', 'Aldous_Huxley', '19320505', 'Science_Fiction_Dystopian_Fiction', 10000),
        ('The_Sound_And_The_Fury', 'William_Faulkner', '19290103', 'Southern_Gothic', 10000),
        ('Catch22', 'Joseph_Heller', '19611010', 'Dark_Comedy', 10000),
        ('The_Grapes_Of_Wrath', 'John_Steinbeck', '19391404', 'Novel', 10000),
        ('I_Claudius', 'Robert_Graves', '19340810', 'Historical', 10000),
        ('To_The_Lighthouse', 'Virginia_Woolf', '19270505', 'Modernism', 10000),
        ('Slaughterhouse_Five', 'Kurt_Vonnegut', '19693103', 'War_Novel', 10000),
        ('Invisible_Man', 'Ralph_Ellison', '19521404', 'African_American_Literature', 10000),
        ('Native_Son', 'Richard_Wright', '19400103', 'Social_Protest', 10000),
        ('USA_Trilogy', 'John_Dos_Passos', '19300405', 'Political_Fiction', 10000),
        ('A_Passage_To_India', 'E_M_Forster', '19240406', 'Novel', 10000),
        ('Tender_Is_The_Night', 'F_Scott_Fitzgerald', '19341204', 'Tragedy', 10000),
        ('Animal_Farm', 'George_Orwell', '19451708', 'Political_Satire', 10000),
        ('The_Golden_Bowl', 'Henry_James', '19041011', 'Philosophy', 10000),
        ('A_Handful_Of_Dust', 'Evelyn_Waugh', '19340603', 'Fiction', 10000),
        ('As_I_Lay_Dying', 'William_Faulkner', '19300302', 'Black_Comedy', 10000),
        ('The_Heart_Of_The_Matter', 'Graham_Greene', '19480302', 'Novel', 10000)
    ]

    for Title, Author, Published_Year, Genre, Available_Copies in books_data:
        Book(Title, Author, Published_Year, Genre, Available_Copies)

    # Insert Book
    Book.insert("Dune", "Frank_Herbert", "19650601",
                "Science_Fiction", 5000)
    Book.getInfo()
    # Search Book
    print()
    Book.search(Genre="Novel")


if __name__ == "__main__":
    main()
