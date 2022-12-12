import Calculator as cal
import PythagoreanTheorem as pytha

# Main
class MAIN:
    
    def mainMENU(self):
            print("================================")
            print("=       CUMPUTE TO PASS        =")
            print("=        In Basic Math         =")
            print("================================")
            print("\t1. CALCULATOR")
            print("\t2. Pythagorean Theorem Calculator")
            print("\t3. EXIT")
            MAIN.choice(self)
        
    
    def choice(self):
        try:
                choice = int(input("===>"))
                if choice == 1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                    print(" ")
                    cal.Calculator.calcuMENU()
                elif choice == 2:
                    print(" ")
                    pytha.Pythagorean.pythagoreanMENU()
                
                elif choice == 3:
                    exit()
                else:
                    try:
                        print(" ========================================")
                        print("|       PUT A CORRECT CHOICE NUMBER     |")
                        print(" ========================================")
                    except ValueError as err:
                        print(" ===================================================")
                        print("| "+ str(err) +" |")
                        print("| PUT a Number not a LETTER or SYMBOL           |")
                        print(" ===================================================")
                        
        except ValueError as err:
            print(" ===================================================")
            print("| "+ str(err) +" |")
            print("| PUT a Number not a LETTER or SYMBOL           |")
            print(" ===================================================")
        
    # end def
main = MAIN()
main.mainMENU()