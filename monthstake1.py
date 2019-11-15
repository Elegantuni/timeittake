#!/usr/bin/env python3

import sys
import math

if len(sys.argv) == 4:
	number1 = float(sys.argv[2])

	total1 = float(sys.argv[1])

	timetakes = total1 / number1

	years = int(timetakes / 12)

	months = int(math.ceil(timetakes % 12))

	if months == 12:
		months = 0
		years = years + 1

	months = months + int(sys.argv[3]) * years

	years = years + int(months / 12)

	months = int(months % 12)

	print("The total amount of years and months to produce $", total1, "saving $", number1, "per month and not saving $", number1, "for", int(sys.argv[3]), "times per year is", years, "years and", months, "months")
else:
	print(sys.argv[0], "<total price> <money saved per month> <months cant save anything>")

