
# coding: utf-8

# In[16]:

num = input('Type the number: ') # num是⼀個字串
numlist = list(num) # numlist是由字元組成的list
checklist = [True for i in range(10)] # 長度為10、值都是True的list
f=True
if len(numlist) != 10:
    print('Illegal input: wrong length')
    f=False
    exit(1)
for i in numlist:
    if not i.isdigit():
        print('Illlegal input: ', i, 'is not a digit')
        exit(2)
        f=False
    else:
        checklist[int(i)] = False
if (any(checklist))and(len(numlist) == 10):
    print('Illegal input: repeated digit')
    f=False
    exit(3)
if num=='9876543210':
    f=False
    print('9876543210 is the max number in length of 10 digits')

p=int(num)
p=p+1 # num是⼀個字串
while(f):
    num=str(p)
    numlist = list(num) # numlist是由字元組成的list
    checklist = [True for i in range(10)] # 長度為10、值都是True的list
    if len(numlist) != 10:
        print('Illegal input: wrong length')
        exit(1)
    for i in numlist:
        if not i.isdigit():
            print('Illlegal input: ', i, 'is not a digit')
            exit(2)
        else:
            checklist[int(i)] = False
    if any(checklist):
        #print('Illegal input: repeated digit')
        p=int(num)
        p=p+1 # num是⼀個字串
    if any(checklist)==False or len(numlist) != 10:
        break

if(p>9876543210 and f):
    print('no such rearrangement exists '+num)
elif(f):
    print('the next larger value = '+num)
else:
    print('請重新執行並輸入')


# In[ ]:



