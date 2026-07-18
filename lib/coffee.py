#!/usr/bin/env python3

class Coffee:
    def __init__(self, size=None, price=None):
        if size is None:
            size = input("Please select your coffee size : Small, Medium or Large ")
        if price is None:
            price = float(input("Please input the coffee price: "))
            
        self.size = size
        self.price = float(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = value

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")