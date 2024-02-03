# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self,title):
    self.title = title

'''
class Author(Book):
  def __init__(self,auth):
    super
    self.auth = auth
'''

# TODO: create instances of the class
book1 = Book("Cracking the code Interview")
#book2 = Author("Raj")

# TODO: print the class and property
# print(book1)
print(book1.title)
