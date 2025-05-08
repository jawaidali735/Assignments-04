#solution of question 04 in information flow

def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")

    return first_name , last_name , email_address

def main():

    data = get_user_info()
    print(f"Here is the data: {data}")


if __name__ == "__main__":
    main()