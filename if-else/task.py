"""

13. Write a program to input electricity unit charge and calculate the total 
	electricity bill according to the given condition:

	For first 50 units Rs. 0.50/unit   -> 0 to 50 -> 25
	For next 100 units Rs. 0.75/unit   -> 50 to 150  -> 75
	For next 100 units Rs. 1.20/unit   -> 150 to 250  -> 120
	For unit above 250 Rs. 1.50/unit   -> 250 > -> 1.50 -> 75 

	300 
	50 - 0.50 = 25
	100 - 0.75=75
	100 - 1.20 = 120
	50 - 1.50  = 75   total - 295


"""


unit = int(input("Enter the Ele Units :"))
bill = 0

if unit <= 50 :
    bill = unit * 0.50
    
if unit <= 150 :
    bill = (50 * 0.50) + (unit - 50) * 0.75
    
if unit <= 250 :
    bill = (50 * 0.50) + (100 * 0.75) + (unit - 150) * 1.20
    
if unit > 250 :
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (unit - 250) * 1.50

print("Total Electricity Bill : ", bill)