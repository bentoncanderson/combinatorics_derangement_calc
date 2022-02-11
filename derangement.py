def derangement(d):
    if (d < 2):
        print("Invalid input.")
    elif (d % 2 == 0):
        num = 1
    else:
        num = -1
    if d == 2:
        return 1
    else:
        return d * derangement(d-1) + num



print(derangement(2))