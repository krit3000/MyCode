# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''

def sales_tax():
	UserPurchase = float(input("Enter the amount of purchase: "))

	statesales_tax = 0.05 * UserPurchase

	countysales_tax = 0.025 * UserPurchase

	total_tax = statesales_tax + countysales_tax

	total_sale = total_tax + UserPurchase

	print("Amount of purchase: $" + format(UserPurchase, ",.2f"), "State Sales Tax: $" + format(statesales_tax,",.2f"), "County Sales Tax: $" + format(countysales_tax, ",.2f"), "Total Tax: $" + format(total_tax, ",.2f"), "Total Sale: $" + format(total_sale, ",.2f"))

# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	P = float(input("Enter the starting principal: "))
	r = float(input("Enter the annual interest rate: "))
	n = float(input("How many times per year will is the interest compounded?: "))
	t = float(input("For how many years will the account earn interest?: "))
	compound_interest = ((1 + (r / (100 * n))) ** (n*t)) * P
	print("At the end of the " + str(format(t , ",.0f")) + " years you will have $" + str(format(compound_interest, ",.2f")))


# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	penny = 0.01
	nickel = 0.05
	dime = 0.10
	quarter = 0.25

	numpenny = int(input("Please enter the number of pennies: "))
	numnickel = int(input("Please enter the number of nickels: "))
	numdime = int(input("Please enter the number of dimes: "))
	numquarter = int(input("Please enter the number of quarter: "))

	pennyval = penny * numpenny
	nickelval = nickel * numnickel
	dimeval = dime * numdime
	quarterval = quarter * numquarter
	totalval = pennyval + nickelval + dimeval + quarterval

	if totalval == 1.00:
		print("Congratulations! The amount you entered was exactly one dollar! You win the game!")

	else:
		if totalval < 1.00:
			print("Sorry, the amount you entered was less than one dollar.")
		if totalval > 1.00:
			print("Sorry, the amount you entered was more than one dollar.")



# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
'''
Enter the number of packages purchased: 10
'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	packagepurchase = int(input("Enter the number of packages purchased: "))
	packageprice = 99

	if packagepurchase < 10: 
		discount = 0;
	elif packagepurchase < 20:
		discount = 0.10
	elif packagepurchase < 50:	
		discount = 0.20
	elif packagepurchase < 100:	
		discount = 0.30
	else:
		discount = 0.40

	subTotal = packagepurchase * packageprice
	Total = subTotal - (subTotal*discount)
	discountAmount = discount * subTotal

	print("Discount amount: $" + str(format(discountAmount, ",.2f")), "Total Amount: $" + str(format(Total, ",.2f")))
	


# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
'''
Enter the weight of the package: 10
'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	packageweight = int(input("Enter the weight of the package: "))
	shippingrate = 0

	if packageweight <= 2:
		shippingrate = 1.50
	elif packageweight <= 6:
		shippingrate = 3.50
	elif packageweight <= 10:
		shippingrate = 4
	else:
		shippingrate = 4.75

	shippingcharge = packageweight * shippingrate

	print("Shipping Charge: $" + str(format(shippingrate, ",.2f")))


# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	budget = int(input("Enter amount budgeted for the month: "))
	spent = int(input("Enter an amount spent(0 to quit): "))
	totalspent = 0 

	while (spent != 0):
		totalspent += spent
		spent = int(input("Enter an amount spent(0 to quit): "))

	print("Budgeted: $" + format(budget, ",.2f"))
	print("Spent: $" + format(totalspent, ",.2f"))	

	if budget > totalspent: 
		print("You are $" + format(budget - totalspent, ",.2f") + " under budget. WELL DONE!")
	elif budget == totalspent:
		print("Spending matches budget. GOOD PLANNING!")
	else:
		print("You are $" + format(totalspent - budget, ",.2f") + " over budget. PLAN BETTER NEXT TIME!")

# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	years = int(input("Enter the number of years: "))
	rainfall = 0
	month = 0
	print("For year " + str(years) + ": ")

	for i in range(years * 12): 
		rain = int(input("Enter the rainfall amount for the month: "))
		month += 1 
		rainfall += rain

	print("For " + str(month) + " months")
	print("Total Rainfall: " + format(rainfall,",.2f") + " inches" )
	print("Average Monthly Rainfall: " + format(rainfall / month, ",.2f") +" inches") 		
			

# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
'''
Enter a nonnegative integer: 10
'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	integer = int(input("Enter a nonnegative integer: "))

	factorial = 1 

	for i in range(1, integer + 1):
		factorial *= i

	print("The factorial of " + str(integer) + " is " + str(factorial))



# Exercise 4-12
# PROMPT(S) (Example user input of 'python'):
'''
Enter the string to be converted to Morse code: python
'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	userstr = str(input("Enter the string to be converted to Morse Code: "))

	userstr = userstr.lower()

	mydict = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '----.', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.-', 'z' : '--..', '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....- ', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', ' ' : ' ', ',' : '--..--', '.' : '.-.-.-', '?' : '..--..'} 
		
	
	for i in '.abcdefghijklmnopqrstuvwxyz123456789,? ':
			userstr = userstr.replace(i , mydict[i])

	print(userstr)

# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	# run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()