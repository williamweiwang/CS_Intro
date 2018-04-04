
# coding: UTF-8

# In[12]:

Last = 0
Current = 1
f=False
n=1
p=input('Please input a number you want to search')
while (Current < int(p)):
    #print(Current)
    n+=1
    Temp = Last
    Last = Current
    Current = Last + Temp
    if(Current==int(p)):
        print(p+' is a Fibonacci number, and it is '+str(n)+'th number')
        f=True
        break
if not f:
    print(p+' is not a Fibonacci number')


# In[ ]:



