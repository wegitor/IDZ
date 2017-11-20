#import sys;

def sort_mas(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if i!=k:
                if arr[i][0]>arr[k][0] :
                    tmp_arr=arr[i]
                    arr[i]=arr[k]
                    arr[k]=tmp_arr
    
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


objects_rural=[]

line=''

for line in f :
        arr=line.split(',')
        objects_rural.append(arr)
        #for i in range(len(arr)):
         #       f_o.write(str(StrLength(arr[i])))
          #      if(i!=len(arr)-1):
           #          f_o.write(',')
        #f_o.write('\n')

#while( (line=f.readline()))
#       print(line)


f_o.close()


test_arr=[]

sort_mas(objects_rural)

count=0
for i in objects_rural:
    print count,
    arr=i
    for k in range(len(arr)):
        print arr[k].decode('utf-8'),
    print ''
    count+=1


