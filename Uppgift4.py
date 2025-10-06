def sum(x, y):
    i = []
    total = 0
    
    for i in range (x,y):
        i.append(i)
    
    for number in i: 
        total = total + number
    
    print ("LIST: ",i)
    print("TOTAL: ",total)
sum(10,20)



def fruitColors(fruit):
    colors = {
        "banana":"yellow",
        "apple": "green"
    }
    return colors.get(fruit)
print (fruitColors("banana"))



def startStop(rangeStart,rangeStop):
    i = []
    for i in range(rangeStart,rangeStop + 1):
        i.append(i)
    print(i)
startStop(10, 15)


def startStopDown(rangeStart,rangeStop):
    i = []
    
    for i in range(rangeStart,rangeStop + 1):
        i.append(i)
            
    print(i[::-1])
startStopDown(10, 20)


def startStopUpAndDown(rangeStart,rangeStop):
    i = []
    
    for i in range(rangeStart,rangeStop + 1):
        i.append(i)

    print("ASCENDING: ", i)        
    print("DECENDING: ", i[::-1])
    
startStopUpAndDown(10, 20)


def repeater(string, times):
    print(string * times)
repeater("Hello ", 3)

def middlePoint(x,y):
    i = []
    for i in range(x,y):
        i.append(i)
    print(i)
    
    middle = len(i)

    if middle % 2 == 1:
        print("MIDDLE", i[middle // 2])
    else:
        print("NO EXACT MIDDLE")

middlePoint(0, 22 + 1)



def fizzBuzz(start, stop):
    
    if start >= stop:
        print("ERROR:START IS BIGGER THAN STOP")
    
    numbers = []
    for i in range(start, stop):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("FizzBuzz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        else:
            numbers.append(str(i))
    print(", ".join(numbers))

fizzBuzz(40, 15 + 1)



def blackJack(a , b, c, x, y, z ):

    playerCards = a, b, c
    dealerCards = x, y, c

    playerSum = a + b + c
    dealerSum = x + y + c

    playerStatus = f" {playerCards} : {playerSum}"
    dealerStatus = f"{dealerCards} : {dealerSum}"
    
    print(playerStatus)
    print(dealerStatus)
    
    if playerSum > 21:
        statusP = (" BUST")
    elif playerSum < 21:
        statusP = (" SAFE")
    elif playerSum == 21:
        statusP = (" BLACKJACK")

    if dealerSum > 21:
        statusD = " BUST"
    elif dealerSum < 17:
        statusD = " SAFE"
    elif dealerSum > 17 and dealerSum < 21:
        statusD = " STOP"
    elif dealerSum == 21:
        statusD = " BLACKJACK"
    print (f"Player:{statusP},{playerSum} Dealer:{statusD},{dealerSum}")

blackJack(8, 10, 3, 9, 6, 11)



def interst(startmoney, years, percent):
    return round(startmoney * (1 + percent/100) ** years, 4)


print (interst(840, 5, 5,))
