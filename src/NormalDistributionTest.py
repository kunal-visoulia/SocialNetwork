#How Do Normal Distribution Appear?
import matplotlib.pyplot as plt
import random
possiblesums=[x for x in range(10,1001)]
sum1=[]
j=0
while(j<991):
    i=0
    list1=[]
    while(i<10):
        list1.append(random.randint(1,100))
        i+=1
    j+=1
    sum1.append(sum(list1))
list2=[]
for x in range(10,1001):
    c=0
    for j in range(0,991):
        if sum1[j]==x:
            c+=1
    list2.append(c)
plt.plot(possiblesums,list2)
plt.show()