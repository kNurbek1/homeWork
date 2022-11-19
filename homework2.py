#Задание 1
stringList = ['Warner', 'brothers', 'pictures']
stringResultOne = ""
stringResultTwo = ""
stringResultThree = stringList[2][::-1]
for x in stringList:
    stringResultOne = stringResultOne + x + " "
    if "bro" in x:
        stringResultTwo = x[0:3]
print(stringResultOne)
print(stringResultTwo)
print(stringResultThree)

#Задание 2
givenList = ['Шалаш', 'А роза упала на лапу Азора', 'abcdxyz']
def validator(argument, original):
    lowerArgument = argument.lower()
    reversedArgument = lowerArgument[::-1]
    if lowerArgument == reversedArgument:
        print(f'{original} - полиндром')
    else:
        print(f'{original} - не полиндром')

for x in givenList:
    replaced = x.replace(' ', '')
    validator(replaced, x)