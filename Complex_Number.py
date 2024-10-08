class Complex_num:

    def __init__(self,number):     
        self.number = str(number)
        if self.number[-1]=='i':
            
            Complex_num.symbol=['+','-','*','/','i']
            self.values=[]
            self.digit=0
            self.c=0
            self.negative=None
        else:
            raise ValueError("Not a Complex Number")
        
    
    def group(self):

        i=0

        while i<len(self.number):

            if self.number[i] in Complex_num.symbol and i==0:
                if (self.number[i+1] in Complex_num.symbol or self.number[i] in ['/','*']):
                    raise ValueError('Invalid Format!')

                elif (self.number[0]=='-'):
                    self.negative=True
                elif(self.number[0]=='+'):
                    pass
                
            
            elif self.number[i] in Complex_num.symbol and i!=0:
                
                self.values.insert(self.c,self.digit)
                self.c+=1
                self.digit=0

                if (i!=len(self.number)-1):
                    self.values.insert(self.c,self.number[i])
                    self.c+=1
                    if self.number[i+1] in Complex_num.symbol:
            
                        if (self.number[i]!=self.number[i+1] and self.number[i+1]=='-') or (self.number[i]==self.number[i+1] and self.number[i]=='-'):
                            self.negative=True
                            i=i+1
                        elif(self.number[i]!=self.number[i+1] and self.number[i+1]=='+') or (self.number[i]==self.number[i+1] and self.number[i]=='+'):
                            i=i+1
                        else:
                            raise ValueError("Enter in correct Format!")

                                

                    elif(self.number[i+1]=='/' or self.number=='*'):
                            raise ValueError("Enter in correct format!")
                    
                    
                
            

                
            else:
                if self.digit>=0:
                    self.digit=(self.digit*10)+int(self.number[i])
                else:
                    self.digit=(self.digit*10)-int(self.number[i])

                if self.digit>0 and self.negative==True and i-1!=0:
                    self.digit=-(self.digit)
                    self.negative=False
            i+=1

        print(self.values)





cn =Complex_num('-5454-+301044i')
cn.group()
                
                

