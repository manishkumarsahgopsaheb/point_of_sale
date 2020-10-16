
with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

# print(currencyDict)
amount = int(input("Enter Amount:\t"))
print("\n\nChoose the name of currency you want to convert this amount? Available Options are:\n")
# print([print(item) for item in currencyDict.keys()])
for item in currencyDict.keys():
    print(item)

choice = input("\nChoice is: ")
print(f'\n\n{amount} INR is equal to {amount*float(currencyDict[choice])} {choice}')
