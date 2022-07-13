def displayBooks(bookList):
    '''function to display details about available books'''
    print("\n\n----------------------Displaying available books---------------------------------")

    #iterate over books in the list
    for book in bookList:
        #call the display method
        book.display()

