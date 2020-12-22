import random


L1 = []
L2 = []

# generate L1 and L2 with random numbers 
for i in range(0,5):
    rand_1 = random.randint(1,9)
    rand_2 = random.randint(1,9)

    L1.append(rand_1)
    L2.append(rand_2)

# sort L1 and L2
L1.sort()
L2.sort()
_L1 =[]
_L2 =[]

L1_holder = [] # hold the reast of L1 after get rid of dubilcate 
for i in range(len(L1)-1): 
    if L1[i]==L1[i+1]: 
        _L1.append(L1[i]) 
        _L1.append(L1[i+1]) 
    else : 
        L1_holder.append(L1[i]) 

L2_holder = [] # hold the reast of L1 after get rid of dubilcate 
for i in range(len(L2)-1): 
    if L2[i]==L2[i+1]: 
        _L2.append(L2[i]) 
        _L2.append(L2[i+1]) 
    else : 
        L2_holder.append(L2[i]) 


L1_holder.extend(L2_holder)
L1_holder.sort()

_L1.extend(_L2)
_L1.sort()

print(L1)
print(L2)

print(L1_holder)

