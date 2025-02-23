import random
# num=random.randint(1.5,3)
# print(num)

# num=random.randrange(1,3)
# print(num)

# num=random.random()
# print(num)

# num=random.uniform(1.5,1.6)
# print(num)

#list=[10,20,30,40,50]
# choice=random.choice(list)
# print(choice)

# random.shuffle(list)
# print(list)

#toss
"""toss=random.randint(0,1)
if(toss==1):
    print("Heads")
else:
    print("Tails")"""

#selecting an random name from the group to pay the bill

"""txt=input("Enter names of each person seperated by , :")
names=txt.split(",")
print(names)
import random
idx=random.randrange(0,len(names))
print(f"{names[idx]} need to pay the bill")"""

#adee
matrix=[['😄','😄','😄'],['😄','😄','😄'],['😄','😄','😄']]
pos=input("Enter a position where you want to hide money:")
row=int(pos[0])-1
col=int(pos[1])-1
matrix[row][col]='X'
print(matrix[0])
print(matrix[1])
print(matrix[2])


