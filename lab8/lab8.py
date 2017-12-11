import re

def is_set(x, n):
    return x & 2**n != 0 

    
def op(oper,left,right):
    rez=None
    if oper == 'V':
        rez=left or right
    elif oper == 'A':
        rez=left and right
    elif oper == '>':
        rez=not(left) or right
    elif oper == '~':
        rez= left == right
    return rez
dictt={}
tmp_ist=[]
oper_ist=[]
class tree:
    
    def __init__(self,Data,ist=False):
        self.left=None
        self.right=None
        self.data=Data
        #if ist:
        oper_ist=[]
        tmp_ist=[]
    def setData(self,Data):
        self.data=Data
    def setLeft(self,Left):
        self.left=Left
    def setRight(self,Right):
        self.right=Right
    def setLeaf(self,Left,Right):
        self.left=Left
        self.right=Right
    def upDown(self):
        print self.data
        if self.left: self.left.upDown()
        if self.right: self.right.upDown()
    def estim(self):
        #print self.data
        global tmp_ist, oper_ist,dictt
        if is_op(self.data):
            opp_rez=op(self.data,self.left.estim(),self.right.estim())
            oper_ist.append(self.data)
            tmp_ist.append(opp_rez)
            return opp_rez
        else:
            if not (self.data.isupper()):
                opp_rez= dictt[self.data];
                return opp_rez
            else:
                oper_ist.append(self.data)
                opp_rez = not(dictt[self.data.lower()]);

                tmp_ist.append(opp_rez)
                return opp_rez
        #print op()
    

def split_by_zn(zn,expr):    
    list_sp=[]
    count_open=0
    last_non_dig=-1
    i=0
    while i < len(expr):
        brackets=False

        if expr[i]=='(':
            count_open+=1
            brackets=True
            tmp_s=expr[i]           

            i+=1

            while count_open:

                tmp_s +=expr[i]
                
                if expr[i]==')':
                    count_open-=1
                    last_non_dig=i

                    if count_open==0:
                        list_sp.append(tmp_s)
                        #print 'clouse'
                        i+=1
                        break
                                 
                elif expr[i]=='(':
                    count_open+=1
                    print count_open

                i+=1
        if i >=len(expr):
            break
        if expr[i] in zn :
            if not(brackets):
                list_sp.append(expr[last_non_dig+1:i])
            list_sp.append(expr[i])
            last_non_dig=i

        if i+1==len(expr):
            list_sp.append(expr[last_non_dig+1:])

        i+=1

    print 'split:', list_sp
    return  list_sp

def digit(expr):
    if expr[0]=='(':
        return tree_expr(expr[1:-1])

    return tree(expr)

def tree_expr(expr):
    operations=['V','A','>','~']


    zn2=['']
    
    list_str=split_by_zn(operations,expr)
    list_tr=[]

    ##gen nodes
    for el in list_str:
        if is_op(el):
             list_tr.append(tree(el))
             
        else:         
            list_tr.append(digit(el))

    ##first priority
    if len(list_tr)>3:
        i=0
        while i < len(list_tr) :

            
            
            if list_tr[i].data in zn2:
                if list_tr[i].right and  list_tr[i].left:
                    i+=1
                    continue
                list_tr[i].setLeaf(list_tr[i-1],list_tr[i+1])
                del list_tr[i-1]
                i-=1
                del list_tr[i+1]
            i+=1
    
    if len(list_tr)>=3:
        tr=list_tr[1]
        tr.setLeaf(list_tr[0],list_tr[2])

        ##last priority
        for i in range(3,len(list_tr)-1):
            tmp_tree=list_tr[i]
            tmp_tree.setLeaf(tr,list_tr[i+1])
            tr=tmp_tree
    else:
        tr=list_tr[0]

    
    return tr


def is_op(oper):
    if oper == 'V':
        return True
    elif oper == 'A':
        return True
    elif oper == '>':
        return True
    elif oper == '~':
        return True
    return False

def expr_estim(expr):
    global tmp_ist, oper_ist,dictt

    list_ist=[]
    
    dictt['+']=True
    dictt['-']=False

    
    list_char=[]

    for el in re.split("[AV>~()]+",expr):
        if el!='':
            if not (el.lower() in list_char):
                list_char.append(el.lower())
                oper_ist.append(el.lower())
        

    for i in range(pow(2 , len(list_char))):
        list_isft=[]
        for el in list_char:
            if el!='+' and el!='-':
                dictt[el]=is_set(i,list_char.index(el))
            list_isft.append(dictt[el])


        tree_expr(expr).estim()
        #estim(tree_expr(expr),True)

        
        for j in range(len(tmp_ist)):
        #for j in range(i*4,i*4+4):
            #print j
            #raw_input()
            list_isft.append(tmp_ist[j])
        tmp_ist=[]
        list_ist.append(list_isft)
    
    print 'list_ist: '
    for i in range(len(list_ist[0])):
        print oper_ist[i],'\t',
    print ''
    for i in list_ist:
        for j in range(len(i)):
            print i[j],'\t',
        print ''
    
    return list_ist

def exp(expr):
    global tmp_ist, oper_ist
    oper_ist=[]
    tmp_ist=[]
    return expr_estim(expr)

def column(matrix, i):
    return [row[i] for row in matrix]


expr=raw_input('Please input expression [ default expression ((p>q)A(P>q))~(P>Q)] : ')
if expr=='': expr='((p>q)A(P>q))~(P>Q)'

rez= exp(expr)

for i in range(len(rez[0])-1):
    for j in range(len(rez[0])-1):
        col=column(list(rez),i)
        if i!=j:
            if col==column(list(rez),j):
                print 'have tavtology ',
                print 'i:',i,'j:',j
