angry = False
bored = True
hungry = True
tired = False

if angry == True and hungry == True and bored == True:
    print("T-Rex will eat the Triceratops")
elif tired == True and hungry == True:
    print("T-Rex will eat the Iguanadon")
elif hungry == True and bored == True:
    print("T-Rex will eat the Stegasaurus")
elif tired == True:
    print("T-Rex will go to sleep")
elif angry == True and bored == True:
    print("T-Rex will fight Velociraptor")
else:
    print("T-Rex gives a toothy smile")
    