class MECHStudent:                
 
 
    stream = 'mech'            
 
   
    def __init__(self, roll):
   
          
        self.roll = roll       
  

a = MECHStudent(101)
b = MECHStudent(102)
  
print(a.stream)  
print(b.stream)  
print(a.roll)    
  

print(MECHStudent.stream)   
