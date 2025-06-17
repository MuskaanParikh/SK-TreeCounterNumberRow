userInput=int(input("Enter a number to see a tree: "))

for i in range(1, userInput+1): 
    lineOfStar=""
    for j in range(i):
        lineOfStar=lineOfStar+ str(i)
    print(lineOfStar)
