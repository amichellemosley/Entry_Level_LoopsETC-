#invoices = open("sales_data.csv", "r")
#invoices.readline()
invoice = id or name 


#invoiceline = id or name 
while True:
##    invoice = invoices.split(',')
    searchBy = input( "Search by invoice id or customer lname?    ".format( invoice ))
    while True:
        if searchBy != invoice:
            break
        print( "ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search" )
        if searchBy == invoice:
            break
        print( "finshed") 
        
       # while True:
          #  invoice = nextlines
           # invoice = invoices.readlines()
            #idorname = input( "Enter your search term:    ".format( nextlines ))
            #while True:
                #if idorname == nextlines:
                  #  break
                #print( nextlines )
            
            
    
#idorname = id or lname
#while True:
   # searchBy = input( "Search by invoice id or customer lname?    ".format( idorname ))
   # while True:
    # if searchBy != idorname:
       # break
   # print( "ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search" )
   # if searchBy == idorname:
    #    break
   # print( "finished" )       
 
        
    