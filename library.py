def addbooks():
    #creating library already holding two tupples
    library =[("1984","George Orwell"),("Brave New World", "Aldous Huxley")]
    print("What is the name and the author of the book you would like to add? ")
    #continue to ask for input until the user is done
    while True:
        #getting book information
        new_book = input("Enter 'done' to quit or... \nEnter new bok titile: ")
        #if user enters 'done' as the name of the book the function will print list of all books in the library even if none was entered
        if new_book == "done":
            print(library)
            break
        new_author = input("Enter the name of the author: ")
        #add user's new book to the library as a tupple
        library.append((new_book,new_author))
        #confirmation new book was added
        print(f"{new_book} by: {new_author} added.")
        #in case data needs to be manipulated later
    return library

addbooks()