import random
import numpy
class matrix:
    
    
    #self.rows=0
    #self.colls=0
    def __init__(self,rows_i,colls_i):
        self.arr_matr=[]
        self.rows=rows_i
        self.colls=colls_i
        
        for i in  range(self.rows):
            tmp_list=[]
            for i in range(self.colls):
                tmp_list.append(0);
            self.arr_matr.append(tmp_list)
    def gen_M(self,fill):
        #if fill<=0:
        for i in range(self.rows):
            for j in range(self.colls):
                self.arr_matr[i][j]=random.randrange(1,fill);
                
                #if i<rows/2 & j   (i== rows/2 & j==colls/2)

                if j>i and i%2==0  : self.arr_matr[i][j]=0
                elif i>j and i%2==1 : self.arr_matr[i][j]=0
                
                #if i==j : matr[i][j]=7
    
    #def genMatr(rows,colls)

    def getRows(self):
        return self.rows
    
    def getColls(self):
        return self.colls
    
    def setItem(self,row,coll,value):
        self.arr_matr[row][coll]=value
        
    def getItem(self,row,coll):
        return self.arr_matr[row][coll]
    
    def addMatr(self,matrB):
        Matr=matrix(self.rows,self.colls)

        for i in range(self.rows):
            for j in range(self.colls):
                Matr.setItem(i,j,self.arr_matr[i][j]+matrB.getItem(i,j))
        return Matr
    def subMatr(self,matrB):
        Matr=matrix(self.rows,self.colls)

        for i in range(self.rows):
            for j in range(self.colls):
                Matr.setItem(i,j,self.arr_matr[i][j]-matrB.getItem(i,j))
        return Matr
    
    def mulMatr(self,matrB):
        Matr=matrix(self.rows,matrB.getColls())

        for i in range(self.rows):
            for j in range(matrB.getColls()):
                for k in range(self.colls):
                    print Matr.getItem(i,j) ,
                    print '+',
                    print self.arr_matr[i][k],
                    print '*',
                    print matrB.getItem(k,j)
                    Matr.setItem(i,j,Matr.getItem(i,j)+self.arr_matr[i][k]*matrB.getItem(k,j))
        return Matr
    def invert(self):
        Matr=matrix(self.colls,self.rows)
        ff=numpy.matrix(self.arr_matr)
        Matr.arr_matr=ff.getI().tolist()
        return Matr
    def divMatr(self,matrB):
        return self.mulMatr(matrB.invert())
    def printM(self):
        for i in range(self.rows):
            print(self.arr_matr[i])

def op(oper,left,right):
    rez=0
    if oper == '+':
        rez=left+right
    elif oper == '-':
        rez=left-right
    elif oper == '*':
        rez=left*right
    elif oper == '/':
        rez=left/right
    return rez
def is_op(oper):
    if oper == '+':
        return True
    elif oper == '-':
        return True
    elif oper == '*':
        return True
    elif oper == '/':
        return True
    return False

def polish_expr():
    expr=raw_input('Input polish expression: ')

    arr=expr.split(' ')


    stack=[]
    stack.append(arr[0])
    stack.append(arr[1])


    for i in range(2,len(arr)):
        if is_op(arr[i]):
            left=int(stack.pop())
            right=int(stack.pop())
            stack.append(op(arr[i],left,right))
        else:
            stack.append(arr[i])
    print stack

def matr_expr():
    line=raw_input('Please input size matrix  end operation [example 3 3 *] :').split(' ')

    
    Matr_a=matrix(int(line[0]),int(line[1]))

    Matr_a.gen_M(9)

    Matr_a.printM()
    print ''
    
    Matr_b=matrix(int(line[0]),int(line[1]))
    Matr_b.gen_M(9)
    Matr_b.printM()

    print ''

    print '='
    
    oper=line[2]
    if oper=='*':
        Matr_a.mulMatr(Matr_b).printM()
    if oper=='-':
        Matr_a.subMatr(Matr_b).printM()
    if oper=='+':
        Matr_a.addMatr(Matr_b).printM()
    if oper=='/':
        Matr_a.divMatr(Matr_b).printM()

def help():
    print 'expresion e\nmatr m\nHelp h\nQuit q\n'

line=''
line=raw_input('please enter command: ')


while(True):
    
    if line=='e':
        polish_expr()
    if line=='m':
        matr_expr()
    if line=='h':
        help()
    if line=='q':
        print 'exit'
        break
    line=raw_input('please enter command: ')


