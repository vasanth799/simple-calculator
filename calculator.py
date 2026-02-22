
class Calculator:
    def __init__(self):
        self.a=int(input('ENTER THE FIRST INPUT VALUE:'))
        self.b=int(input('ENTER THE SECOND INPUT VALUE:'))
     
         
        
    def add(self):
        return self.a+self.b   
    def sub(self):
        return self.a-self.b
    def division(self):
       try:
           return self.a/self.b
       except ZeroDivisionError:
           print('enter a valid denominator/second value other than zero')
        
    def remainder(self):
        try:
            return self.a%self.b
        except ZeroDivisionError:
            print('enter a valid denominator/second value other than zero')
       
    def multiplication(self):
        return self.a*self.b
    def exponentiation(self):
        return self.a**self.b
    def floor_division(self):
         try:
             return self.a//self.b
         except ZeroDivisionError:
            print('enter a valid denominator/second value other than zero')
       
    


print("ARITHMETIC OPERATIONS\n")
print('1.ADDITION(+)\n2.SUBTRACTION(-)\n3.MULTIPLICATION(*)\n4.DIVISION(/)\n5.REMAINDER(%)\n6.EXPONENTIONAL(^)\n7.ROUNDEDDIVISON(//)\n8.EXIT\n')  
while True:
         choice=int(input('ENTER YOUR CHOICE:'))
         match choice:
             case 1:
                 try:  
                     C=Calculator()
                     print(f'THE RESULTANT ADDITION VALUE:{C.add()}')
                 except ValueError:
                     print('enter a valid numeric number')       
             case 2:
                 try:
                     C=Calculator()
                     print(f'THE RESULTANT SUBSTRACTION VALUE:{C.sub()}')
                 except ValueError:
                     print('enter a valid numeric number') 
             case 3:
                 try:
                     C=Calculator()
                     print(f'THE RESULTANT MULTIPLICATION VALUE:{C.multiplication()}')
                 except ValueError:
                     print('enter a valid numeric number')     
             case 4:
                  try:   
                     C=Calculator()
                     print(f'THE RESULTANT DIVISION VALUE:{C.division()}')
                  except ValueError:
                     print('enter a valid numeric number')    
             case 5:
                  try:
                     C=Calculator()
                     print(f'THE RESULTANT REMAINDER VALUE:{C.remainder()}')
                  except ValueError:
                     print('enter a valid numeric number')    
             case 6:
                  try:
                     C=Calculator()
                     print(f'THE RESULTANT EXPONENTIONAL VALUE:{C.exponentiation()}')
                  except ValueError:
                     print('enter a valid numeric number')    
             case 7:
                  try:
                     C=Calculator()
                     print(f'THE RESULTANT FLOOR_DIVISION VALUE:{C.floor_division()}')
                  except ValueError:
                     print('enter a valid numeric number')    
             case 8:
                      print('THANK YOU FOR USING CALCULATOR!')
                      print('---------EXITING------------')  
                      exit(0)
                      break
             case _:
                 print(' Invalid choice,please enter your choice again')     
      
      
                 
                 
      
      