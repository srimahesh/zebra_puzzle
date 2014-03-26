
import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
	"House h1 is immediately right of h2 if h1-h2 == 1"
	return h1-h2 == 1

def nextto(h1, h2):
	"Two houses are next to each other if they differ by 1"
	return abs(h1-h2) == 1

# for (red, green, ivory, yellow, blue) in orderings:
# 	for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:
# 		for (dog, snails, fox, horse, ZEBRA) in orderings:
# 			for (coffee, tea, milk, oj, WATER) in orderings:
# 				for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
# 					# contraints go here
# 					if (Englishman is red): #2


def zebra_puzzle():
	"Return a tuple (WATER, ZEBRA) indicating their house numbers"
	houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
	orderings = list(itertools.permutations(houses))
	# Generator expression   next( (gen expr) )
	# gen_exp =  ( r  in   for r in xyx  if .. for .. if.. for .. if  for for for ) 
	# next(gen_exp)
	return next( (WATER, ZEBRA)
			for (red, green, ivory, yellow, blue) in orderings
			if imright(green, ivory)
			for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
			if Englishman is red
			if Norwegian is first
			if nextto(Norwegian, blue)
			for (coffee, tea, milk, oj, WATER) in orderings
			if coffee is green
			if Ukranian is tea
			if milk is middle
			for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
			if Kools is yellow
			if LuckyStrike is oj
			if Japanese is Parliaments
			for (dog, snails, fox, horse, ZEBRA) in orderings
			if Spaniard is dog
			if OldGold is snails
			if nextto(Chesterfields, fox)
			if nextto(Kools, horse)
			)
	 		
	 		# if Englishman is red		#2
	 		# if Spaniard is dog			#3	
	 		# if coffee is green  		#4
	 		# if Ukranian is tea			#5
	 		# if imright(green, ivory)
	 		# if OldGold is snails
	 		# if Kools is yellow
	 		# if milk is middle
	 		# if Norwegian is first
	 		# if nextto(Chesterfields, fox)
	 		# if nextto(Kools, horse)
	 		# if LuckyStrike is oj
	 		# if Japanese is Parliaments
	 		# if nextto(Norwegian, blue)

# print(zebra_puzzle())

import time

def timedcal(fn, *args):
	"Call function and return elapsed time."
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result

# print(())
def average(numbers):
	"Return the average (arithmetic mean) of a sequence of numbers"
	return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
	"Call function n times with args; return the min, avg, and max time."
	times = [timedcal(fn, *args)[0] for _ in range(n)]
	return min(times), average(times), max(times)


def timedcalls2(n, fn, *args):
	""" Call fn(*args) repeatedly: n times if n is a int, or up to 
	n seconds if n is a float; return the min, avg and max time"""
	times = []
	if isinstance(n, int):
		times = [timedcal(fn, *args)[0] for _ in range(n)]
	else:
		while n > 0:
			call = timedcal(fn, *args)
			n = n - call[0]
			times.append(call[0])
	return min(times), average(times), max(times)

timedcalls2(10.0, zebra_puzzle)

