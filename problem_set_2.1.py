# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:23:07 2021

@author: charl
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

iRate = annualInterestRate / 12.0

pBal = balance
for m in range(12):
    minPayment = monthlyPaymentRate * pBal
    pBal = pBal - minPayment
    pBal = pBal + ( iRate * pBal)

print("Remaining balance:" , round(pBal, 2))