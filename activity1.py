class library:
         def __init__(self,list_of_book,name):
              self.booklist = list_of_book
              self.name = name
              self.lenddic = {}
         def displayBooks(self):
            print(f"We have the following books in our library{self.name}")
            for books in self.booklist:
              print(books)
         def lendbooks(self,user,book):
              if book not in self.booklist:
                   print("Sorry!WE donot have that book.")
              elif book in self.lenddic:
                   print(f"User {self.name} have already borrowed the book.")
              else:
                   self.lenddic[book] = user
                   print("The book has successfully benn lended by the user,")
         def addBook(self, book):
          self.booksList.append(book)
          print(f"{book} has been added to the book list.")
         def returnBook(self, book):
          if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
          else:
            print("That book wasn't borrowed from us.")
#OUTPUT PART

if __name__ == '__main__':
    books = library([
   'Harry Potter','The tale of two cities','Famous five','Robin Hood',
   'Qudditch through ages','Tales of beedle the bard'
    ], "Let's Upskill")
    user_name = input("Welcome to our library! Please enter your name: ")
while True:
    print(f"\nHello{user_name} Welcome to our {books.name}library please enter a suitable option:")
    print("\n1.Display Books\n2.Lend Books\n3.Add Books\n4.Return Books\n5.Quit")
    user_choice = ("Please enter a Option")
    if user_choice not in ['1','2','3','4','5']:
        print("Please enter a valid option")
        continue
    if user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        print("Please enter the name of book you want to choose:")
        books.lendbooks(user_name,)
    elif user_choice == '3':
        print("Enter the name of book you want to add:")
        books.addBook()
    elif user_choice == '4':
        print("Enter the name of book you want to return:")
        books.returnBook()
    elif user_choice == '5':
        print(f"Thankyou for coming to our library{user_name}!GOODBYE")
        break