class UIInterface:
    def main_menu(self):
        raise NotImplementedError
    
    def get_book_details(self):
        raise NotImplementedError

    def get_book_id(self):
        raise NotImplementedError

    def show_message(self, message):
        raise NotImplementedError    

class ConsoleUI(UIInterface):
    def main_menu(self):
        print('1. Tambah Buku')
        print('2. Pinjam Buku')
        print('3. Kembalikan Buku')
        print('4. Lihat Buku')
        print('5. Keluar')
        