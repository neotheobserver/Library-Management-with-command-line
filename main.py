#import pre-defined library
import sys
import time

#import function definition for burrowing
from burrowBook import burrowBooks
#import function definition for returning
from returnBook import returnBooks
#import function to read file and make list of books    
from makeList import makeBookList
#import function to read list and write to file
from writeLine import writeLines
#import function to display books
from display import displayBooks

        
def main():
    #open the file to read
    while True:
        try:
            file = open("lms.txt", "r")
            break
        except:
            print("A file named lms.txt with detail of books seperated by commas i.e. title,author,quantity,price is required for the program to run")
            for i in range(3, 0, -1):
                print("Closing program in ",i,"seconds.")
                time.sleep(1)
            sys.exit(0)

    #after file is opened read each lines and store as list of string        
    lines = file.readlines()

    #call makeBookList function that return list of books
    bookList = makeBookList(lines)
    
    #close the file
    file.close()
  
    #run loop until user wants to exit
    while True:
    
        #display all the books in the list
        displayBooks(bookList)

        #get user input for task to perform
        while True:
            #try to get integer value
            try:
                ask_user = int(input("Enter 1 to borrow a book\nEnter 2 to return a book\nEnter 0 to exit the program\nYour input: "))
                break
            #error message if not integer
            except:
                print("Enter integer value only")

        #if the value is integer but not 0,1, or 2                
        if ask_user != 0 and ask_user != 1 and ask_user != 2:
            print("Invalid Input...Please enter 0 to exit 1 to burrow and 2 to return")

        #if user wants to exit	
        if ask_user == 0:
            #call writeLines function
            writeLines(bookList)
            #exit out of program
            sys.exit(0)

        #if user wants to burrow	
        if ask_user == 1:
            #ask for burrower name
            name = input("Enter your name: ")

            #get user input for number of books to add
            while True:
                #try to get integer value
                try:
                    quantity = int(input("No of books to borrow: "))
                    if (quantity < 1):
                        print("Enter a positive value")
                        continue
                    break
                #error message if not integer
                except:
                    print("Enter integer value")

            #list to store all the books user wants to burrow                     
            titles = []
            for i in range(1, quantity+1):
                #get the title of book to burrow until correct tile entered
                exists = True
                while exists:
                    title = input("Enter the title of the book "+str(i)+": ")
                    count = 0
                    #if the entered title exist in the list of the books
                    for book in bookList:
                        #increase count for final case
                        count += 1

                        #check if book found in list
                        if title == book.title:
                            #if found break out of both loops
                            exists = False
                            break
                        
                        #if end of list without finding book print message
                        if count == len(bookList):
                            print("Sorry, We do not have this book at this time.")
                #add to list
                titles.append(title)
                                          
            #call burrowBooks method with perons name, books to burrow, and current list of books                      
            bookList = burrowBooks(name, titles, bookList)

        #if user wants to return
        if ask_user == 2:
            #ask for returner name
            name = input("Enter your name: ")

            #get user input for number of books to return
            while True:
                #try to get integer value
                try:
                    quantity = int(input("No of books to return: "))
                    if (quantity < 1):
                        print("Enter a positive value")
                        continue
                    break
                #error message if not integer
                except:
                    print("Enter integer value")

            #list to store all the books user wants to return                      
            titles = []
            for i in range(1, quantity+1):
                #get the title of book to return until correct tile entered
                exists = True
                while exists:
                    title = input("Enter the title of the book "+str(i)+": ")
                    count = 0
                    
                    #if the entered title exist in the list of the books
                    for book in bookList:
                        count += 1
                        if title == book.title:
                            exists = False
                            break
                        if count == len(bookList):
                            print("The book was not found in the list...you are probably in the wrong library")

                #add the title to the list
                titles.append(title)

            #call returnBooks method with person name, book to return, and current list of books
            bookList = returnBooks(name, titles, bookList)


if __name__ == "__main__":
    main()
