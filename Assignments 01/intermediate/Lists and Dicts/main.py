


def create_fruit_list():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Initial fruit list:", fruit_list)
    print("Length of fruit list:", len(fruit_list))
    
    fruit_list.append('mango')
    print("Updated fruit list:", fruit_list)
    return fruit_list

def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Changed '{old_value}' to '{new_value}'."
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Start or end index out of range."

def main():
    fruit_list = create_fruit_list()
    
    while True:
        print("\nChoose an operation: access / modify / slice / quit")
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'access':
            index = int(input("Enter index to access: "))
            print(access_element(fruit_list, index))
        
        elif choice == 'modify':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(fruit_list, index, new_value))
            print("Updated list:", fruit_list)
        
        elif choice == 'slice':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(fruit_list, start, end)
            print("Sliced list:", result)
        
        elif choice == 'quit':
            print("Thanks for playing with the fruit list!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
