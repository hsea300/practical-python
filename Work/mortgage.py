# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0 
month = 0 

extra_payment_start_month = int(input("Enter the month you will start extra payment: "))
extra_payment_end_month = int(input("Enter the month you will end extra payment: "))
extra_payment = int(input("Extra payment: "))


while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)

    else:
      principal = principal * (1+rate/12) - payment 
      total_paid = total_paid + payment

    print(month, round(total_paid), round(principal))
    
      

print('Total paid', total_paid) 



##Other way with f string

# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0 
month = 0 

extra_payment_start_month = int(input("Enter the month you will start extra payment: "))
extra_payment_end_month = int(input("Enter the month you will end extra payment: "))
extra_payment = int(input("Extra payment: "))


while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)

    else:
      principal = principal * (1+rate/12) - payment 
      total_paid = total_paid + payment

    #print(month, round(total_paid), round(principal))
    print(f'Month: {month}, Total Paid:{round(total_paid,2)}')

print('Total paid', total_paid) 

