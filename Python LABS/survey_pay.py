# Calculate time it takes to earn

while True:
    try:
        Earning_daily = int(input("What is the daily earning: "))
        Expected_amount = int(input("What is your desired earning amount: "))

#Catch TypeError
        break  # Exit the loop if both inputs are valid integers
    except ValueError:
        print("Invalid input. Please enter integers for daily earning and desired amount.")

Time_taken = int(Expected_amount / Earning_daily) 
print ("It will take approximately", Time_taken, "days.")



