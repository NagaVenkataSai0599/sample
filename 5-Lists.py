#lists
marks=[74,92,23,83,87,69,98,15]
print(marks)
marks.append(10)
print(marks)
marks.extend([27,94,76])
print(marks)
marks.sort(reverse=True)
print(marks)
marks.insert(7,66)
print(marks)
marks.insert(9,[64,55,43,35])
print(marks)
popped=marks.pop(9)
print(popped)
idx=marks.index(27)
print(idx)
print(marks)
marks[10]=24
print(marks)
#print(marks[7:9])
marks[7:9]=[64,55]
print(marks)
marks[7:9]=[66,69,43,35]
print(marks)
marks[7:9]=[64]
print(marks)
marks[7:9]=[]
print(marks)
#print(marks.index(35))
marks[7:7]=[66,69]
print(marks)
marks.sort(reverse=True)
print(marks)
#print(marks.index(35))
marks.insert(9,[63,55,41])
print(marks)
marks[9][2:2]=[53,50,49,45]
print(marks)
del marks[9][2:2+4]
print("marks:",marks)
#marks1=list(marks)
marks1=marks.copy()
print("marks1:",marks1)
marks[1]=95
print("marks:",marks)
print("marks1:",marks1)
# del marks1[:]
marks1.clear()
print(marks1)
# marks[]
print(marks.index(66))
marks[8:8]=[92,83,74,98]
print(marks)
print(marks[6:].count(98))
print(marks.index(83))
print(marks[1:5])
print(marks)
#marks.remove(100)
# marks.pop(20)
print(marks)
print(marks.index(35))
#marks.pop([14:])
del marks[14:]
print(marks)
pop=marks.pop()
print(pop)
print(marks)
marks2=marks.copy()
print(marks2)
del marks2
# print(marks2)

#sort lists
print("sort list...")
def sorting(n):
    return n-80
marks.sort(reverse=True,key=sorting)
print(marks)

#copying a list
print("copying a list")
marks10=marks
marks10[2]=94
print(marks10)
print(marks)
scores=[10,20]*5
print(scores)



