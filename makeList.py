#import book class
from book import Book

def makeBookList(lines):
    '''read list of lines of string and return list of books'''
    #display message for user
    print("\n\n----------------------------Reading database---------------------------------------")
    
    #initialize an empty string
    bookList = []

    #iterate over each line
    for line in lines:
        #split the string into list
        items = line.split(",")
        
        #create instance of book
        bookInstance = Book(items[0], items[1], items[2], items[3])
        
        #add the book to bookList
        bookList.append(bookInstance)

    #return the list of books
    return bookList
