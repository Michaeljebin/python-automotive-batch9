def calculate_emi(loan_amount):
    print("Loan Amount: ", loan_amount)
    yearly_interest = float(input("Enter Annual Interest in %: "))
    years = int(input("Enter Loan Tenure (Years): "))
    # Convert yearly interest to monthly interest
    monthly_interest = yearly_interest / (12 * 100)
    # Convert years to months
    months = years * 12
    #  formula for emi
    emi = round((loan_amount * monthly_interest * (1 + monthly_interest)
                 ** months) / ((1 + monthly_interest) ** months - 1), 2)
    total_payment = round(emi * months, 2)
    # Total payment and interest
    total_interest = round(total_payment - loan_amount,2)
    print("\n--- Loan Calculation Details ---")
    print("Monthly EMI        :", emi,)
    print("Total Interest     : ", total_interest, )
    # Output
    print("Total Amount Paid  : ", total_payment,)
