import graphics as g

win = g.GraphWin( "polygon tool", 200, 200 )


firsttext = g.Text( g.Point( 50, 65 ), "Click 1" )
firsttext.draw( win )
firstclick = g.Point( 50, 75 )
firstclick.draw( win )

win.getMouse()
firstline = g.Line( g.Point( 50, 75), g.Point( 150, 75 ))
firstline.draw( win )
secondtext = g.Text( g.Point( 150, 65 ), "Click 2" )
secondtext.draw( win )
#win.getMouse( firsttext )

win.getMouse()
#click here and it draws line from firstclick to secondclick
thirdtext = g.Text( g.Point( 100, 160 ), "Click 3")
thirdtext.draw( win )
secondline = g.Line( g.Point( 150, 75), g.Point( 100, 150 ))
secondline.draw( win )                    
secondclick = g.Point( 150, 75)
secondclick.draw( win )

win.getMouse()
thirdline = g.Line( g.Point( 100, 150), g.Point( 50, 75))
thirdline.draw( win )
#click here and it draws line from secondclick to thirdclick
#and puts a line between thirdclick and firstclick 
thirdclick = g.Point( 100, 150)
thirdclick.draw( win )
closingtext = g. Text( g.Point( 100, 180), "Click here to close" )
closingtext.draw( win )

win.getMouse()
win.close()

