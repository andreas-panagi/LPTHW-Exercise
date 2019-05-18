#VARIABLES AND NAMES
cars = 100
spaceInACar = 4.0
drivers = 30
passenger = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePasengersPerCar = passenger / carsDriven

print ("there are", cars, "cars available.")
print ("there are", drivers, "drivers available.")
print ("there will be", carsNotDriven, "empty cars today.")