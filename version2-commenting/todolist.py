# Define a function to display the menu
def menu():
    # Printing the menu options
    print("1. Add a thing")  # Option to add a task
    print("2. Show things")  # Option to show all tasks
    print("3. Remove a thing")  # Option to remove a task
    print("4. Stop")  # Option to exit the program
    print()  # Print a blank line for better readability

# Define a function to add a task to the list
def add(x):
    y = input("Enter a thing: ")  # Prompt the user to enter a task
    x.append(y)  # Add the entered task to the list

# Define a function to show all tasks in the list
def show(x):
    if x:  # Check if the list is not empty
        for i, y in enumerate(x, 1):  # Loop through each task in the list
            print(f"{i}. {y}")  # Print each task with its number
    else:
        print("List is empty.")  # Inform the user if the list is empty

# Define a function to remove a task from the list
def remove(x):
    num = int(input("Enter number to remove: "))  # Ask the user for the task number to remove
    if 0 < num <= len(x):  # Check if the entered number is valid
        x.pop(num - 1)  # Remove the task from the list
    else:
        print("Wrong number.")  # Inform the user if the entered number is invalid

# Define the main function to run the program
def start():
    lst = []  # Initialize an empty list to store tasks
    while True:  # Start an infinite loop to continuously run the program
        menu()  # Display the menu
        opt = input("Pick an option: ")  # Ask the user to pick an option

        # Check the user's choice and call the appropriate function
        if opt == "1":
            add(lst)  # Call the add function to add a task
        elif opt == "2":
            show(lst)  # Call the show function to display all tasks
        elif opt == "3":
            remove(lst)  # Call the remove function to delete a task
        elif opt == "4":
            print("Bye!")  # Print goodbye message and
            break  # Exit the loop to end the program
        else:
            print("Wrong choice. Try again.")  # Inform the user of an invalid choice

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    start()  # Call the start function to run the program
