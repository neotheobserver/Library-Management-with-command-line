def writeLines(bookList):
    '''function to write current list of books to file'''
    #display message for user
    print("\n\n----------------------------Closing database---------------------------------------")
    
    #open the file to write
    file = open("lms.txt", "w")
    
    #iterate over current list of books
    for book in bookList:
        #call to writeToFile method of book class
        book.writeToFile(file)
        
    #close the file
    file.close()
