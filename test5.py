#This code was written to calculate all positive numbers
given_list3=[7,5,4,4,3,1,-2,-3,-5,-7]
total6=0
i=len(given_list3) - 1
while given_list3[i] < 0:
    total6 += given_list3[i]
    i-=1
print(total6)