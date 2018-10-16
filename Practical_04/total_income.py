"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of Months."""
    incomes = []
    Pay_Months = int(input("How many Months? "))

    for month in range(1, Pay_Months + 1):
        paycheck = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(paycheck)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, Pay_Months + 1):
        paycheck = incomes[month - 1]
        total += paycheck
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, paycheck, total))


main()