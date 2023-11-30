def menu():
    print("1. Add a thing\n2. Show things\n3. Remove a thing\n4. Stop")
    print()


def add(x):
    y = input("Enter a thing: ")
    x.append(y)


def show(x):
    if x:
        for i,y in enumerate(x, 1):
            print(f"{i}. {y}")
    else:
        print("List is empty.")
        #pass


def remove(x):
    num = int(input("Enter number to remove: "))
    if 0 < num <= len(x):
      x.pop(num - 1)
    else:
      print("Wrong number.")
#           pass
# def remove(x):
    #     num = int(input("Enter number to remove: "))
    #     if 0 < num <= len(x):
    #       x.remove(num - 1)
    #     else:
#       print("Wrong number.")
# #           pass
def start():
    lst=[]
    while True:
      menu()
      opt = input("Pick an option: ")
      if opt=="1":
          add(lst)
      elif opt=="2":
        show(lst)
      elif opt=="3":
          remove(lst)
      elif opt=="4":
          print("Bye!")
          break
      else:
          print("Wrong choice. Try again.")
# for x in range(0, 5):
#     ??
if __name__ == "__main__":
    start()
