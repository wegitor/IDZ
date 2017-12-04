#import sys;
import re

def sort_mas(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if i!=k:
                if arr[i][0]<arr[k][0] :
                    tmp_arr=arr[i]
                    arr[i]=arr[k]
                    arr[k]=tmp_arr


objects_rural=[]


def help():
    print 'File input f\nFile Output w\nSort sor\nPrint p\nSet s\nDelete d\nEdit e\nSet const c\nCompare cmp\nSearch sea\nHelp h\nQuit q\n'

line=''
line=raw_input('please enter command: ')

#help()
while(True):
    
    if line=='f':
        f = open('input.cvs','r')

        
        objects_rural=[]

        line=''

        for line in f :
                arr=line.decode('utf-8').encode('cp1251').split(',')

                objects_rural.append(arr)
   

    if line=='p':
        

        count=0
        for i in objects_rural:
            print count,
            arr=i
            for k in range(len(arr)):
                print arr[k],#.decode('utf-8'),
            print ''
            count+=1
    if line=='sor':
        sort_mas(objects_rural)
    if line=='s':
        print 'Name\tType\tEmploers\tFunction\tIncome'
        objects_rural.append(raw_input('').split())
       # f_o.close()
    if line=='w':
        name=raw_input('file name (default output.cvs): ')
        if name=='' :
            name= 'output.cvs'
        f_o=file(name,'w')
        for i in objects_rural:
            for j in range(len(i)):
                f_o.write(i[j])
                if j+1!=len(i):
                    f_o.write(', ')
            f_o.write('\n')
        f_o.close()
    if line=='d':
        objects_rural.remove(objects_rural[input('Enter number for delate: ')])
    if line=='e':
        
        num=input('Input num for edit: ')
        print 'Name\tType\tEmploers\tFunction\tIncome'
        for k in objects_rural[num]:
            print k,#.decode('utf-8'),
            print '\t',
        print ''

        print 'Input line: '
        objects_rural[num]=raw_input('').split()
    if line=='c':
        print 'i/o'
    if line=='cmp':
        num=raw_input('Input numbers for compare: ')
        print 'Name\tType\tEmploe\tFunc\tIncome'
        num1=int(num.split(' ')[0])
        num2=int(num.split(' ')[1])

        num1=objects_rural[num1]
        num2=objects_rural[num2]


        for i in range(len(num1)):
            
            print num1[i],
            print '\t',
        print ''
        for i in range(len(num2)):
            
            print num2[i],
            print '\t',
        print ''
        for i in range(len(num1)):
            
            print num1[i]==num2[i],
            print '\t',
        print ''
    if line=='sea':
        expr=raw_input('Please input search expr: ')
        for i in objects_rural:
            len2=i

            find=False
            for j in len2:
                m=re.search(expr,j)
                if m :
                    find=True
            if find:
                for l in i:
                    print l,
                print ''
                
    if line=='h':
        help()
    if line=='q':
        print 'exit'
        break
    line=raw_input('Please enter command: ')



