# Store the sales tax rate in a module. This module should also contain functions that calculate the sales tax and the total after tax. These functions should round the results to a maximum of two decimal places.

SALES_TAX_RATE = .06

def get_tax(total_without_tax):
    "Takes the total bill without any tax applied as a Number. Returns the rounded sales tax to be applied."
    tax = total_without_tax * SALES_TAX_RATE
    return round(tax, 2)
    

def get_total(total_without_tax):
    "Takes the total bill without any tax applied as a Number. Returns the rounded total with sales tax added."
    total = total_without_tax + get_tax(total_without_tax)
    return round(total, 2)