
class Student:
    def __init__(self,s_name,branch,adm_year,adm_id_no,rollno):
        self.s_name=s_name
        self.branch=branch
        self.adm_year=adm_year
        self.adm_id_no=adm_id_no
        self.rollno=rollno
        self.s_bookissued=0
        self.student_dict={}