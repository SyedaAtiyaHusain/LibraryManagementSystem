class Faculty:
  
  """
  This class is defined so as to create the instance of faculty which will contain the name,
  faculty id, employee bookissued count and dictionary to keep the record of books which faculty has issued, fields.
  """  
  
  def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
        self.e_bookissued=0
        self.fac_dict={}
