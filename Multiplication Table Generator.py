# --- Task 3: Multiplication Table Generator ---

print("Multiplication Table Generator")
print("-------------------------------")

# A 'while' loop keeps the whole program running for multiple sessions
while True:
    try:
        # 1. Get User Input
        user_input = input("\nEnter a number (or type 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        number = int(user_input)
        table_range = int(input("Enter the range (e.g., up to 10 or 12): "))

        print(f"\nMultiplication Table for {number}:")
        print("-" * 25)

        # 2. The 'for' loop generates the actual table
        # range(1, table_range + 1) starts at 1 and stops exactly at the range
        for i in range(1, table_range + 1):
            result = number * i
            
            # Simple formatting for the output
            output = f"{number} x {i} = {result}"
            
            # Bonus: Highlight multiples of 5 or 10
            if result % 5 == 0 or result % 10 == 0:
                output += " (* Multiple of 5/10 *)"
                
            print(output)

        print("-" * 25)

    except ValueError:
        print("Error: Please enter valid whole numbers.")