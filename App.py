from utils import Database

Database.CreateBookTable()

USER_CHOICE = "Enter:\n'a' to add a new book\n'l' to list all books\n'r' to mark a book as read\n'd' to delete a book\n'q' to quit\n"

def menu():
    userInput = input(USER_CHOICE)
    while userInput != 'q':
        if userInput == 'a':
            PromptAddBook()
        elif userInput == 'l':
            PromptListBooks()        
        elif userInput == 'r':
            PromptReadBooks()
        elif userInput == 'd':
            PromptDeleteBook()
        else:
            print('Unknown command. Please try again!')
        userInput = input(USER_CHOICE)
def PromptAddBook():
    name = input('Enter the book name: ')
    author = input('Enter the author name: ')
    Database.AddBook(name, author)

def PromptListBooks():
    for book in Database.GetAllBooks():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

def PromptReadBooks():
    name = input('Enter the name of the book you just finished reading: ')
    Database.MarkAsRead(name)

def PromptDeleteBook():
    name = input('Enter the name od the book to delete: ')
    Database.DeleteBook(name)

menu()