#solution of question 04 in information flow

#Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

def num_in_stock(fruit):
    if fruit == "apple":
        return 2
    elif fruit == "durian":
        return 4
    elif fruit == "pear":
        return 1000
    else:
        return 0
    
def main():
	fruit = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)
     


	
if __name__ == "__main__":
      main()	

