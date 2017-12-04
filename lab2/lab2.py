#import sys;




def StrLength(s):
        count=0
        for i in range(len(s)):
                if s[i]!=' ' and s[i]!='\n':
                        #estimate count non-space chars
                        count+=1;
                        #print(s[i])
        return count
        
print StrLength('test test')

f = open('input.cvs','r')
f_o= open('output.cvs','w')

line=''

for line in f :
        #split input lines frow cvs file
        arr=line.split(',')
        for i in range(len(arr)):
                f_o.write(str(StrLength(arr[i])))
                if(i!=len(arr)-1):
                     f_o.write(',')
        f_o.write('\n')


f_o.close()


