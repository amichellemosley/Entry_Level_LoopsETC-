class StockHolding:
    def __init__( self, symbol, shares, price ):
        self.symbol = symbol
        self.shares = int(shares)
        self.price = float(price)
        
    
    def getSymbol( self, symbol):
        return self.symbol
    
    def getNumofShares( self, shares):
        return self.shares
    
    def getTotalCost( self, shares, price):
        return self.price * self.shares
    
    
    def estimateProfit( self, numofShares, numofprice):
        numofShares = input(int( "Number of shares: "))
        numofprice = input(float("Price per share: "))
        profit = numofShares * numofprice
        return profit 
    
    def sellShares( self, currentshares, numtosell):
        currentshares = int(input("Enter your current amount of shares: "))
        numtosell = int(input("Enter the amount of shares you are wanting to sell: "))
        sharestosell = currentshares - numtosell
        if currentshares >= numtosell:
            return sharestosell
        if numtosell <= currentshares:
            ValueError = print(" Value Error! Current shares is less than amount of shares to sell.")
            return ValueError 


def main():
    estimateProfit( self, numofShares, numofprice)
    sellShares( self, currentshares, numtosell)
    #testStockHolding = StockHolding()


main()
