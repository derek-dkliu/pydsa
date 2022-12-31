from enum import Enum
import random

class AccountType(Enum):
    Basic = 0
    Standard = 1
    Premium = 2

class OnlineReader:
    def __init__(self):
        self.bookmanager = BookManager(self)
        self.usermanager = UserManager(self)
        self.userreader = UserReader(self)
        self.active_user = None

    def login(self, id):
        user = self.usermanager.get_user(id)
        if user is None:
            raise Exception("Invalid user")
        self.active_user = user
        self.show_profile()

    def logout(self):
        self.active_user = None
        print("Logout successfully.")

    def show_home(self):
        print("\nWelcome to Online Book Reader")
        print("1. Login")
        print("2. Manage users")
        print("3. Manage books")
        num = int(input("\nPlease select: "))
        if num == 1:
            id = int(input("Your user ID: "))
            self.login(id)
        elif num == 2:
            self.usermanager.display()
        else:
            self.bookmanager.display()

    def show_profile(self):
        if self.active_user is None:
            self.show_home()
            return
        self.active_user.show_profile()
        print("1. Read my books")
        print("2. Manage my books")
        print("3. Logout")
        num = int(input("\nPlease select: "))
        if num == 1:
            self.read_my_books()
        elif num == 2:
            self.manage_my_books()
        else:
            self.logout()

    def read_my_books(self):
        self.active_user.list_books()
        self.userreader.set_user(self.active_user)
        try:
            id = int(input("\nPlease input the book id: "))
            self.userreader.set_book(self.get_book(id))
        except:
            self.show_profile()

    def manage_my_books(self):
        self.active_user.list_books()
        print("1. Add book")
        print("2. Remove book")
        print("3. Back")
        num = int(input("\nPlease select: "))
        try:
            if num == 1:
                id = int(input("Please input the book id: "))
                self.active_user.add_book(self.get_book(id))
                self.manage_my_books()
            elif num == 2:
                id = int(input("Please input the book id to remove: "))
                self.active_user.remove_user(self.get_book(id))
                self.manage_my_books()
            else:
                self.show_profile()
        except:
            self.show_profile()

    def get_book(self, id):
        book = self.bookmanager.get_book(id)
        if book is None:
            raise Exception(f"Invalid book id {id}")
        return book

class BookManager:
    def __init__(self, reader):
        self.books = {}
        self.reader = reader

    def add_book(self, title):
        id = max(self.books.keys() or [0]) + 1
        if id not in self.books:
            book = Book(id, title)
            self.books[id] = book
            return book
        return None

    def remove_book(self, id):
        if id in self.books:
            del self.books[id]
            return True
        return False

    def get_book(self, id):
        return self.books.get(id, None)

    def update_book(self, id, title):
        book = self.get_book(id)
        if book is None:
            raise Exception(f"Invalid book id {id}")
        book.update(title)

    def list_books(self):
        print(f"\nAll books ({len(self.books)}):")
        print('\n'.join(map(lambda x: f"({x[0]}) {x[1]}", self.books.items()))) 
        print()

    def display(self):
        print("\nBook Manager")
        print("1. List books")
        print("2. Add book")
        print("3. Remove Book")
        print("4. Back")
        num = int(input("\nPlease select: "))
        if num == 1:
            self.list_books()
            self.display()
        elif num == 2:
            title = input("Please input the book title: ")
            self.add_book(title)
            self.display()
        elif num == 3:
            id = int(input("Please input the book id to remove: "))
            self.remove_book(id)
            self.display()
        else:
            self.reader.show_profile()

class UserManager:
    def __init__(self, reader):
        self.users = {}
        self.reader = reader

    def add_user(self, name, account_type):
        id = max(self.users.keys() or [0]) + 1
        if id not in self.users:
            user = User(id, name, account_type)
            self.users[id] = user
            return user
        return None

    def remove_user(self, id):
        if id in self.users:
            del self.users[id]
            return True
        return False

    def get_user(self, id):
        return self.users.get(id, None)

    def list_users(self):
        print(f"\nAll users ({len(self.users)}):")
        print('\n'.join(map(lambda x: f"({x[0]}) {x[1]}", self.users.items()))) 

    def display(self):
        print("\nUser Manager")
        print("1. List users")
        print("2. Add user")
        print("3. Remove user")
        print("4. Back")
        num = int(input("\nPlease select: "))
        if num == 1:
            self.list_users()
            self.display()
        elif num == 2:
            name = input("Please input the user name: ")
            self.add_user(name, AccountType.Basic)
            self.display()
        elif num == 3:
            id = int(input("Please input the user id to remove: "))
            self.remove_user(id)
            self.display()
        else:
            self.reader.show_profile()

class UserReader:
    def __init__(self, reader):
        self.reader = reader
        self.user = None
        self.book = None
        self.pagenum = None
        self.bookmarks = {}

    def set_user(self, user):
        self.user = user
        if user not in self.bookmarks:
            self.bookmarks[user] = {}

    def set_book(self, book):
        if not self.user.has_book(book):
            print(f'You don\'t have book "{book}"')
            self.reader.read_my_books()
            return
        self.book = book
        self.pagenum = self.bookmarks[self.user].get(book, 1)
        while True:
            print(f"Your are reading page {self.pagenum}.")
            action = input("\n(N)ext page or (P)rev page: ").lower()
            if action == 'n':
                self.nextpage()
            elif action == 'p':
                self.prevpage()
            else:
                self.reader.read_my_books()

    def nextpage(self):
        if self.pagenum >= self.book.pages:
            print("You have finished the book.")
            return False
        self.pagenum += 1
        self.bookmarks[self.user][self.book] = self.pagenum
        return True

    def prevpage(self):
        if self.pagenum <= 1:
            print("This is the first page")
            return False
        self.pagenum -= 1
        self.bookmarks[self.user][self.book] = self.pagenum
        return True

class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.pages = random.randint(5, 10)

    def update(self, title):
        self.title = title

    def __str__(self):
        return self.title

class User:
    def __init__(self, id, name, account_type):
        self.id = id
        self.name = name
        self.account_type = account_type
        self.books = set()

    def has_book(self, book):
        return book in self.books

    def add_book(self, book):
        self.books.add(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        if (self.books):
            print(f"\nYour have {len(self.books)} book(s).")
            print('\n'.join(map(lambda x: f"({x.id}) {x.title}", self.books)))
        else:
            print('No books yet.')

    def show_profile(self):
        print(f"\nWelcome {self.name}!")
        print(f"User ID:\t {self.id}")
        print(f"Account type:\t {self.account_type.name}")

    def __str__(self):
        return f"{self.name} ({self.account_type.name})"

reader = OnlineReader()
books = [
    'Harry potter',
    "The lord of the rings",
    "Fullmetal alchemist",
    "Yomi no tsugai",
    "Tao te ching"
]
users = [
    ['Peter', AccountType.Premium],
    ['Anne', AccountType.Basic],
    ['Sue', AccountType.Standard],
    ['Tim', AccountType.Basic],
]
for title in books:
    reader.bookmanager.add_book(title)
for name, type in users:
    reader.usermanager.add_user(name, type)
user = reader.usermanager.get_user(1)
user.add_book(reader.bookmanager.get_book(2))
user.add_book(reader.bookmanager.get_book(3))

reader.show_home()

