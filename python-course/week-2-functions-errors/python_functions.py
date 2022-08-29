# without using function
bill = 175.00
tax_rate = 15
total_tax = bill * tax_rate / 100.00

print("Total tax: ", total_tax)

# with using a function
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print("Total tax: ", calculate_tax(200, 20))
print("Total tax: ", calculate_tax(162.4, 64))