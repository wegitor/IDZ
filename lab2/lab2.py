#import sys;




def StrLength(s):
        count=0
        for i in range(len(s)):
                if s[i]!=' ' :
                        count+=1;
                        #print(s[i])
        return count
        
#StrLength('test test')

f = open('input.cvs','r')
f_o= open('output.cvs','w')

line=''

for line in f :
        arr=line.split(',')
        for i in range(len(arr)):
                f_o.write(str(StrLength(arr[i])))
                if(i!=len(arr)-1):
                     f_o.write(',')
        f_o.write('\n')

#while( (line=f.readline()))
#       print(line)


f_o.close()


