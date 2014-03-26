
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

def c(sequence):
	"""Gerate items in sequence; keepig counts as we go. c.starts is the 
	number of sequences started; c.items is number of items generated."""
	c.starts += 1
	for item in sequence:
		c.items += 1
		yield item

def zebra_puzzle():
	"Return a tuple (WATER, ZEBRA) indicating their house numbers"
	houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
	orderings = list(itertools.permutations(houses))
	# Generator expression   next( (gen expr) )
	# gen_exp =  ( r  in   for r in xyx  if .. for .. if.. for .. if  for for for ) 
	# next(gen_exp)
	return next( (WATER, ZEBRA)
			for (red, green, ivory, yellow, blue) in c(orderings)
			if imright(green, ivory)
			for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
			if Englishman is red
			if Norwegian is first
			if nextto(Norwegian, blue)
			for (coffee, tea, milk, oj, WATER) in c(orderings)
			if coffee is green
			if Ukranian is tea
			if milk is middle
			for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
			if Kools is yellow
			if LuckyStrike is oj
			if Japanese is Parliaments
			for (dog, snails, fox, horse, ZEBRA) in c(orderings)
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

def timedcalls(n, fn, *args):
	"Call function n times with args; return the min, avg, and max time."
	times = [timedcal(fn, *args)[0] for _ in range(n)]
	return min(times), average(times), max(times)

def average(numbers):
	"Return the average (arithmetic mean) of a sequence of numbers"
	return sum(numbers) / float(len(numbers))

def timedcalls2(n, fn, *args):
	""" Call fn(*args) repeatedly: n times if n is a int, or up to 
	n seconds if n is a float; return the min, avg and max time"""
	if isinstance(n, int):
		times = [timedcal(fn, *args)[0] for _ in range(n)]
	else:
		times = []
		while sum(times) < n:
			times.append(timedcal(fn, *args)[0])
	return min(times), average(times), max(times)

def instrument_fn(fn, *args):
	c.starts, c.items = 0, 0
	result = fn(*args)
	print("%s got %s with %5d iters over %7d items" % (fn.__name__, result, c.starts, c.items))


# >>> instrument_fn(zebra_puzzle)
# zebra_puzzle3 got (1, 5) with 25 iters over 2775 items

# >>> instrument_fn(zebra_puzzle2)
# zebra_puzzle2 got (1, 5) with 39328 iters over 4719135 items





