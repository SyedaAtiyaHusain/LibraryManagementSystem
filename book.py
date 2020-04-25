class Book: 
  
  """
  This class is defined so as to create the instance of book which will contain the titile,
  author, number of copies and isbn number, fields.
  """
  
    def __init__(self,title,author,isbn,copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies
