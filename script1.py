from functions import *
from getpass import getpass
admin_password="admin"
while True:
    ch=input("Which type of user you are?\n1. Librarian\n2. Faculty\n3. Student\4.Exit")
    if ch=="1":
        password=getpass()
        if password==admin_password:
            while True:
                v=input("1.Add student\n2.Add Faculty\n3.Add Book\n4.Issue book to student\n5.Issue book to faculty\n6.Return book  by student\n7.return book by faculty\n8.Search book\n9.Print book record\n10.Print Student record\n11.Print faculty record\n12Exit\n-->")
                if v=="1":
                    add_student()
                elif v=="2":
                    add_faculty()
                elif v=="3":
                    add_book()
                elif v=="4":
                    issue_book_student()
                elif v=="5":
                    issue_book_faculty()
                elif v=="6":
                    return_book_student()
                elif v=="7":
                    return_book_faculty()
                elif v=="8":
                    mode=input("Enter the mode by which you want to search\nisbn\ntitle\nauthor\n-->")
                    data=input("Enter data to be searched:")
                    search_book(mode,data)
                elif v=="9":
                    print_book()
                elif v=="10":
                    print_student()
                elif v=="11":
                    print_faculty()
                else:
                    break
        else:
            print("Wrong password!")
    elif ch=="2":
        print("Welcome!!")
        while True:
            v=input("1.View user detail\n2.View books detail\n3.Search a book\n4.Exit\n-->")
            if v=="1":
                eid=input("Enter Faculty ID:")
                fac_disp(eid)
            elif v=="2":
                print_book()
            elif v=="3":
                mode=input("Enter the mode by which you want to search\nisbn\ntitle\nauthor\n-->")
                data=input("Enter data to be searched:")
                search_book(mode,data)
            elif v=="4":
                print("closed")
                break
            else:
                print("Invalid choive")
    elif ch=="3":
        print("Welcome!!")
        while True:
            v=input("1.View user detail\n2.View books detail\n3.Search a book\n4.Exit\n-->")
            if v=="1":
                rollno=input("Enter rollno:")
                stud_disp(rollno)
            elif v=="2":
                print_book()
            elif v=="3":
                mode=input("Enter the mode by which you want to search\nisbn\ntitle\nauthor\n-->")
                data=input("Enter data to be searched:")
                search_book(mode,data)
            elif v=="4":
                print("closed")
                break
            else:
                print("Invalid choive")
            
    elif ch=="4":
        print("Closed")
        break
    else:
        print("Invalid choive")
        
    