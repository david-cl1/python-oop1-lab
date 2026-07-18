#!/usr/bin/env python3

class Book:
    def __init__(self):
        self.title = input("Please input the title of the book:... ")
        
        while True:
            try:
                user_input = input("Please input the page count:... ")
                self.page_count = int(user_input)
                break 
            except ValueError:
                print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")