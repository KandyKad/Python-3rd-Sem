for r in range(7) :
    for c in range(7):
        if r==0 or r==6 or c==(6-r):
            print("*", end="")
        else:
            print(end=" ")
    print()
