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

class tree:
    
    def __init__(self,Data):
        self.left=None
        self.right=None
        self.data=Data
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

        if is_op(self.data):
            return op(self.data,float(self.left.estim()),float(self.right.estim()))
        else:
            return float(self.data);
        #print op()

class treeN:
    #self.arr_child=[]
    #data=None
    def __init__(self,Data):
        self.data=None
        self.arr_child=[]
        self.data=Data
    def addLeaf(self,Leaf):
        self.arr_child.append(Leaf)
    def addLeafs(self,*args):
        for i in args:
            self.addLeaf(i)
    def setLeaf(self,Num,Leaf):
        self.arr_child[Num]=Leaf
    def upDown(self):
        print self.data
        for i in self.arr_child:
            i.upDown()

def task_one():
    root=tree('a')
    t_b=tree('b')
    t_c=tree('c')
    t_d=tree('d')
    t_e=tree('e')
    t_f=tree('f')
    t_g=tree('g')
    t_h=tree('h')


    root.setLeaf(t_b,t_e)
    t_b.setLeaf(t_c,t_d)

    t_e.setLeft(t_f)
    t_f.setLeaf(t_g,t_h)


    root.upDown()

def task_two():
    root=treeN('a')
    t_b=treeN('b')
    t_c=treeN('c')
    t_d=treeN('d')
    t_e=treeN('e')
    t_f=treeN('f')
    t_g=treeN('g')
    t_h=treeN('h')


    root.addLeafs(t_b,t_f)
    t_b.addLeafs(t_c,t_d,t_e)

    t_f.addLeafs(t_g,t_h)


    root.upDown()
    

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
    operations=['+','-','*','/']


    zn2=['/','*']
    
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
    if oper == '+':
        return True
    elif oper == '-':
        return True
    elif oper == '*':
        return True
    elif oper == '/':
        return True
    return False

def expr_estim(expr):
    return tree_expr(expr).estim()
  
print 'task one'
task_one()
print 'task two'
task_two()

expr=raw_input('Please input expression [ default expression ((2*4)-(4/6))+(5/(2-1)) ] : ')
if expr=='': expr='((2*4)-(4/6))+(5/(2-1))'
print expr,
print '=',
print expr_estim(expr)


