for i in range(7):
    if i<4:
        for j in range(5):
            if (i%3==0 and j != 0 and j!=4)or(i%3 != 0 and j==0):
                print("*", end="")
            else:
                print(end=" ")
        print()
    else:
        for k in range(5):
            if (i==6 and k != 4)or(i!=6 and k==4):
                print("*", end="")
            else:
                print(end=" ")
        print()

