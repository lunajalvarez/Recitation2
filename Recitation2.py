#######################################################################
# Program Filename: Gas and such
# Author: Luna Alvarez
# Date: 04/07/2022
# Description: This program allows a user to input the MPg or equivalent of a vehicle,
# in addition to the current cost of gas or power, and outputs the amount they will spend
# on average on gas or power annually.
# Input: MPG or MPGe
# Output: Gallons or equivalent used over a year, cost of gas/power over a year
#######################################################################

mpyppOregon = 14032 #Miles/year/person driven in Oregon
mpgCar = 126 #MPG or equivalent MPG for car of your choice
mpyppOregon/mpgCar
print('Gallons or equivalent gallons used over a year:')
print(mpyppOregon/mpgCar) #This will output the gallons or equivalent gallons used over relevant year
gallsUsed = mpyppOregon/mpgCar
costGas = 0 #Input cost of gas per gallon during relevant year
costGas * gallsUsed
print('Cost of gas over year:')
print(costGas * gallsUsed) #This will output your cost of gas over the relevant year
costPower = .1116 #Input the cost of power per kWh during relevant year
costAPower = (33.7 * costPower)
costAPower * gallsUsed
print('Cost of power over year:')
print(costAPower * gallsUsed) #This will output your cost of power over the relevant year





