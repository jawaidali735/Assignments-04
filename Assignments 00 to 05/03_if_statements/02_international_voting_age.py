#Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
#Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:
#the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
#the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
#the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)
#Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.


voting_age_in_Peturksbouipo = 16
voting_age_in_Stanlau = 25
voting_age_in_Mayengua = 48 

def main():

    age = int(input("Enter your age: "))

    if age >= voting_age_in_Peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {voting_age_in_Peturksbouipo}.")
    else:
         print(f"You can not vote in Peturksbouipo where the voting age is {voting_age_in_Peturksbouipo}.")


    if age >= voting_age_in_Stanlau:
        print(f"You can vote in Peturksbouipo where the voting age is {voting_age_in_Stanlau}.")
    else:
         print(f"You can not vote in Peturksbouipo where the voting age is {voting_age_in_Stanlau}.")
    

    if age >= voting_age_in_Mayengua:
        print(f"You can vote in Peturksbouipo where the voting age is {voting_age_in_Mayengua}.")
    else:
         print(f"You can not vote in Peturksbouipo where the voting age is {voting_age_in_Mayengua}.")


if __name__ == "__main__":
    main()
    
