class asd:
    def __init__(self, name):
        self.name = name
    def printString(self,line):
      self.line=line
      t=''
      for i in self.line:
        if( i>='a' and i<='z'): t+=chr(ord(i)-32)
        else: t+=i
      print(t)
a = asd(input())

a.printString(a.name)

