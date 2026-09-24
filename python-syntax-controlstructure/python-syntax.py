def main():

    #if:
    note = int(input("Gebe eine Note von 1 - 5 ein:"))
    if note == 1:
        print("sehr gut")
    elif note == 2:
        print("gut")
    elif note == 3:
        print("befriedigend")
    elif note == 4:
        print("genügend")
    elif note == 5:
        print("nicht genügend")
    else: print("keine gültige Note!")

    #schleifen:
    arr = [1, 5, 2, 8, 2, 0, 3, 1]
    for i in range(len(arr)):
        print(arr[i])

    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1

    #break
    for i in range(1,101):
        if i % 7 == 0:
            print(i)
            break

    #pass
    for i in range(1,11):
        if i % 2 == 0:
            pass
        else:
            print(i)

    #try-except
    try: 
        num = int(input("Gebe eine Zahl ein:"))
        print(num/2)
    except ValueError:
        print("ungültige Eingabe!")



if __name__ == "__main__":
    main()
