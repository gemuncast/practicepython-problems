#two player play rock paper scissors, display who is the winner
#1- rock : 1
#2- paper : 2
#3- scissor : 3

while True:
    p1 = int(input("P1 : ")) 
    p2 = int(input("P2 : "))
    if p1 == 1 and p2 == 3:
        print("p1 wins")
        break
    elif p1 == 2 and p2 == 1:
        print("p1 wins")
        break
    elif p1 == 3 and p2 == 2:
        print("p1 wins")
        break
    elif p2 == 1 and p1 == 3:
        print("p2 wins")
        break
    elif p2 == 2 and p1 == 1:
        print("p2 wins")
        break
    elif p2 == 3 and p1 == 2:
        print("p2 wins")
        break
    else :
        print("Draw!!!")