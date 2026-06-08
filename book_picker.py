import json
import random
import customtkinter


def load_library(filepath="library.json"):
    """Load the book library from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_library(library, filepath="library.json"):
    """Save the book library to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=4)


class BookPickerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Book Picker")
        self.geometry("600x700")

        self.library = load_library()

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Title
        self.title_label = customtkinter.CTkLabel(
            self, text="Book Picker", font=("", 24, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Add Book Section
        self.add_frame = customtkinter.CTkFrame(self)
        self.add_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.add_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.title_entry = customtkinter.CTkEntry(
            self.add_frame, placeholder_text="Title"
        )
        self.title_entry.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        self.author_entry = customtkinter.CTkEntry(
            self.add_frame, placeholder_text="Author"
        )
        self.author_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        

        self.add_button = customtkinter.CTkButton(
            self.add_frame, text="Add Book", command=self.add_book
        )
        self.add_button.grid(row=1, column=0, columnspan=3, padx=5, pady=(0, 10))

        # Pick Random Button
        self.pick_button = customtkinter.CTkButton(
            self, text="Pick a Random Book", command=self.pick_random_book,
            font=("", 16, "bold"), height=40
        )
        self.pick_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Result Label
        self.result_label = customtkinter.CTkLabel(
            self, text="", font=("", 16), text_color=("#1f6aa5", "#5dade2")
        )
        self.result_label.grid(row=2, column=0, padx=20, pady=(60, 0))

        # Book Library (Scrollable)
        self.library_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Your Library"
        )
        self.library_frame.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")
        self.library_frame.grid_columnconfigure(0, weight=1)

        self.refresh_library()

    def refresh_library(self):
        """Clear and re-render the book list."""
        for widget in self.library_frame.winfo_children():
            widget.destroy()

        if not self.library:
            empty_label = customtkinter.CTkLabel(
                self.library_frame, text="No books yet. Add some above!"
            )
            empty_label.grid(row=0, column=0, padx=10, pady=10)
            return

        for i, book in enumerate(self.library):
            book_text = f"\"{ book['title']}\" by {book['author']} ]"

            book_label = customtkinter.CTkLabel(
                self.library_frame, text=book_text, anchor="w"
            )
            book_label.grid(row=i, column=0, padx=10, pady=2, sticky="w")

            remove_button = customtkinter.CTkButton(
                self.library_frame, text="Remove", width=70,
                fg_color="transparent", border_width=1,
                command=lambda idx=i: self.remove_book(idx)
            )
            remove_button.grid(row=i, column=1, padx=5, pady=2)

    def add_book(self):
        """Add a new book from the entry fields."""
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        

        if not title or not author or not genre:
            self.result_label.configure(text="Please fill in all fields.")
            return

        book = {"title": title, "author": author}
        self.library.append(book)
        save_library(self.library)

        # Clear entries
        self.title_entry.delete(0, "end")
        self.author_entry.delete(0, "end")
        

        self.result_label.configure(text=f"Added \"{title}\"!")
        self.refresh_library()

    def remove_book(self, index):
        """Remove a book by its index."""
        removed = self.library.pop(index)
        save_library(self.library)
        self.result_label.configure(text=f"Removed \"{removed['title']}\"")
        self.refresh_library()

    def pick_random_book(self):
        """Pick a random book from the library."""
        if not self.library:
            self.result_label.configure(text="Library is empty! Add some books first.")
            return

        book = random.choice(self.library)
        self.result_label.configure(
            text=f"Read this: \"{book['title']}\" by {book['author']}"
        )


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    app = BookPickerApp()
    app.mainloop()