#!/usr/bin/env python
import sys

# Convert Tempaerature from Fahrenheit to Celcius and back
# Runs from terminal with python conv_temp.py f2c fahrenheit_temp or c2f celsius_temp

def f2c(fahrenheit):
	return (fahrenheit - 32) * 5/9

def c2f(celsius):
	return (celsius * 9 / 5) + 32

if len(sys.argv) != 3:
	print("Usage: ")
	print(f" python {sys.argv[0]} f2c temp")
	print(f" python {sys.argv[0]} c2f temp")
	sys.exit(1)

conversion = sys.argv[1]
temperature = float(sys.argv[2])

if conversion == "f2c":
	result = f2c(temperature)
elif conversion == "c2f":
	result = c2f(temperature)
else:
	print("Error: conversion must be 'f2c' or 'c2f'")

print(f"{result:.1f}")
