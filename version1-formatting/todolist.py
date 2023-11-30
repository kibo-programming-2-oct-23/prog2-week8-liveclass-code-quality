def menu():
    print("1. Add a thing")
    print("2. Show things")
    print("3. Remove a thing")
    print("4. Stop")
    print()

def add(x):
    y = input("Enter a thing: ")
    x.append(y)

def show(x):
    if x:
        for i, y in enumerate(x, 1):
            print(f"{i}. {y}")
    else:
        print("List is empty.")

def remove(x):
    num = int(input("Enter number to remove: "))
    if 0 < num <= len(x):
        x.pop(num - 1)
    else:
        print("Wrong number.")

def start():
    lst = []
    while True:
        menu()
        opt = input("Pick an option: ")

        if opt == "1":
            add(lst)
        elif opt == "2":
            show(lst)
        elif opt == "3":
            remove(lst)
        elif opt == "4":
            print("Bye!")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    start()
