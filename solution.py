userInput=int(input("Enter a number to see a tree: "))
counter=1

while(counter<=userInput):
    starCounter=1
    while(starCounter<=counter):
        print(counter, end="")
        starCounter=starCounter + 1
       
    counter=counter+1
    print("")
