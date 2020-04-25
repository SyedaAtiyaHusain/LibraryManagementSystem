class Student:  
  
    """
    This class is defined so as to create the instance of student which will contain the name,branch, admission year,
    admission ID, roll no, student bookissued count and dictionary to keep the record of books which student has issued, fields.
    """
    
    def __init__(self,s_name,branch,adm_year,adm_id_no,rollno):
        self.s_name=s_name
        self.branch=branch
        self.adm_year=adm_year
        self.adm_id_no=adm_id_no
        self.rollno=rollno
        self.s_bookissued=0
        self.student_dict={}
