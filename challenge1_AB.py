# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations"""

loan_costs = [500, 600, 200, 1000, 450]

# 1. Number of loans
num_loans = len(loan_costs)

# 2. Total value of the loans
value_loans = sum(loan_costs)

# 3. Average loan amount
avg_loan_cost = value_loans / num_loans

#4. Print calculations
print(f"There are {num_loans} loans in the portfolio with a total value of ${value_loans} " + 
f"and an average price of ${avg_loan_cost:.0f}")

"""Part 2: Analyze Loan Data."""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(future_value, remaining_months)

hurdle_rate = 0.2
present_value = future_value/(1+hurdle_rate/12)**loan.get("remaining_months")
print(present_value)

if present_value >= loan.get("loan_price"):
    print("The loan is worth buying")
else:
    print("The loan is too expensive - do not buy")


"""Part 3: Perform Financial Calculations."""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/(1+annual_discount_rate/12)**remaining_months
    return present_value

annual_discount_rate = 0.2
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans = []

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Header row
    csvwriter.writerow(header)

    # Data rows
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
