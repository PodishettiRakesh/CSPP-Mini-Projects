import json

def loaddata():
    with open('books.json','r') as file:
        data=json.load(file)
        return data


def viewCollections(collections):
    for book in collections:
        print(book)


def addBook():
    title=input("enter title: ")
    author=input("enter the author name: ")
    year=input("enter the year  book published: ")
    genre=input("enter the genre of your book: ")
    book={}
    book["title"]=title
    book["author"]=author
    book["year"]=year
    book["genre"]=genre
    return book



def savetoJson(book):
    
    with open('books.json','r') as file:
        data=json.load(file)
        data.append(book)

    with open('books.json','w') as file:
        json.dump(data,file,indent=4)



def searchByTitle(data,title):
    for book in data:
        if book["title"]==title:
            return book
    return "No book found with that title"

    

def searchByAuthor(data,author):
    lis=[]
    for book in data:
        if book["author"]==author:
            lis.append(book)
    if lis==[]:

        return "No book found with that title"
    else:
        return lis

    


def removebook(title):
    with open('books.json','r') as file:
        data=json.load(file)
        for book in data:
            if book["title"]==title:
                data.remove(book)   

    with open('books.json','w') as file:
        json.dump(data,file,indent=4)

def sortByTitle(data):
    titles=[]
    for book in data:
        titles.append(book["title"])
    titles.sort()
    for title in titles:
        for books in data:
            if books["title"]==title:
                print(books)

def sortByAuthor(data):
    authors=[]
    for book in data:
        authors.append(book["author"])
    authors.sort()
    
    for author in authors:
        for books in data:
            if books["author"]==author:
                print(books)


def sortByYear(data):
    years=[]
    for book in data:
        years.append(book["year"])
    years.sort()
    for year in years:
        for books in data:
            if books["year"]==year:
                print(books)



def main():
    print("welcome to the book collection ")
    while True:
        data=loaddata()
        print("enter 1 to view book collection:")
        print("enter 2 to add book into collection")
        print("enter 3 to remove book from the collection")
        print("enter 4 to search book by the title")
        print("enter 5 to search book by the author")
        print("enter 6 to view sorted collection by tiitle")
        print("eneter 7 to view sorted collection by author")
        print("enter 8 to view sorted collection by year")
        print("enter 9 to exit from the book collection")
        user_choice=int(input("please enter your choice: "))
        if user_choice==1:
            viewCollections(data)
        elif user_choice==2:
            book=addBook()
            savetoJson(book)
            print("book added succesfully")

        elif user_choice==3:
            title=input("enter the title of book to be removed: ")
            removebook(title)
            print("book removed from collection succesfully")

        elif user_choice==4:
            title=input("enter title to search the book: ")
            print(searchByTitle(data,title))
        elif user_choice==5:
            author=input("enter author of the book to be searc: ")
            print(searchByAuthor(data,author))
        elif user_choice==6:
            sortByTitle(data)
        elif user_choice==7:
            sortByAuthor(data)
        elif user_choice==8:
            sortByYear(data)
        elif user_choice==9:
            return 
        
main()
    







