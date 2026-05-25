
# DATA STRUCTURE
print("---------------------Data structure----------------------")
#
#   books = [
#       {"book_name": "Python Basics",  "book_qty": 10},
#       {"book_name": "Clean Code",     "book_qty": 5},
#       {"book_name": "The Pragmatic",  "book_qty": 8},
#   ]
#
#   - books        --> the main LIST (holds all books)
#   - books[0]     --> the FIRST book (a dictionary)
#   - books[1]     --> the SECOND book (a dictionary)
#
#   - books[0]["book_name"]  --> "Python Basics"
#   - books[0]["book_qty"]   --> 10
#
#   Think of it like a TABLE:
#   +-----------------+----------+
#   | book_name       | book_qty |
#   +-----------------+----------+
#   | Python Basics   |    10    |
#   | Clean Code      |     5    |
#   | The Pragmatic   |     8    |
#   +-----------------+----------+
#
# ============================================================
# OPERATIONS
# ============================================================
#   1. create_book(name, qty)   --> Add a new book
#   2. list_books()             --> Display all books
#   3. sell_book(name, qty)     --> Sell copies of a book
#   4. add_book_qty(name, qty)  --> Restock an existing book
# ============================================================


# ============================================================
# MAIN DATA STORE
# ============================================================
# This is our "database" — an empty list to start.
# Every book we add will be a dictionary inside this list.
# ============================================================
#Example:
#   find_book("Clean Code")
#   --> {"book_name": "Clean Code", "book_qty": 5}
#
#   find_book("Unknown Book")
#   --> None

# ============================================================
# HELPER: find_book(name)
# DATA STRUCTURE
print("---------------------Data structure----------------------")

# ============================================================
# MAIN DATA STORE
# ============================================================
# This is our "database" — an empty list to start.
# Every book we add will be a dictionary inside this list.
# ============================================================
books = []  # Global list to store all books

# ============================================================
# HELPER: find_book(name)
# ============================================================
def find_book(name):
    """Find a book by name (case-insensitive)"""
    for book in books:
        if book["book_name"].lower() == name.lower():
            return book
    return None

# ============================================================
# OPERATION 1: CREATE BOOK
# ============================================================
def create_book(name, qty):
    """Add a new book to inventory"""
    # Step 1 — Check if already exists
    if find_book(name):
        print(f"Error: '{name}' already exists!")
        return

    # Step 2 — Validate quantity
    if qty <= 0:
        print("Error: Quantity must be greater than 0!")
        return

    # Step 3 & 4 — Create and append
    new_book = {"book_name": name, "book_qty": qty}
    books.append(new_book)

    # Step 5 — Success message
    print(f"\n  Book Added Successfully!")
    print(f"  Name     : {name}")
    print(f"  Quantity : {qty}")

# ============================================================
# OPERATION 2: LIST BOOKS
# ============================================================
def list_books():
    """Display all books in inventory"""
    # Step 1 — Check if empty
    if not books:
        print("\n  No books in inventory yet!")
        return

    # Step 2 — Print table header
    print(f"\n  {'-' * 47}")
    print(f"  {'#':<5} {'Book Name':<30} {'Qty':>5}")
    print(f"  {'-' * 47}")

    # Step 3 — Loop with enumerate
    total_stock = 0
    for index, book in enumerate(books, start=1):
        print(f"  {index:<5} {book['book_name']:<30} {book['book_qty']:>5}")
        total_stock += book["book_qty"]

    # Step 4 — Totals
    print(f"  {'-' * 47}")
    print(f"  Total books: {len(books)}  |  Total stock: {total_stock}")
    print(f"  {'-' * 47}")

# ============================================================
# OPERATION 3: SELL BOOK
# ============================================================
def sell_book(name, qty):
    """Sell copies of a book"""
    # Step 1 — Find the book
    book = find_book(name)
    if not book:
        print(f"\n  Error: '{name}' not found!")
        return

    # Step 2 — Validate quantity
    if qty <= 0:
        print("  Error: Quantity must be greater than 0!")
        return

    # Step 3 — Check stock
    if book["book_qty"] < qty:
        print(f"\n  Error: Not enough stock!")
        print(f"  Available : {book['book_qty']}")
        print(f"  Requested : {qty}")
        return

    # Step 4 — Deduct stock
    book["book_qty"] -= qty

    # Step 5 — Confirmation
    print(f"\n  Sold {qty} copies of '{name}'.")
    print(f"  Remaining stock: {book['book_qty']}")

# ============================================================
# OPERATION 4: ADD BOOK QUANTITY (RESTOCK)
# ============================================================
def add_book_qty(name, qty):
    """Restock an existing book"""
    # Step 1 — Find the book
    book = find_book(name)
    if not book:
        print(f"\n  Error: '{name}' not found!")
        print(f"  Tip: Use 'Create Book' to add it first.")
        return

    # Step 2 — Validate quantity
    if qty <= 0:
        print("  Error: Quantity must be greater than 0!")
        return

    # Step 3 — Add stock
    book["book_qty"] += qty

    # Step 4 — Confirmation
    print(f"\n  Restocked '{name}' by {qty}.")
    print(f"  New total: {book['book_qty']}")

# ============================================================
# MENU SYSTEM
# ============================================================
def menu():
    """Display the main menu and handle user input"""
    while True:
        print(f"\n  {'=' * 40}")
        print(f"        BOOK INVENTORY SYSTEM")
        print(f"  {'=' * 40}")
        print(f"  1. Add New Book")
        print(f"  2. List All Books")
        print(f"  3. Sell a Book")
        print(f"  4. Restock a Book")
        print(f"  5. Exit")
        print(f"  {'=' * 40}")

        choice = input("  Choose (1-5): ").strip()

        if choice == "1":
            name = input("\n  Book name : ").strip()
            try:
                qty = int(input("  Quantity  : "))
                create_book(name, qty)
            except ValueError:
                print("  Error: Please enter a valid number!")

        elif choice == "2":
            list_books()

        elif choice == "3":
            name = input("\n  Book name : ").strip()
            try:
                qty = int(input("  Qty to sell: "))
                sell_book(name, qty)
            except ValueError:
                print("  Error: Please enter a valid number!")

        elif choice == "4":
            name = input("\n  Book name : ").strip()
            try:
                qty = int(input("  Qty to add: "))
                add_book_qty(name, qty)
            except ValueError:
                print("  Error: Please enter a valid number!")

        elif choice == "5":
            print("\n  Goodbye! 👋")
            break

        else:
            print("\n  Invalid choice! Please enter 1–5.")

# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
if __name__ == "__main__":
    menu()