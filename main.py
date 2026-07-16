from library import *

load_books()

def save_books():
    with open("books.txt", "w") as file:
        for book in books:
            file.write(f"{book['id']},{book['title']},{book['author']},{book['status']}\n")

def show_menu():
    print("\n----------- Library Management System ------------")
    print("1. Add a new Book")
    print("2. View all Books")
    print("3. Search for a Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Delete a Book")
    print("7. Exit")



# Main Program
while True:
    show_menu()
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_book()
        
    elif choice == 2:
        view_books()
        
    elif choice == 3:
        search_book()
        
    elif choice == 4:
        borrow_book()
        
    elif choice == 5:
        return_book()
        
    elif choice == 6:
        delete_book()
        
    elif choice == 7:
        print("Thank You for using Library Management System.")
        break
    
    else:
        print("Invalid Choice! Please try again.")
