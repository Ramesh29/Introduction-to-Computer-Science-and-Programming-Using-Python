# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:00:14 2021

@author: charl
"""

balance = 320000
annualInterestRate = 0.2
interestRate  = annualInterestRate / 12.0

lowerBoundPayment = balance/12.0
upperBoundPayment = ( balance * ((1+interestRate)**12) ) / 12.0


while True:
    payment = (lowerBoundPayment + upperBoundPayment )/2.0

    preBalance = balance
    for i in range(12):
        curBalance = preBalance - payment
        curBalance = curBalance + (interestRate * curBalance)
        preBalance = curBalance
        

    if round(curBalance, 2) > 0.00:
        lowerBoundPayment = payment
    elif round(curBalance,2) < 0.00:
        upperBoundPayment = payment
    else:
        break
print("Lowest Payment:", round(payment,2) )