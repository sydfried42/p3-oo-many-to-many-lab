class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be an instance of a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an instance of an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        resault = []
        # return all contracts that have the same date as the date passed into the method
        for contract in cls.all:
            if contract.date == date:
                resault.append(contract)
        return sorted(resault, key=lambda x: x.date)

class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    def contracts(self):
        # loop through contracts
        authors_contracts = []
        for contract in Contract.all:
            if contract.author is self:
                authors_contracts.append(contract)
        return authors_contracts
        # return [contract for contract in Contract.all if contract.author is self]
        
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]

    def sign_contract(self, book, date, royalties): 
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self): 
        total = 0
        for contract in Contract.all:
            if contract.author is self:
                total += contract.royalties
        return total

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]

