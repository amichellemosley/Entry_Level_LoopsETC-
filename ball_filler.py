# Please do your work for problem one in this file

#How many bowling balls will be manufactured? 100
#What is the diameter of each ball in inches? 8.5
#What is the core volume in inches cubed? 124
#You will need 19755.509806430524 inches cubed of filler

bowlingballs = float(input("How many bowling balls will be manufactured?: "))

diameter = float(input("What is the diameter of each ball in inches?: "))

radius = .5 * diameter

TotalVolume = float(1.33333333* 3.141592653589793 * radius **3)

CoreFiller = float(input("What is the core volume in inches cubed?: "))

HowMuchCubedFiller = float(TotalVolume - CoreFiller)

HowMuchTotal = bowlingballs * HowMuchCubedFiller

print('You will need', HowMuchTotal, 'inches of cubed filler')

                



