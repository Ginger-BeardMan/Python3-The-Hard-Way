# defines/creates the cheese_and_crackers function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# calls the cheese_and_crackers function
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# creates two variables to use when calling the cheese_and_crackers function
amount_of_cheese = 10
amount_of_crackers = 50

# calls the cheese_and_crackers function using the variables amount_of_cheese and amount_of_crackers as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# calls the cheese_and_crackers function using two equations as variables
cheese_and_crackers(10+20, 5+6)


print("And we can combine the two, variables and math:")
# calls the cheese_and_crackers function using the created variables with addition
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)