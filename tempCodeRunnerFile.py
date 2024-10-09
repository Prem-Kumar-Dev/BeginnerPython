class Complex_Number:

    def __init__(self,number):
        self.number=number

        if self.number[-1]=='i':
            Complex_Number.symbol=['+','-','*','/','i']
            self.value=[]
            self.digits=0
            self.negative=False
            self.counter=0
            self.realImag=[]
            self.group()
            self.val()
            
        
        else:
            raise ValueError("Not a Complex Number")

    def group(self):
        
        for i in range(0,len(self.number)):

            if self.number[i] not in Complex_Number.symbol:
                if self.negative:
                    self.digits=(self.digits*10)-int(self.number[i])

                else:
                    self.digits=(self.digits*10)+int(self.number[i])
            
            elif((self.number[i] in Complex_Number.symbol and i==0) or (self.number[i-1] in Complex_Number.symbol and self.number[i] in Complex_Number.symbol)):
                if self.number[i]=='-':
                    self.negative=True
                elif(self.number[i]=='+'):
                    pass
                else:
                    raise ValueError("Invalid Format")
            else:
                self.value.insert(self.counter,self.digits)
                self.digits=0
                self.negative=False
                self.counter+=1
                self.value.insert(self.counter,self.number[i])
                self.counter+=1
        print(self.value)
        

    

    def val(self):
        i=0
        self.counter=0
    
        while self.value[i]!='i':
            
            if self.value[i]=='/':
                self.realImag.insert(self.counter,(self.value[i-1]/self.value[i+1]))
                i+=1
                self.counter+=1
            elif self.value[i]=='*':
                self.realImag.insert(self.counter,(self.value[i-1]*self.value[i+1]))
                i+=1
                self.counter+=1
            elif self.value[i]=='-' and i!=0:

                self.value[i+1]=-self.value[i+1]
                
                self.realImag.insert(self.counter,'+')
                self.counter+=1

                if self.value[i+2] not in Complex_Number.symbol:
                    self.realImag.insert(self.counter,self.value[i+1])
                    self.counter+=1
                    i+=1
                    
            elif self.value[i]=='+' and i!=0:

                
                if i-2<len(self.value) and self.value[i+2] not in ['/','*']:

                    self.realImag.insert(self.counter,self.value[i-1])
                    self.counter+=1

                self.realImag.insert(self.counter,'+')
                self.counter+=1

                if i+2 < len(self.value) and self.value[i+2] not in ['/','*']:      
                    self.realImag.insert(self.counter,self.value[i+1])
                    self.counter+=1
            i+=1
        print(self.realImag)
    

cn=Complex_Number("-33100+-55/20i")

print(cn.realImag[0])
#print(cn.realImag[2])

cn2=Complex_Number("10+-3i")






