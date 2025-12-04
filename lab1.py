# HW1 - Book Class 

class Book:
    def __init__(self, title, author, year, price):
        # خصائص الكتاب
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
        # عرض معلومات الكتاب
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: {self.price} SR")

    def discount(self, percent):
        # تطبيق خصم
        self.price -= self.price * (percent / 100)


# إنشاء ثلاثة كائنات
b1 = Book("Clean Code", "Robert Martin", 2008, 150)
b2 = Book("Python Crash Course", "Eric Matthes", 2019, 120)
b3 = Book("Algorithms", "Sedgewick", 2016, 180)

print("Before Discount:")
b1.display_info()
b2.display_info()
b3.display_info()

# تطبيق خصم
b1.discount(10)
b2.discount(15)
b3.discount(5)

print("\nAfter Discount:")
b1.display_info()
b2.display_info()
b3.display_info()
