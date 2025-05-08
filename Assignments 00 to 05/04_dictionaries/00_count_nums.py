#ans of question 1

def get_numbers():

    user_numbers = []

    while True:
        user_input = input("Enter your number: ")

        if user_input == "":
            break
       
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers


def get_dic(lst):

    num_dic = {}

    for num in lst:
        if num not in num_dic:
            num_dic[num] = 1
        else:
            num_dic[num] += 1
    return num_dic


def print_counts(num_dict):
  
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():

    user_numbers = get_numbers()
    num_dic = get_dic(user_numbers)

    print_counts(num_dic)

if __name__ == "__main__":
    main()