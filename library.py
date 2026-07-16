books = []

def add_book():
    book_id = int(input(("Enter Book ID: ")))
    title = input("Enter Book name: ")
    author = input("Enter Author's name: ")
    
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    })
    
    with open("books.txt", "a") as file:
        file.write(f"{book_id},{title},{author},Available\n")
    
    print("Book added successfully!")


def view_books():
    if len(books) == 0:
        print("\n No books available in the library.")
        return
    
    print("\n---------- BOOK LIST ---------")
    print("ID \t Tittle \t\t Author \t\t\t Status")
    print("---------------------------------------------------------------")
    
    for book in books:
        print(f"{book['ID']} \t {book['Title']} \t\t {book['Author']} \t\t\t {book['Status']}")


def search_book():
    title = input("Enter Book name: ")
    
    for book in books:
        if book["title"].lower() == title.lower():
            print("Book is available in the library.")
            return
        
    print("Book is not available in the Library.")


def borrow_book():
    book_id = int(input("Enter book id: "))
    
    for book in books:
        if book["id"] ==  book_id:
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
                return
            
        print("Book not Found")


def return_book():
    book_id = int(input("Enter Book ID: "))
    
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                print("Book returned successfully.")
            else:
                print("Book is already available.")
                return
            
    print("Book not Found.")


def delete_book():
    if len(books) == 0:
        print("\nNo books available to delete.")
        return
    
    book_id = int(input("Enter Book ID to delete: "))
    
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return
        
    print("Book not found.")


def load_books():
    try:
        with open("books.txt", "r") as file:
            for linne in file:
                data = line.strip().split(",")
                
                books.append({
                    "id": int(data[0]),
                    "title": data[0],
                    "author": data[2],
                    "status": data[3]
                })
    
    except FileNotFoundError:
        pass