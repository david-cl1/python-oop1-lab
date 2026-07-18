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
                    print("page_count must be an integer")
        else:
            if isinstance(page_count, int):
                self.page_count = page_count
            else:
                print("page_count must be an integer")
                self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")