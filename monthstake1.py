#!/usr/bin/env python3

import sys
import math

if len(sys.argv) == 4:
	number1 = float(sys.argv[2])

	total1 = float(sys.argv[1])

	moneyoff = float(sys.argv[3])

	timetakes = total1 / number1

	years = int(timetakes / 12)

	total2 = total1 / number1 + (years+1) * moneyoff

	months = int(math.ceil(total2 % 12))

	years = int(total2 / 12)

	print("The total amount of years and months to produce $", total1, "saving $", number1, "per month and not saving $", number1, "for", int(sys.argv[3]), "times per year is", years, "years and", months, "months")
else:
	print(sys.argv[0], "<total price> <money saved per month> <months cant save anything>")

