def in_set(i,set):
    for el in set:
        if el==i:
            return True
    return False
def in_sets(gen,sets):
    main_all=False
    for le in sets:
        all=True
        for i in gen:
            if  not in_set(i,le):
                all=False
        if all:
            main_all=True
    return main_all
def print_items(items):
    for i in items:
        for j in i:
            print '[',
            for h in range(len(j)):
                print j[h],
                #if h!=len(j)-1: print ',',
            print ']',
        print ''
## transactions
##{A, B, C, K},{A, B, C, D, E},{A, C, D, E},{A, B, C}
##      A,B,C,D,E,K
trans=[[1,1,1,0,0,1],
       [1,1,1,1,1,0],
       [1,0,1,1,1,0],
       [1,1,1,0,0,0]]

size=6

transac=4

trans=[[1,0,1,1],
       [0,1,0,1],
       [1,1,0,1]]

size=4


transac=3


supp_min=60
conf_min=80

frequent_item=[]
supp=[]

tmp_list=[]
for i in range(size):
    tr_list=[]
    tr_list.append(i)
    tmp_list.append(tr_list)
frequent_item.append(tmp_list)

## main support 0 level
supp_m=[]
for i in range(size):
    
    supp_m.append(0)
    coun=0
    for el in trans:
        coun+=el[i]
    supp_m[i]=(float) (coun)/ (float)(transac) * 100

supp.append(supp_m)
##gen next set
gen_tmp=[]
for i in range(size):
    for j in range(i,size):
        if i!=j : gen_tmp.append([i,j])
        print j,
    print ''

frequent_item.append(gen_tmp)  
print frequent_item

for k in range(1,size-1):
    #print_items(frequent_item)

    
    count=[]
    tmp_supp=[]
    fr_it_tmp=[]

    print 'step: ', k
    
    ## support estim
    i =0
    while i <len(frequent_item[k]):
        print 'frequent_item[k][i]',frequent_item[k][i]
        count.append(0)
        tsupp=0
        for el in trans:
            tr_c=1
            for kk in  frequent_item[k][i]:
                if el[kk]<tr_c:
                    tr_c=el[kk]
            print 'tr_c: ',tr_c
            if tr_c: count[i]+=1
        print count[i]
        tsupp=(float) (count[i])/ (float)(transac) * 100
        print 'tsupp:',tsupp 


        #if tsupp>supp_min:
        tmp_supp.append(tsupp)
        #    print 'remain'
        """else:
            print 'del:',
            print k , i
            del count[i]
            del frequent_item[k][i]
            #print frequent_item[k]
            continue
        """
        i+=1  
    if tmp_supp!=[]:
        supp.append(tmp_supp)
    #print 'supp ',supp

    if k!= size: 
        

        t_gen_list=[]
        for p in range(len(frequent_item[k])):
            for ji in range(0,size):
                empty=True
                tmp_gen=[]
                for ii in range(len(frequent_item[k][p])):
                    tmp_gen.append(frequent_item[k][p][ii])

                tmp_gen.append(ji)
                if in_set(ji,frequent_item[k][p]) or in_sets(tmp_gen,t_gen_list):
                    empty=False
                
                if empty:
                    #print 'tmp_gen: ',tmp_gen , ' I :', ji
                    t_gen_list.append(tmp_gen)

        #print 't_gen_list ',t_gen_list
                    
        frequent_item.append(t_gen_list)
    
    
#print count
for k in range(len(frequent_item)-1):
    for i in range(len(frequent_item[k])):
        print supp[k][i],
    print ''



def get_sup(k):
    k_supp=list(k)
    k_supp.pop()

    for el in frequent_item[len(k_supp)-1]:
        tmp_set=[]
        tmp_set.append(el)
        if in_sets(k_supp,tmp_set):
            return supp[len(k_supp)-1][frequent_item[len(k_supp)-1].index(el)]

print_items(frequent_item)

### generate rules for virify
conf=[]
for k in range(2,len(frequent_item)-1):
    tconf=[]
    for i in range(len(frequent_item[k])):
        tconf.append(-1)
        tmp=frequent_item[k][i]
        #print i
        if supp[k][i]!=0 and get_sup(tmp)!=0:
            
            tconf[i]=supp[k][i]/get_sup(tmp)*100
    conf.append(tconf)

print conf

"""
def print_it(el):
    print '[',
    for  i in el:
        print i,
    print ']'

for k in range(2,len(frequent_item)-1):
    print_items(frequent_item)
    for i in range(len(frequent_item[k])):
        if conf[k-1][i]>conf_min:
            print 'rule: ' ,
            
            #print_it(frequent_item[k][i])
            print ' conf:',conf[k-1][i]
            
print_items(frequent_item)
"""
