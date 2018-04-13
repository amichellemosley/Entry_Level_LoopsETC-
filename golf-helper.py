print( "Welcome to the Golf Club Helper!" )
print( "Tell me your situation, and I'll recommend a club!" )


LandedOnGreen = input( "Did you hit the ball on the green y/n?  " )

if LandedOnGreen == 'y':
    Range = int(input( "How far is the ball from the hole?  " ))
   
if LandedOnGreen == 'n':
    Range = int(input( "How far is the ball from the hole?  " ))
    
    
if Range >= 200:
    print( "I recommend using your Driver" )
    
if Range <200 and Range >= 140:
    print( "I recommend the 5 Iron" )
    
if Range < 140 and Range >= 100:
    print( "I recommend the 9-Iron" )
    
if Range < 100:
    print( "I recommend the pitching wedge" )
    

                
        
    
