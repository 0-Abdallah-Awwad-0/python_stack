from abc import ABC, abstractmethod
from datetime import date


class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

        # Encapsulation: private attributes
        self.__is_borrowed = False
        self.__borrower = None
        self.__due_date = None

    def borrow(self, user, due_date):
        if self.__is_borrowed:
            print(f"{self.title} is already borrowed.")
        else:
            self.__is_borrowed = True
            self.__borrower = user
            self.__due_date = due_date
            print(f"{self.title} borrowed by {user}.")

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            self.__borrower = None
            self.__due_date = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def check_availability(self):
        return not self.__is_borrowed

    def notify_overdue(self, current_date):
        if self.__is_borrowed and current_date > self.__due_date:
            days_late = (current_date - self.__due_date).days
            fee = self.calculate_late_fee(days_late)
            print(f"Overdue notice: {self.title} is {days_late} days late.")
            print(f"Borrower: {self.__borrower}")
            print(f"Late fee: ${fee}")
        else:
            print(f"{self.title} is not overdue.")

    @abstractmethod
    def calculate_late_fee(self, days_late):
        pass


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def calculate_late_fee(self, days_late):
        return days_late * 1


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_num):
        super().__init__(title, item_id)
        self.issue_num = issue_num

    def calculate_late_fee(self, days_late):
        return days_late * 0.5


class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    def calculate_late_fee(self, days_late):
        return days_late * 2


# Testing the system

book1 = Book("Python Basics", 1, "John Smith")
magazine1 = Magazine("Tech Monthly", 2, 45)
dvd1 = DVD("OOP Tutorial", 3, "120 minutes")

book1.borrow("Abdallah", date(2026, 5, 10))
magazine1.borrow("Ali", date(2026, 5, 20))
dvd1.borrow("Omar", date(2026, 5, 8))

print(book1.check_availability())
print(magazine1.check_availability())

book1.notify_overdue(date(2026, 5, 13))
magazine1.notify_overdue(date(2026, 5, 13))
dvd1.notify_overdue(date(2026, 5, 13))

book1.return_item()
print(book1.check_availability())