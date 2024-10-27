from datetime import datetime 
import json

class Borrower:
    def __init__(self, name, email,number, id):
        self.name=name
        self.email=email
        self.number=number
        self.bookid=id
        current_datetime = datetime.now()
        self.curdate= current_datetime.strftime("%Y-%m-%d")
    def detaillog(self):
        # user_log={"Name:" :{self.name} ,"ID:":{self.bookid}, "Date of borrow:":{self.curdate},  "Email:": {self.email}}
        with  open("borrowerlog.txt", "a") as f:
            f.write(f"Name:{self.name} ,ID:{self.bookid}, Date of borrow:{self.curdate},  Email: {self.email} , Status:\n")
            




def browse():
    with  open('Books\\mybookcollection.txt', 'r') as f:
        for each in f:
            print(each.strip())
def borrow():
    n=input("Enter your name:")
    e=input("Enter your email:")
    num=input("Enter your number:")
    bid=input("Enter the id of your book you wish to borrow:")
    user=Borrower(n,e,num,bid)
    user.detaillog()
    print("You have borrowed the book successfully")
def returning():
    current_user = input("Enter your name: ")
    current_book = input("Enter book ID of the book you wish to return: ")
    current_day=datetime.now()
    current_day=current_day.strftime("%Y-%m-%d")
    # Read the lines from the log file
    with open("borrowerlog.txt", "r") as f:
        lines = f.readlines()

    # Check if the specified user and book exist in the log
    book_found = False
    for line in lines:
        if current_user in line and current_book in line:
            book_found = True
            myuser=line
            break  # Exit the loop since we found the book

    if not book_found:
        print(f"No record found for {current_user} returning book {current_book}.")
        return

    # Write back to the log file excluding the entry for the returned book
    with open('borrowerlog.txt', 'w') as file:
        for line in lines:
            if not (current_user in line and current_book in line):  # Skip the line with the current user and book
                file.write(line)
    with open('borrowerlog.txt', 'a') as file:
        file.write(f"{myuser}  Status:Returned on {current_day}\n")

    print(f"Book {current_book} returned successfully.")

def discovering():
    print("Enter the genre you would like to discover:\n1.Fantasy\n2.Historical\n3.Mystery Thriler\n4.Non Ficition\n5.Science Fiction")
    user_genre=int(input("Enter the genre you would like to discover"))
    
    if user_genre==1:
        with open("Books'\\'fantasy_books.txt",'r') as b:
            for each in b:
                print(each.strip())
    elif user_genre==2:
        with open("Books\\historical_fiction_books.txt",'r') as b:
            for each in b:
                print(each.strip())
    elif user_genre==3:
        with open("Books\\mystery_thriller_books.txt",'r') as b:
            for each in b:
                print(each.strip())
    elif user_genre==4:
        with open("Books'\\'non_fiction_books.txt",'r') as b:
            for each in b:
                print(each.strip())
    elif user_genre==5:
        with open("Books\\science_fiction_books.txt",'r') as b:
            for each in b:
                print(each.strip())
    else:
        print("Invalid choice")
def suggestion():
    new_book=input("Enter the books name")
    new_genre=input("Enter the genre of the book")
    new_auth=input("Enter author of book's name")
    new_id={"book":new_book,"genre":new_genre,"author":new_auth}
    with open("suggestion.txt", "a") as file:
        file.write(json.dumps(new_id))
def showing():
    with open("suggestion.txt", "r") as file:
        for line in file:
            print(line.strip())

def menuopt(opt):
    if opt==1:
        browse()
    elif opt==2:
        borrow()
    elif opt==3:
        returning()
    elif opt==4:
        discovering()
    elif opt==5:
        suggestion()
    elif opt==6:
        showing()
    else:
        print("What do you want to do today?")
    









print("Welcome to Goldberg's Library")
print("What would you like to do today? \n1.Browse our collections\n2.Borrow a book\n3.Return a book\n4.Discover new and upcoming books\n5.Suggest a book for us to add to our collection\n6.Soon to be added books")
user_input=int(input())
menuopt(user_input)


