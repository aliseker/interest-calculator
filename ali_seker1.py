print("..............................................\n.*.*.*.*Welcome to interest calculator.*.*.*.*\n..............................................")

name = str(input("enter your name please: "))
interest_rate = float(input("enter the interest rate(per year):"))
loan_amount = int(input("enter loan amount($):"))
print("--> TIME LENGTH")
max_year = int(input("loan terms in years:"))
max_month = int(input("loan terms in months:"))
iteration_interval = int(input("iteration interval:"))
print("Report for", name)

def print_duration(n):
    print("year:", n//12, "month:", n%12 )

def print_money(m):
    print(round(m,1),"$")

def print_entry(loan_amount, interest_rate,month):
    print("----------------------")
    total= loan_amount + (loan_amount/100)*(interest_rate/12)*month
    print_duration(month)
    print("Total payment:")
    print_money(total)
    print("Monthly payment:")
    print_money(total/month)
    print("----------------------")

def print_full_report(loan_amount, interest_rate, max_year, max_month, iteration_interval):
    for iteration_interval in range (iteration_interval, max_year*12+max_month+1, iteration_interval):
        print_entry(loan_amount, interest_rate, iteration_interval)
print_full_report(loan_amount, interest_rate, max_year,max_month, iteration_interval)
