
# coding: utf-8

# In[2]:

#以下程式來自https://openhome.cc/Gossip/AlgorithmGossip/HanoiTower.htm#Python網站上的資源

def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)

n = input("請輸入整數：")
for move in hanoi(int(n), 'A', 'B', 'C'):
    print("盤由 %c 移至 %c" % move)


# In[ ]:



