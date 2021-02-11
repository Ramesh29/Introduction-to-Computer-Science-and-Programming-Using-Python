# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:20:04 2021

@author: charl
"""
balance = 3329
annualInterestRate = 0.2
fixedPayment = 10
interestRate  = annualInterestRate / 12.0

preBalance = balance
while True:
    for i in range(12):
        curBalance = preBalance - fixedPayment
        curBalance = curBalance + (interestRate * curBalance)
        preBalance = curBalance
        
    if curBalance <= 0:
        break
    else:
        fixedPayment = fixedPayment + 10
        preBalance = balance

print("Lowest Payment:", fixedPayment )