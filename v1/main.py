# Importing libs
import secrets

# Get input
inputFile = open("input.txt", 'r')
allPeople = []
for line in inputFile:
    allPeople.append(line.strip("\n").split(", "))

# Get random choices
print("There are {0} people in total.".format(len(allPeople)))
while True:
    try:
        numberOfPeople = int(input("How many people do you want to draw? "))
        break
    except:
        pass

finalPeople = []
for i in range(numberOfPeople):
    finalPeople.append(allPeople.pop(allPeople.index(secrets.choice(allPeople))))  ### Write custom function later to tidy up code

# Print output
print("")
for person in finalPeople:
    print("{person}: {reason} - {who}".format(person=person[0], reason=person[1], who=person[2]))
print("\nDone!")
# Save output
outputFile = open("output.txt", 'w')
for person in finalPeople:
    outputFile.write("{person}: {reason} - {who}\n".format(person=person[0], reason=person[1], who=person[2]))
outputFile.close()

# Infinite loop to keep program running
while True: pass
