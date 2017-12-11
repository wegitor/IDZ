import math


class treeN:
    #self.arr_child=[]
    #data=None
    def __init__(self,Data,attr=None):
        self.data=None
        self.arr_child=[]
        self.data=Data
        self.ar=None
        self.atr=attr
    def addLeaf(self,Leaf):
        self.arr_child.append(Leaf)
    def addLeafs(self,*args):
        for i in args:
            self.addLeaf(i)
    def setLeaf(self,Num,Leaf):
        self.arr_child[Num]=Leaf
    def upDown(self):
        print 'node:',self.data,
        if self.atr!=None:
            print 'atr:',self.atr,
        for i in self.arr_child:
            i.upDown()
        print ' return'
    def upDownL(self,list):
        if self.arr_child==[]:
            print self.data
        for i in self.arr_child:
            if i.atr==list[self.data]:
                i.upDownL(list)
        

input_d=[[0, 0, 0, 1, False],
        [0, 0, 1, 0, False],
        [0, 1, 0, 2, True],
        [0, 1, 1, 1, False],
        [0, 1, 1, 2, False],
        [1, 1, 1, 1, False],
        [1, 1, 0, 0, True],
        [1, 1, 1, 1, True],
        [2, 0, 0, 0, True],
        [2, 0, 0, 1, True],
        [2, 0, 0, 2, False],
        [2, 0, 1, 0, False],
        [2, 0, 1, 2, False],
        [2, 1, 0, 2, True]]

input_d=[[0, 2, 0, 0, False],
        [0, 2, 0, 1, False],
        [1, 2, 0, 0, True],
        [2, 1, 0, 0, True],
        [2, 0, 1, 0, True],
        [2, 0, 1, 1, False],
        [1, 0, 1, 1, True],
        [0, 1, 0, 0, False],
        [0, 0, 1, 0, True],
        [2, 1, 1, 0, True],
        [0, 1, 1, 1, True],
        [1, 1, 0, 1, True],
        [1, 2, 1, 0, True],
        [2, 1, 0, 1, False]]

"""

"""

def get_range(ar,col):
    return 0

    
def logg(x,base):
    if x==0:
        return 0
    else:
        return math.log(x,base)
    
def estim_count(ar,col):
    #print 'est size: ', len(ar) , 'col: ',col
    #print 'est in:',ar
    tmp_tr=[]
    tmp_fa=[]

    lenc=len(ar[0])-1
    i=0
    while i in range(lenc):
        #print 'len:  ',lenc,'i: ',i
        tmp_tr.append(0); tmp_fa.append(0)
        for el in ar:
            if el[col]==i:
                #print 'end el: ', el[len(el)-1]
                if el[len(el)-1]:
                    tmp_tr[i]+=1
                else: tmp_fa[i]+=1
        if tmp_tr[i]==0 and tmp_fa[i]==0:#delete elem if is not in range
            #print 'ok'
            del tmp_tr[i]
            del tmp_fa[i]
            lenc-=1
            continue
        i+=1
        
       

    tmp_tr.append(0)
    tmp_fa.append(0)
    for el in ar:
        if el[len(el)-1]:
            tmp_tr[len(tmp_tr)-1]+=1
        else: tmp_fa[len(tmp_fa)-1]+=1

    #print tmp_tr,tmp_fa
    E=0
    for i in range(len(tmp_tr)-1):
        val=tmp_tr[i]+tmp_fa[i]
        val1=(float)(tmp_tr[i])/(float)(val)
        val2=(float)(tmp_fa[i])/(float)(val)
        #print val, val1,val2
        E+=val*(-(val1*logg(val1,2)) - val2*logg(val2,2) )
    #print E
    E/=len(ar)
    tr=tmp_tr[len(tmp_tr)-1]
    fa=tmp_fa[len(tmp_fa)-1]
    val=tr+fa
    val1=(float)(tr)/(float)(val)
    val2=(float)(fa)/(float)(val)
    gain= ((-(val1*logg(val1,2)) - val2*logg(val2,2)  )-E)
    #print 'Gain:',gain
    return gain

def column(matrix, i):
    return [row[i] for row in matrix]
def dif(ar):
    ells=column(ar,len(ar[0])-1)
    tmp=ells[0]
    for el in ells[1:]:
        if el!=tmp:
            return False
    return True
def tree_build(ar,list_c ,atr=None):
    print 'tree:',ar

    #print len(ar[0])-1
    #if dif(ar, len(ar[0])-1):
    #   return treeN('-',atr)#ar[0][len(ar)-1])
    
    list_tmp=[]
    len_col=len(ar[0])
    for i in range(len_col-1):
        list_tmp.append(estim_count(ar,i))

    print 'estim_count',list_tmp
    #if len(ar[0])<2:
        #print 'less: ',ar
    coll=list_tmp.index(max(list_tmp))
    #rint 'len',(len(input_d[0])-1)-(len(ar[0])-1)+coll
    numCol=(len(input_d[0])-1)-(len(ar[0])-1)+coll
    numCol=coll
    col_n=list_c[numCol]
    print numCol
    del list_c[numCol]
    tr=treeN(col_n,atr)
    tr.ar=ar
    for i in range(3):
        tmp_ar=[]
        for el in ar:
            #print el[coll],'==',i
            if el[coll]==i:
                tmp_el=list(el)
                #print 'del in: ',el
                del tmp_el[coll]
                #print 'after ',tmp_el
                tmp_ar.append(tmp_el)
        if tmp_ar!=[]:
            
            if not(dif(tmp_ar)) and len(tmp_ar[0])>1:
                #print 'tr build: ',tmp_ar
                tr.addLeaf(tree_build(tmp_ar,list(list_c),i))
            elif dif(tmp_ar) and len(tmp_ar[0])>1:
                #print 'create leaf,',tmp_ar[0][len(tmp_ar[0])-1] , tmp_ar
                tr.addLeaf(treeN(tmp_ar[0][len(tmp_ar[0])-1],i) )
    print 'return'
    return tr


tree=tree_build(input_d,range(len(input_d[0])-1))

print tree.data
for el in tree.arr_child:
    print el.data ,': ',el.ar





print 'tree print'
tree.upDown()

#tree.upDownv()

#print 'for: ', [2,2,2,2]
print 'for: ', [2,1,1,2]
#print 'for : ',input_d[0][:-1]
print 'is: ',
#tree.upDownL(input_d[0][:-1])
#tree.upDownL([2,2,00,1])
tree.upDownL([2,2,1,1])
