print()
#fruit = {"Apple":3, "apple":5}
#print(fruit)
fruit = {}
def appleton(index):
    if index in fruit:
        fruit[index] += 1
        print(fruit)
    else:
        fruit[index] = 1
appleton('Apple')
appleton('apple')
appleton('Banana')
appleton('Apple')
print(fruit)
print()
print(len(fruit))
