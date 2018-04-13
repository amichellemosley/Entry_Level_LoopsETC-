def doConversion():
    tempInFAsString = input('Enter the temperature in Farenheit: ')
    tempInF = float( tempInFAsString )
    tempInC = (tempInF - 32) * (5/9)
    print('The temperature in Celcius is', tempInC, 'degrees')

for conversionCount in range( 3 ):
    doConversion()
