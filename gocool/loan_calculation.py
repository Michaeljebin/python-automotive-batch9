loan_amount = float(input("Enter Loan Amount (₹): "))
yearly_interest = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))
monthly_interest = yearly_interest / (12 * 100)    # Convert yearly interest to monthly interest
months = years * 12                                # Convert years to months
emi = (loan_amount * monthly_interest * (1 + monthly_interest) ** months) / ((1 + monthly_interest) ** months - 1)  #  formula for emi
total_payment = emi * months
total_interest = total_payment - loan_amount    # Total payment and interest
print("\n--- Loan Calculation Details ---")  
print("Monthly EMI        :",emi,)
print("Total Interest     : ",total_interest, )
print("Total Amount Paid  : ",total_payment,)       # Output