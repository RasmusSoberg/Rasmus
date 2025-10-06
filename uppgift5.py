array2 = ["potato", "carrot", "onion", "leek", "cabbage"]
print(array2[1])

print(array2[0],"-", array2[-1])

array1 = [47, 98, -13, 0, -412, 499, 3, 1200]


array3 = array1 + array2
print(array3)

array21 = array2
array21.sort()
print("ARRAY21",array21)

array11 = array1
array11.sort()
print(array11)


array22 = array2
print([word.upper() for word in array22])


array12 = array1
for negative in array12[:]:
    if negative < 0:
        array12.remove(negative)
        print(array12)


myArray = array1
temp = myArray[0]
myArray[0] = myArray[-1]
myArray[-1] = temp
print(myArray)


myArray[3] = False
myArray[4] = False
print(myArray)


