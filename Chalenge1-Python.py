tab=[]
a=int(input())
str_number = input()
for j in str_number:
    if j != ' ':
        tab.append(int(j))
tab.sort()
print(tab[-1]*tab[-2])
        
