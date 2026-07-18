#!/usr/bin/env python3

class Book:
    def __init__(self, title=None, page_count=None):
        if title is None:
            title = input("Please input the title of the book:... ")
        self.title = title

        if page_count is None:
            while True:
                try:
                    user_input = input("Please input the page count:... ")
                    self.page_count = int(user_input)
                    break
                except ValueError:
                    pass 
        else:
            self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and not isinstance(value, bool):
            self._page_count = value
        else:
            print("page_count must be an integer")
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")