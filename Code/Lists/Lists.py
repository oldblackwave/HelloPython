list = [1,2,3,4,5,6,7,8,9,10,11,12]

print(list[5])
print(list[-3])
print(len(list))

print(list[2:10])
print(list[2:10:2])
print(list[2::2])

list2 = [15,16]

list.append(13)
list.extend(list2)

list.insert(5, 56)
list[4] = 33

list[2] = list[2] * 8

print(list)

del list[5:7]

list.remove(15)

list.reverse()


print(list)


list3 = [2,3,4,1,5]

list4 = sorted(list3)

list3.sort()

print(list3)
print(list4)