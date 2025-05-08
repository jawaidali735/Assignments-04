
C = 299792458 # constant of value of light of speed

def main():

    mass_value = float(input("Enter kilos of mass: "))

    e = mass_value * (C**2) # formula to calculate

    print("Formula to calculate mass-energy: " + "e = m * C^2...")
    print("Mass value in kg: " + "m = " + str(mass_value) + " kg")
    print("Constant value: "+"C = " + str(C) + " m/s")

    print(f"\n{e} joules of energy!")

if __name__ == '__main__':
    main() 