# Expense Calculator
# Calculates how much each person has to pay for shared flat expenses.

print("\n===== Expense Calculator =====")

# Inputs (using float for accurate money calculation)
Rent = float(input("Enter the Flat Rent = "))
Grocery = float(input("Enter the Grocery Amount = "))
Water_Bill = float(input("Enter the Total Water Bill Amount = "))
Electricity_Units_Spend = float(input("Enter the Total Electricity Units Spent = "))
Charge_per_unit = float(input("Enter the Charge per Unit = "))
Persons = int(input("Enter the Number of Persons Living In Flat = "))

     # Error handling for zero persons
if Persons == 0:
        print("Number of persons cannot be zero. Please try again.")
else:

    # Electricity bill calculation
 Total_Electricity_Bill = Electricity_Units_Spend * Charge_per_unit

          # Total expense calculation
Total_Expense = (Rent + Grocery + Water_Bill + Total_Electricity_Bill) 
Amount_Per_Person = Total_Expense / Persons


        # Expense breakdown
print("\n----- Expense Breakdown -----")
print("Rent:", Rent)
print("Grocery:", Grocery)
print("Water Bill:", Water_Bill)
print("Electricity Bill:", Total_Electricity_Bill)
print("Total Expense:", Total_Expense)

            # Final output
print("\nEach person has to pay = ", Amount_Per_Person)

     # Save to file
with open("expenses.txt", "w") as file:
        file.write("Expense Calculator Result\n")
        file.write(f"Total Expense: {Total_Expense}\n")
        file.write(f"Each Person Pays: {round(Amount_Per_Person, 2)}\n")




