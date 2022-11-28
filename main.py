count=0
for i in range(10):
    while i<3:
        if i==3:
            break
        count=count+10
        i=i+1
        count=count+1
else:
        count=count+20
print(count)