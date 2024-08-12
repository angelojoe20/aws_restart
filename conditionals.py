#Exercise 1: Working with the if and else statement
userReply = input('Do you need to ship a package? (Enter Yes or No) ')

if userReply == 'yes':
    print("We will ship you the package!")
else:
    print("We will not you ship you the packages.")
    
print('')

# Exercise 3: Working with the elif statement    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

