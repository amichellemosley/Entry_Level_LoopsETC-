# Please write your bitcoin_converter program in this file.

#As of 8/1/17 at 11:13 am, bitcoin is currently trading at $2086 per bitcoin.
#Enter the bitcoin amount: .5
#That is worth 1043 us dollars.

print("As of 8/1/17 at 11:13 am, bitcoin is currently trading at $2086 per bitcoin.")

BitCoinAmount = float(input( "Enter the Bit Coin amount here: "))

DollarAmount = BitCoinAmount * 2086

print("That is worth", DollarAmount, "us dollars" )


