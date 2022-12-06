
class Calculator():
    def add(a, b):
        answer = a + b
        print("| Answer: "+ str(a) + " + " + str( b) + " = " + str(answer)+"     |")
            
    def sub(a, b):
        answer = a - b
        print("|Answer: "+ str(a) + " - " + str(b ) + " = " + str(answer) + "    |")
        
    def mul(a, b):
        answer = a*b
        print("Answer: "+ str(a) + " * " + str(b) + " = " + str(answer) + "      |")
        
    def div(a, b):
            answer = a / b
            print("Answer: "+ str(a) + " / " + str(b) + " = " + str(answer) + "      |")
            
    def calcu():   
        while True:
            print()
            print("=======================================")
            print("=     DIFFERENT TYPES OF CALCULATOR   =")
            print("=======================================")
            print("A. Addition")
            print("B. Subtraction")
            print("C. Multiplication")
            print("D. Division")
            print("E. Exit")
            try:
                choice = str(input("input your choice: "))
                if choice == "a" or choice == "A":
                    print("================================")
                    print("Addition                        ")
                    a = int(input("Input first number:     "))
                    b = int(input("Input second number:    "))
                    print("================================")
                    Calculator.add(a, b)
                    print("================================")
                    
                    
                elif choice == "b" or choice == "B":
                    print("================================")
                    print("Subtraction                        ")
                    
                    a = int(input("Input first number:     "))
                    b = int(input("Input second number:    "))
                    print("================================")
                    Calculator.sub(a, b)
                    print("================================")
                    
                
                elif choice == "c" or choice == "C":
                    print("================================")
                    print("Multiplication                        ")
                    
                    a = int(input("Input first number:     "))
                    b = int(input("Input second number:    "))
                    print("================================")
                    Calculator.mul(a, b)
                    print("================================")
                    
                
                elif choice == "d" or choice == "D":
                    print("================================")
                    print("Dvision                        ")
                    
                    a = int(input("Input first number:     "))
                    b = int(input("Input second number:    "))
                    print("================================")
                    Calculator.div(a, b)
                    print("================================")
                    
                elif choice == "e" or choice == "E":
                    exit()
         
                else:
                    print(" ============================")
                    print("| INVALID INPUT              |")
                    print(" =============================")
            except ValueError as err:
                    print(" ===================================================")
                    print(err)
                    print("| PUT a Number not a LETTER or SYMBOL")
                    print(" ===================================================")
 