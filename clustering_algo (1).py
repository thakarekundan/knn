from math import sqrt
l1=[185,170,168,179,182,188]
l2=[72,56,60,68,72,77]
 
cluster1=[185,72]
cluster2=[170,56]
ans=[]
for i in range(len(l1)):
    ans.append([sqrt(((cluster1[0]-l1[i])**2)+((cluster1[1]-l2[i])**2)),sqrt(((cluster2[0]-l1[i])**2)+((cluster2[1]-l2[i])**2))])


print(ans)
ans1=dict()
j=-1
for i in ans:
    j=j+1
    if i[0]<i[1]:
        ans1[j]=1
    else:
        ans1[j]=2
    
        
print(ans1)
