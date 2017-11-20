#import sys
import random
s = self
class matrix:
    
    arr_matr=[[]]
    rows=0
    colls=0
    def __init__(self,rows_i,colls_i,fill=9):
        rows=rows_i
        colls=colls_i
        
        for i in  range(rows):
            tmp_list=[]
            for i in range(colls):
                if fill>0 : tmp_list.append(random.randrange(1,fill));
                else : tmp_list.append(fill);
            self.arr_matr.append(tmp_list)

        if fill<0:
            for i in range(rows):
                for j in range(colls):

                    
                    #if i<rows/2 & j   (i== rows/2 & j==colls/2)

                    if j>i and i%2==0  : self.arr_matr[i][j]=0
                    elif i>j and i%2==1 : self.arr_matr[i][j]=0
                    
                    #if i==j : matr[i][j]=7
    
    #def genMatr(rows,colls)

    def getRows():
        return rows
    
    def getColls():
        return colls
    
    def setItem(Row,Coll,value):
        arr_matr[row][coll]=value
        
    def getItem(Row,Coll):
        return arr_matr[row][coll]
    
    def addMatr(matrB):
        Matr=maxtrix(rows,colls,0)

        for i in range(rows):
            for j in range(colls):
                Matr.setItem(i,j,arr_matr[i][j]+matrB.getItem(i,j))
        return Matr
    
    def mulMatr(s.matrB):
        Matr=matrix(s.rows,matrB.getColls(),0)

        for i in range(s.rows):
            for j in range(matrB.getColls()):
                for k in range(colls):
                        Matr.setItem(i,j,Matr.getItem[i][j]+s.arr_matr[i][k]*matrB.getItem(k,j))
        return Matr

    def printM(self):
        for i in range(self.rows):
            print(arr_matr[i])


Matr_a=matrix(2,2)
Matr_a.printM()

"""
My_matr1=genMatr(2,2)
#printMatr(My_matr1,10)
print("")
matTask(My_matr1,2,2)
printMatr(My_matr1,2)

My_matr2=genMatr(2,3)
#printMatr(My_matr2,10)
print("")
matTask(My_matr2,2,3)
printMatr(My_matr2,2)


print("")

RezMatr=mulMatr(My_matr1,My_matr2,2,3,2)

printMatr(RezMatr,2)

#print (genMatr(10,10));





while true :
    #Expr=raw_input("Pleas input expression: ")

    Expr=input()
    

    #print("You are enter: "+Expr)
    
    
"""


