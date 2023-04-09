#Answer Q1
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]

# Loop through each character name in the list
for name in disney_characters:
    # Check if the name contains "u"
    if "u" in name:
        print(name + " U are so Uniquely U!")
    # Check if the name contains "i"
    elif "i" in name:
        print(name + " I bet you're Impressively Intelligent!")
    # Check if the name contains "o"
    elif "o" in name:
        print(name + " O My! How Original!")
    # Default case
    else:
        print(name + " Ehh, a's and e's are so ordinary.")


#Answer Q2
temperature = 90

while temperature > 75:
    print(f"Temperature is {temperature} - crank the AC!")
    temperature -= 3
print(f"{temperature}. Ahh, that's better")