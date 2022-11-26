


a = ''
b = []


for i in range (100,999):
    for j in range(100,999):
        a = str(i*j)
        


        if a[::1]==a[::-1] and len(a) == 6:
            b.append(a)
            b.sort(reverse=True)
print(b[0]) 









        



