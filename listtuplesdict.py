#Defining a list
myFruitlist = ['apple', 'banana', 'cherry']
print(myFruitlist)
print(type(myFruitlist))

#Accessing a list by position
print(myFruitlist[0])
print(myFruitlist[1])
print(myFruitlist[2])

print('')

#Changing the values in a list
myFruitlist[2] = 'orange'
print(myFruitlist)

#Exercise 2: Introducing the tuple data type
#Defining a Tuple
myFinalAnswerTuple = ('apple', 'banana', 'pineapple')
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print('')

#Accessing a dictionary by name
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
