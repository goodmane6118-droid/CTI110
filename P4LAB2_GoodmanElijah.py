

while True:
    
    num = int(input("Enter an integer: "))
    
    if num < 0:
        print("Cannot accept negative values.")
    else:
      
        print(f"Multiplication table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    
    
    user_response = input("Do you want to run the program again? (yes/no): ")
    
    
    while user_response.lower() == "no":
        print("Exiting program. . . ")
        user_response = "end"
        exit()





