from .database import Database
from .models import Book 

class LibraryManager:
    def __init__(self, ui):
        self.database = Database()
        self.ui = ui 

    def start(self):
        while True:
            choice = self.ui.main_menu()
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.check_out_book()
            elif choice == 3:
                self.return_book()
            elif choice == 4:
                self.view_books()
            elif choice == 5:
                break

    def add_book(self):
        title, author, year = self.ui.get_book_details()
        book = Book(title, author, year)
        self.database.execute(
            'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',
            (book.title, book.author, book.year)
        )
        self.ui.show.message(f'Buku {book.title} berhasil ditambahkan.')

    def check_out_book(self):
        book_id = self.ui.get_look_id()
        book_data = self.database.fetch_all('SELECT * FROM books WHERE id=?', (book_id,))
        if book_data:
            is_checked_out = bool(book_data[0][4])
            book = Book(book_data[0][1], book_data[0][2], book_data[0][3], book_id)
            book._Book_is_checked_out = is_checked_out
            try:
                book.check_out()
                self.database.execute(
                    'UPDATE books SET is_checked_out=1 WHERE id=?', (book_id,)
                )
                self.ui.show_message(f"Buku '{book.title}' berhasil dipinjam.")
                except Exception as e:
                    self.ui.show_message(str(e))
                else: 
                    self.ui.show_message('Buku tidak ditemukan')

    def return_book(self):
         book_id = self.ui.get_look_id()
        book_data = self.database.fetch_all('SELECT * FROM books WHERE id=?', (book_id,))
        if book_data:
            is_checked_out = bool(book_data[0][4])
            book = Book(book_data[0][1], book_data[0][2], book_data[0][3], book_id)
            book._Book_is_checked_out = is_checked_out
            try:
                book.check_out()
                self.database.execute(
                    'UPDATE books SET is_checked_out=1 WHERE id=?', (book_id,)
                )
                self.ui.show_message(f"Buku '{book.title}' berhasil dipinjam.")
                except Exception as e:
                    self.ui.show_message(str(e))
                else: 
                    self.ui.show_message('Buku tidak ditemukan.')
    
    def view_books(self):
        books = self.database.fetch_all('SELECT * FORM books')
        if books:
            for book in books:
                checked_out_status = "Dipinjam" if book[4] == 1 else "Tersedia"
                self.ui.show_message(f'ID: {book[0]}, Judul: {book[1]}, Penulis: {book[2]}, Tahun:{[3]}, Status: {checked_out_status}')
                else: 
                    self.ui.show_message('Tidak ada buku di perpustakaan')