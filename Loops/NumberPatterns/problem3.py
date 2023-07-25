rows = int(input())
p=rows
for i in range(1 ,rows+1):   
    for j in range(i,rows+1):
        print(p ,end=" ")
        
    print()
    p=p-1