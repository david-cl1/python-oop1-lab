#!/usr/bin/env python3

class Book:
    def __init__ (self):
        title = input("Please input the title of the book:... ")
        self.title = title
        page_count = input (int("Please input the page count:..."))
        y = True
        while y == True:
            try:
                page_count = float(page_count)
                y = False
            except:
                print("page_count must be an integer")

        self.pagecount = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")