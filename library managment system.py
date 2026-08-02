#library manage ment system 
class book:
    def __init__(self, book_id, title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.borrowed=False
        
    def display(self):
        status="borowed" if self.is_borrowed else "Available"
        print(f"ID:{self.book_book_id},title:{self.title}, tatus:{status}")
        
class Patron:
    def __init__ (self,patron_id,name):
        self.patron_id=patron_id
        self.name=name
        self.borrowed_book=False
        
    def display(self):
        print(f"patron ID:{self.patron_id}, Name:{self.name}")
        
        print("Borrowed Books:",self.borrowed_books)
        
        
        
class library:
    def __init__ (self):
        self.books={}
        self.patron={}
        
        
    #add a new book
    def add_book(self,book):
        self.books[book.book_id]=book
        print(f"Book'{book.title}' added successfully.")
        
        
    #register of new patron
    def register_patron(self,patron):
        self.patron[patron.patron_id]=patron
        print(f"patron'{patron.name}'register successefully.")
        
        
    #borrow new book
    def borrow_book(self,patron_id,book_id):
        if patron_id not in self.patrons:
            print("patron not found.")
            return
        
        if book_id not in self.books:
            print("Book not found.")
        return
    
    book = self.books[book_id]
    patron = self.patrons[patron_id]
        
    if book.is_borrowed:
            print(f"Book {book.title}'is already borrowed.")
        
    else:
            book.is_borrowed=True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name}borrowed'{book.title}'.")
            
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid  Patron ID or book ID.")
            return
        
        book= self.books[book_id]
        patron = self.patrons[patron_id]
        
        if book.title in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book.title)
            print (f"{patron.name} returned'{book.title}'.")
            
        else:
            print ("this book was not borrowed by the patron.")
            
            
            def display_book(self):
                print ("\nLibrary Book")
                print ("_"*50)
                for book in self.books.values():
                    book.display()
                    print()
                    
                    
library = Library()
while true:
    print ("\n======= Library management System =======")
    print("1.Add Book")
    print("2.Register Patron")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Display book")
    print("6.Display Patron")
    print("7.Exit")
    
    choice = input("Enter your choice:")
    
    if choice =="1":
        book_id=input ("Enter Book ID:")
        title= input ("Enter Book Title : ")
        author=input ("Enter Author Name:")
        library.add_book(Book(book_id,title,author))
        
    elif choice=="2":
        patron_id =input ("enter Patron ID :")
        name=input("enter Patron name:")
        library.register_patron (patron(patron_id,name))
        
    elif choice == "3":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID:")
        library.borrow_book(patron_id, book_id)
        
    elif choice =="4":
        patron_id = input("enter patron ID: ")
        book_id = input("Enter Book ID:")
        library.return_book(patron_id, book_id)
        
    elif choice == "5":
       library.display_books()
       
       
    elif choice == "6":
        library.display_patrons()
    elif choice == "7":
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid Choice. Pleass try again.")