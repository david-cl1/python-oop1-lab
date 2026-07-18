#!/usr/bin/env python3

class Coffee:
    def __init__(self):
        size = input("Please select your coffee size : Small, Medium or Large")
        if size== "Small" :
            size = "Small"
        elif size == "Medium":
            size= "Medium"
        elif size == "Large":
            size= "Large"
        else:
            print("size must be Small, Medium, or Large")
        self.size = size
        price = input(int("Please input the coffee price:..."))
        self.price =price
    def tip(self):
        self.price+=1
        print("This coffee is great, here's a tip!")