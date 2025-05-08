#Write a function that takes a list of numbers and returns the sum of those numbers.


def add_numbers(nums):
    
   
    total_num = 0
    for i in nums:
        
        total_num += i
    return total_num


def main():
    nums = [1,2,3,4,5,7,8]
    sum = add_numbers(nums)

    print(sum)


if __name__ == '__main__':
    main()