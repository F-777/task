class Book:
    def __init__(self, title, author, year, book_id=None):
        self.__id = book_id
        self.__title = title 
        self.__author = author
        self.__year = year 
        self.__is_checked_out = False

        # Getter untuk aksesbilitas properti 
        @property
        def id(self):
            return self.id
        
        @property
        def title(self):
            return self.title
        
        @property
        def author(self):
            return self.author

        @property
        def year(self):
            return self.year
        
        @property
        def is_checked_out(self):
            return self.__is_checked_out
        
        def check_out(self):
          if not self.__is_checked_out:
            self.__is_checked_out = True
            else: 
                raise Exception('Buku sudah dipinjam.')
        
        def check_in(self):
            if self.__is_checked_out:
            self.__is_checked_out = False
            else: 
                raise Exception('Buku sudah ada di perpustakaan.')