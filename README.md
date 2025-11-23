# 📚 Simple Library Management System (Python)

A basic command-line application built in Python that simulates core library functions: adding books, displaying the list of available books, lending books, and returning books. This project uses **Object-Oriented Programming (OOP)** principles with `Book` and `Library` classes.

## ✨ Features

* **Add Book:** Incorporate new books into the library's collection.
* **Display Books:** View the current list of all books in the library and their status (available/not available).
* **Lend Book:** Change a book's status to borrowed/not available.
* **Return Book:** Change a book's status back to available.
* **Simple CLI:** Interactive command-line interface for easy operation.

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3** installed on your system.

### Installation

1.  **Save the Code:** Save the provided code into a file named `library_app.py`.

2.  **Run the Application:** Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:

    ```bash
    python library_app.py
    ```

---

## 🛠 Usage

Once the application is running, you will be greeted by the main menu. Follow the on-screen instructions to interact with the library system.

### Example Workflow

1.  **Add a Book (Choice 2):**
    ```
    Enter your choice (1-5): 2
    Enter the Title of your book: The Hobbit
    Enter the author of yout book: J.R.R. Tolkien
    The Hobbit added to the library
    ```

2.  **Display Books (Choice 1):**
    ```
    Enter your choice (1-5): 1
    List of Books
    The Hobbit written by J.R.R. Tolkien
    ```

3.  **Borrow a Book (Choice 3):**
    ```
    Enter your choice (1-5): 3
    Enter the Title of your book: The Hobbit
    You have borrowed The Hobbit
    ```

---

## 💻 Code Structure

The application is structured into two main classes and a driver function.

### `Book` Class

Represents a single book with the following attributes:
* `title`
* `author`
* `available` (Boolean: `True` if available, `False` if borrowed)

### `Library` Class

Manages the collection of `Book` objects and provides the core functionality:
* `add_book(book)`: Adds a new `Book` instance to the internal list.
* `lend_book(title)`: Marks a book as not available if it's found and currently available.
* `return_book(title)`: Marks a book as available if it's found and currently borrowed.
* `display_books()`: Prints the details of all books.

### `run_library()` Function

This is the main loop that provides the interactive **Command-Line Interface (CLI)**, handles user input, and calls the appropriate methods on the `Library` object.

---

## ⚠️ Known Issues

* **Error in Logic:** The `lend_book` and `return_book` methods have a logical issue where they **return immediately** after checking the status of the *first book* in the list, rather than continuing the loop to find the correct book. This needs to be corrected for proper functionality.
* **Case Sensitivity:** Book searching is currently case-insensitive (`.lower()`) but should be robustly implemented to handle edge cases.

---

## 🤝 Contributing

This is a simple project, but feel free to fork the repository and submit pull requests with improvements, especially fixing the **Known Issues**!

---
