my_fruit = "pear"
match my_fruit:
    case "banana": 
        print("The banana is yellow")
    case "apple":
        print("The apple is green")
    case "kiwi":
        print("The kiwi is green")
    case "plum":
        print("The plum is purple")
    case _:
        print("This is an unknown fruit")

cnt = 481
for cnt in range(481,541,6):
    print (cnt, " + 6 " , cnt)

cnt = 551
for cnt in range(551, 471, -8):
    print (cnt, " - 8 = ", cnt)

for num in range(22,46,2):
    if num <44:
        print(num, ", ", end="")
    else:
        print(num)

count = 10
li = 0
while count < 481:
    count += 6
    li += 1
    print (li,",", count)
    


count = 551
li = 0

while count >= 0:
    count -= 8
    li += 1
    print(li, count)

numbers = []
i = 28

while i <= 63:
    if i % 5 == 0 or i % 7 == 0:
        numbers.append(str(i))
    i += 1

print(", ".join(numbers))