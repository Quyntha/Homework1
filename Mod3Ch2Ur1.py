l = [1,4,1,6,'Hello','a',5,'Hello']
a = []    
    

for i in range(0, len(l)):   
    for j in range(i+1, len(l)):   
        if(l[i] == l[j]):   
            a.append(l[j])
print(a)