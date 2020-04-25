from student import *                                                   #importing necessary modules.                                                   
from faculty import *
from book import *
from datetime import date                                               #importing necessary libraries.
import datetime
import pickle

ls=[]
lf=[]
lb=[]

def check_student(r_no):
        
    """This function is defined so as to check whether the student already exist in the system."""
    
    try:
        with open("student_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    if obj[i].rollno==r_no:
                        return True
                    i+=1
                except (EOFError,IndexError):
                    return False
    except:
        return False

    
def add_student():
    
    """This function is defined to add a student record in the system"""
    
    name=input("Enter the name of the student:")
    branch=input("Enter the branch of the student:")
    while True:
        add_year=input("Enter the addmission year:")
        if int(add_year) > date.today().year:
            print("Invalid Admission Year!!")
        else:
            break
    while True:
        ad_id_no=input("Enter the addmission id number:")
        if len(ad_id_no)!=4:
            print("Invalid Admission Id!!")
        else:
            break
    r_no="0187"+branch+add_year+ad_id_no
    if(check_student(r_no)):
            print("Student already exists!!")
    else:
        s=Student(name,branch,add_year,ad_id_no,r_no)
        ls.append(s)
        with open("student_record.pkl","wb") as f:
            pickle.dump(ls,f)    

def display_student(obj):
        
    """This function is defined to display a student record"""
    
    print("*"*70)
    print(f"Name:{obj.s_name}")
    print(f"Branch:{obj.branch}")
    print(f"Admission ID number:{obj.adm_id_no}")
    print(f"Admission year:{obj.adm_year}")
    print(f"Roll number:{obj.rollno}")
    if obj.student_dict is {}:
        print("No Book Issued")
    else:
        print(f"Books issued:{obj.student_dict}")
    print(f"Total number of book issued:{obj.s_bookissued}")
    print("*"*70)

def print_student():
        
    """This function is defined to display record of every student whose record is added to the system"""
    
    try:
        with open("student_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    display_student(obj[i])
                    i+=1
                except:
                    break
    except:
        print("No Record Found")
        
def check_faculty(fac_id):
        
    """This function is defined to check whether the faculty already exist in the system. """
    
    try:
        with open("faculty_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    if obj[i].eid==fac_id:
                        return True
                    i+=1
                except (EOFError,IndexError):
                    return False
    except:
        return False
    
    
def add_faculty():
        
    """This function is defined to add a faculty record in the system"""
    
    name=input("Enter faculty name: ")    
    while True:
        fac_id=input("Enter the Faculty Id:")
        if len(fac_id)!=5:
            print("Invalid Faculty Id!!")
        else:
            break
    if(check_faculty(fac_id)):
            print("Faculty already exists!!")
    else:
        fac=Faculty(name,fac_id)
        lf.append(fac)
        with open("faculty_record.pkl","wb") as f:
            pickle.dump(lf,f)
    
def check_book(isbn,copies):
    try:
        with open("book_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    if obj[i].isbn==isbn:
                        obj[i].copies+=copies
                        with open("book_record.pkl","wb") as f:
                            pickle.dump(obj,f)
                        return True
                    i+=1
                except:
                    return False
    except:
        return False
  
def display_faculty(obj):
    
    """This function is defined to display a faculty record"""
    
    print("*"*70)
    print(f"Faculty name:{obj.ename}")
    print(f"Faculty ID:{obj.eid}")
    print(f"Book issued:{obj.fac_dict}")
    print("*"*70)
    
def print_faculty():
            
    """This function is defined to display record of every faculty whose record is added to the system"""
   
    try:
        with open("faculty_record.pkl","rb") as f:
            l=pickle.load(f)
            i=0
            while True:
                try:
                    display_faculty(l[i])
                    i+=1
                except:
                    break
    except:
        print("No Record Found!")  
def add_book():
    
    """This function is defined to add a book in the system. """
    
    title=input("Enter the title of the book:")
    author=input("Enter the author of the book:")
    while True:
        isbn=input("Enter the International standard book number:")
        if len(isbn)!=13:
            print("Invalid!!Try again")
        else:break
    copies=int(input("Enter the number of copies:"))
    if check_book(isbn,copies):
        pass
    else:
        b=Book(title,author,isbn,copies)
        lb.append(b)
        with open("book_record.pkl","wb") as f:
            pickle.dump(lb,f)
            
def display_book(obj):
    
    """ This function is defined to display a book record present in the system. """
    
    print("*"*70)
    print(f"Title:{obj.title}")
    print(f"Author:{obj.author}")
    print(f"ISBN:{obj.isbn}")
    print(f"Number of copies:{obj.copies}")
    print("*"*70)
          
def print_book():
    
    """ This function is defined to display every book record present in the system. """
    
    try:
        with open("book_record.pkl","rb") as f:
            l=pickle.load(f)
            i=0
            while True:
                try:
                    display_book(l[i])
                    i+=1
                except:
                    break
    except:
        print("No Record Found!")
        
def search_book(mode,data):
    
    """
    This function is defined to search a book by either its ISBN or by its Author name or by its Title.
    If the book is found then it will display all the details of the book otherwise it will display a message of "Not Found"
    """
    
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        if mode.lower()=="isbn":
            while True:
                try:
                    if obj[i].isbn==data:
                        display_book(obj[i])
                        break
                    i+=1
                except:
                    print("Not found")
        elif mode.lower()=="author":
            while True:
                try:
                    if obj[i].author==data:
                        display_book(obj[i])
                        break
                    i+=1
                except:
                    print("Not Found")
        elif mode.lower()=="title":
            while True:
                try:
                    if obj[i].title==data:
                        display_book(obj[i])
                        break
                    i+=1
                except:
                    print("Not Found")
        else:
            print("Wrong choice.!!PLEASE Enter correct mode")
             
def modify_student_issue(rollno,isbn,l):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].rollno==rollno:
                    obj[i].student_dict[isbn]=l
                    obj[i].s_bookissued+=1
                    with open("student_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                pass
def modify_book_issue(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    obj[i].copies-=copies
                    with open("book_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                pass

            
            
def check_std_limit(rollno):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].rollno==rollno and obj[i].s_bookissued>=5:
                    return False
                else:
                    return True
                i+=1
            except:
                pass
def availability_of_book(isbn):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn and obj[i].copies>0:
                    return True
                i+=1
            except:
                return False  
def already_have(isbn,rollno):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].rollno==rollno and isbn in obj[i].student_dict:
                    return True
                i+=1
            except:
                return False
        
        

def issue_book_student():
    rollno=input("Enter roll number of the student:")
    if check_student(rollno):
        if check_std_limit(rollno):
            isbn=input("Enter the isbn number of the book to be issued:")
            if not availability_of_book(isbn):
                print("Either book is not present or all copies are issued to others")
            elif already_have(isbn,rollno):
                print("This student already has the one copy of this book")
            else:
                l=[x for x in str(datetime.date.today()).split("-")]
                modify_student_issue(rollno,isbn,l)
                modify_book_issue(isbn,1)
        else:
            print("Student has reached the book limit.Cannot issue the book")
    else:
        print("Student not found!! Cannot issue book")
       
 
        
def modify_student_return(rollno,isbn):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].rollno==rollno:
                    with open("student_record.pkl","wb") as f:
                        del obj[i].student_dict[isbn]
                        obj[i].s_bookissued-=1
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break
def modify_book_return_s(isbn):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    with open("book_record.pkl","wb") as f:
                        obj[i].copies+=1
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                pass

def return_book_student():
    rollno=input("Enter the rollno of the student:")
    if check_student(rollno):
        isbn=input("Enter isbn:")
        if already_have(isbn,rollno):
            modify_student_return(rollno,isbn)
            modify_book_return_s(isbn)
        else:
            print("Book with this isbn is not issued to this student")
    else:
        print("Student not found")

def modify_book_issue(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    with open("book_record.pkl","wb") as f:
                        obj[i].copies-=copies
                        pickle.dump(obj,f)
                    break
                i+=1
            except :
                pass

def modify_fac(i,isbn,copies):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        if isbn in obj[i].fac_dict:
            with open("faculty_record.pkl","wb") as f:
                obj[i].fac_dict[isbn]+=copies
                pickle.dump(obj,f)
        else:
            with open("faculty_record.pkl","wb") as f:
                obj[i].fac_dict[isbn]=copies 
                pickle.dump(obj,f)
            
                
def check_avail_book(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn and obj[i].copies>=copies: 
                    return True
                i+=1
            except:
                return False

def issue_book_faculty():
    fac_id=input("Enter the id:")
    if check_faculty(fac_id):
        isbn=input("Enter the ISBN:")
        copies=int(input("Enter the number of copies:"))
        if check_avail_book(isbn,copies):
            with open("faculty_record.pkl","rb") as f:
                obj=pickle.load(f)
                i=0
                while True:
                    try:
                        if obj[i].eid==fac_id:
                            modify_fac(i,isbn,copies)
                            modify_book_issue(isbn,copies) 
                            print("Book Issued")
                            break
                        i+=1
                    except:
                        break
        else:
            print("Book does not found in the record")
    else:
        print("Faculty does not exist!!")
                            
def modify_fac_return(fac_id,isbn,co):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].eid==fac_id:
                    if obj[i].fac_dict[isbn]==co:
                        del obj[i].fac_dict[isbn]
                    else:
                        obj[i].fac_dict[isbn]-=co
                    with open("faculty_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break
def modify_book_return_f(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    with open("book_record.pkl","wb") as f:
                        obj[i].copies+=copies
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break

def already_have_fac(isbn,fac_id):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].eid==fac_id:
                    if isbn in obj[i].fac_dict:
                        return True
                i+=1
            except:
                return False

                        
def return_book_faculty():
    fac_id=input("Enter the Employee id:")
    if check_faculty(fac_id):
        isbn=input("Enter isbn:")
        if already_have_fac(isbn,fac_id):
            co=int(input("Enter the no. of copies you want to return"))
            modify_fac_return(fac_id,isbn,co)
            modify_book_return_f(isbn,co)
        else:
            print("Book with this isbn is not issued to this faculty")
    else:
        print("Faculty not found")
