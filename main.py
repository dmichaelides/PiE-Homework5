"""
'Python-is-Easy' Homework #5 (Basic Loops)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with Loops in Python.  It is the fifth homework assigment in the
'Python is Easy' course, from Pirple.

The FizzBuzz challenge.  Write a program that prints numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz", and for numbers which are divisible by only itself and 1, print "Prime". 

"""
FBPList = [] #This is the list we will compose. The FizBuzzPrimeList.

# Compose list with Fizz, Buzz and FizzBuzz numbers.  Prime numbers will be replaced afterward.
for num in range(1,101):
	if num%3 == 0 and num%5 == 0: # First find the FizzBuzz numbers. Condition set to AND to make sure that this unique number is filtered out first. If not FizzBuzz, jumps to next 'if' statement.
		FBPList.append("FizzBuzz")
		continue # If the number is FizzBuzz, we need to start the loop again to keep the order of numbers appended to the list in correct sequence.
	if num%5 == 0: # Find the Buzz words next.  
		FBPList.append("Buzz")
		continue # If the number is Buzz, we need to start the loop again to keep the order of numbers appended to the list in correct sequence.
	if num%3 == 0:
		FBPList.append("Fizz")
		continue # If the number is Fizz, we need to start the loop again to keep the order of numbers appended to the list in correct sequence.
	else: # If the number has not been filtered up to this point, it is neither Fizz, Buzz nor FizzBuzz and we simply add the actual number to the list.
		FBPList.append(num)

collection = [] # The collection list will be used to filter out the Prime numbers.  All non-prime numbers will be collected into this list with the 'Find Non Prime' loop. 

# The Find Non Prime loop. All non prime numbers (except for the number 2), found. 
for findnonprime in range(101,1,-1):
	for n in range(101,1,-1): # loop within a 'parent' for loop. The sequence will divide each number from the Parent loop, by the sequence of numbers lower than the parent number in the sub loop. 
		if n < findnonprime: # check for non-prime, by dividing from a divisor always lower than the dividend.  
			if findnonprime%n == 0 and n != 1: # At this level, if the modulo operation is equal to zero AND is not equal to 1, then the number is divisable by other numbers other than itself and 1.  
				if findnonprime not in collection: # since we are looping, we want to keep the list unique. 
					collection.append(findnonprime) # collect non-prime numbers. 

collection.append(2) # the reason we manually add 2, is because the 'Find Non Prime' loop logic does not work for number 2.

# Identify the index number for the Prime numbers, and replace the value in the FBPList to 'Prime'. 
for findprimeindex in range(100):
	if findprimeindex+1 not in collection:
		FBPList[findprimeindex] = "Prime"

print(FBPList)
