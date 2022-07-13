#import library to get date and time
from datetime import datetime

def returnBooks(name, titles, bookList):
    '''function to return a book'''
    print("\n\n------------------------Generating notes for books returned-----------------------")

    #set initial fine to 0
    totalFine = 0

    #create/open file for the person who wants to return
    returnBook = open(name+" returned on "+datetime.now().strftime("%m_%d_%Y, %H_%M_%S")+".txt", "w")

    #write to file the name of returner and time of return
    returnBook.write("The books returned by "+name+" on "+datetime.now().strftime("%m/%d/%Y, %H:%M")+":\n")

    #display similar information to the user
    print(name, "returned the following books:")

    #iterate over the titles to return
    for title in titles:

        #iterate over the list of books looking for the title
        for book in bookList:

            #if title is found
            if title == book.title:
                #get the quantity and convert to int
                quantity = int(book.quantity)

                #write the tile to file and display to user
                returnBook.write(title+"\n")
                print(title)

                print("----------")

                #get the no of lending days
                while True:
                    #try to get integer value
                    try:
                        days = int(input("No of Days the book was burrowed: "))
                        break
                    #error message if not integer
                    except:
                        print("Enter integer value")

                print("----------")
                                    
                #calculate the fine amount
                if days > 10:
                    #Rs 2 fine for each late day
                    totalFine += (days-10)*2
                                    
                #call the returnBook() method of book class to increase the quantity of book
                book.returnBook()

                #exit out of loop after returning current book
                break;

                
    #display info to user
    print("Time of return is: "+datetime.now().strftime("%m/%d/%Y, %H:%M"))                       

    #write total price to file and display to user
    if totalFine == 0:
        returnBook.write("The books were returned on time\n\n")
        print("The books were returned on time")
    else:
        returnBook.write("The total fine is: Rs."+str(totalFine)+"\n\n")
        print("The total fine is: Rs."+str(totalFine))

    #close the return file
    returnBook.close()
    
    #return the current list of books
    return bookList
