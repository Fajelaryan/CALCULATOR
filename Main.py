import Calculator as cal
import PythagoreanTheorem as pytha

# Main
def MAIN():
    while True:
        print("================================")
        print("=CUMPUTE TO PASS =")
        print("= In Basic Math =")
        print("================================")
        print("\t 1. CALCULATOR")
        print("\t 2. Pythagorean Theorem Calculator")
        print("\t 3. EXIT")
        try:
            choice = int(input("===>"))
            if choice == 1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                print(" ")
                cal.Calculator.calcu()
            elif choice == 2:
                print(" ")
                pytha.Pythagorean.pythagorean()
            elif choice == 3:
                exit()
            else:
                print("Invalid Input ")
        except ValueError as err:
                print(" ===================================================")
                print("| "+ str(err) +" |")
                print("| PUT a Number not a LETTER or SYMBOL           |")
                print(" ===================================================")
MAIN()