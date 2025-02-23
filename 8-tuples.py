# tuple1=(10,20,30,40,40,60)
# print(tuple1)

# (*marks1,marks2)=tuple1
# print(marks1)
# print(marks2)

# tuple1=(1,2,3)
# tuple2=(10,20,30)
# tuple3=tuple1*tuple2
# print(tuple3)

# list1=[1,2,3,7,8,9]
# list2=[4,5,6]
# zipped=tuple(zip(list1,list2))
# print(zipped)

# names=("sai","siva","nadeem")
# ages=(20,19,18)
# persons=list(zip(names,ages))
# print(persons)

# for name,age in persons:
#     print(f"{name} is {age} years old")


# list=[["a",1],["b",2],["c",3]]
# list=[["a",1],"b","c"]
# for x,y in list:
#     print(f"value of {x} is:{y}")

# tuple=(10,20,(30,40),50)
# if 30 in tuple:
#     print("Yes Item exists")
# else:
#     print("No item doesnt exists")

# tuple=(10,20,30,40,50,10,20)
# list=list(tuple)
# print(list)

list=(10,20,30,40,50,10,20)
value=10
seen=set()
newList=[]
for x in list:
    if x==value:
        if x not in seen:
            newList.append(x)
            seen.add(x)
    else:
        newList.append(x)
print(newList)











