
import math

class Pythagorean:
    

    def side_c(side_a,side_b):
        answer = math.sqrt((side_a*side_a)+(side_b*side_b))
        print("Answer: sqrt("+ str(side_a) + " * " + str(side_a) + ") + (" +str(side_b) + " * " + str(side_b)+") = " +str(answer) + "      |")
    # end def

    def side_a(hypo_c, side_b):
        answer = math.sqrt((hypo_c * hypo_c) - (side_b * side_b))
        print("Answer: sqrt("+ str(hypo_c) + " * " + str(hypo_c) + ") - (" +str(side_b) + " * " + str(side_b)+") = " +str(answer) + "      |")
        
    # end def

    def side_b(hypo_c,side_a):
        answer = math.sqrt((hypo_c * hypo_c - side_a * side_a))
        print("Answer: sqrt("+ str(hypo_c) + " * " + str(hypo_c) + ") - (" +str(side_a) + " * " + str(side_a)+") = " +str(answer) + "      |")
        
    # end def
    def pythagoreanMENU(): 
        while True:
            print(" ")
            print("==============================================================================================")
            print("Pythagorean theorem calculator! Calculate your triangle sides.")
            print("Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle")
            print("==============================================================================================")
            print(" ")
            CHOICE.fomula()
            
            
class CHOICE(Pythagorean):   
    def fomula():
        try:
            formula = input("Which side (a, b, c) do you wish to calculate? side -> ")
            if formula == 'c' or formula == 'C':
                print("========================================================") 
                side_a = int(input("Input the length of side a: "))
                side_b = int(input("Input the length of side b: "))
                print("The length of Hypotenuse c is: " )
                Pythagorean.side_c(side_a,side_b)
                print("========================================================")
                        
            elif formula == 'a' or formula == 'A':
                print("========================================================")
                hypo_c = int(input("Input the Hypotenuse c: "))
                side_b = int(input("Input the length of side b: "))
                print("The length of side a is: " )
                Pythagorean.side_a(hypo_c,side_b)
                print("========================================================")
                print()

            elif formula == 'b' or formula == 'B':
                print()
                print("========================================================")
                hypo_c = int(input("Input the Hypotenuse c: "))
                side_a = int(input("Input the length of side a: "))
                print("The length of side b is: " )
                Pythagorean.side_b(hypo_c,side_a)
                print("========================================================")
                print()
                
            elif formula == 'r' or formula == 'R':
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
                print()
                print(" ===================================================")
                print("| "+ str(err) +" |")
                print("| PUT a Number not a LETTER or SYMBOL           |")
                print(" ===================================================")
                print()
    #end def
                
pytho = Pythagorean()
pytho.pythagoreanMENU