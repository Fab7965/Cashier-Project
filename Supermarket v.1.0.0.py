#SCOPE
#create an application without ai assistance that simulates a cashier without relying on external databases.

#Defining a Function that allows us to endlessly list products and quantities
def enterProducts():
    #dictionary for the data so it can store the product and quantity as key-value pairs
    buyingData = {}
    #created a While loop for endless product listings
    enterDetails = True
    while enterDetails:
        #using input to allow the cashier to enter product names and quantity with a default argument to give directions.
        details = input('press A to add product and Q to quit:')
        if details == 'A':
            product = input('Enter Product: ')
            quantity = int(input('enter quantity: '))
            buyingData.update({product: quantity})
        #creating a conditional to exit the program
        elif details == 'Q':
            enterDetails = False
        else:
            print('please select a correct option')
    return buyingData
#Defining a function that calculates price
def getPrice(product, quantity):
    #create a dictionary of products and their Prices
    priceData = {
        'Biscuit': 3,
        'Chicken': 2,
        'Taco': 1,
        'Egg': 2,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 1,
        'Milk': 4,
        'Cheese': 4,
        'Ham': 2
    }
    #calculate the total price of the order and display it.
    subtotal = priceData[product]* quantity
    print(product + ':$' + str(priceData[product]) + 'X' + str(quantity) + '=' + str(subtotal))
    return subtotal
#command to test the function, Works.
#getPrice (bread, 10)
#create a function with a conditional that introduces membership discounts on orders above 25$.
def getDiscount(billAmount, membership):
    discount = 0
    #introduce the conditional, and the membership tiers
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount* 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount* 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount* 0.95
            discount = 5
        elif membership == 'No':
            billAmount = billAmount
            discount = 0
        #return the updated price and the reasoning behind the discount or no discount.
        print(str(discount)+ '% off for '+ membership +' ' + 'membership on total amount: $' + str(billAmount) )
    else:
        print('No discount on amount less than 25')
    return billAmount
#command to test this block of code:
#getDiscount(30, 'Gold')
#code = Functional
# Final bill function
def makeBill(buyingData, membership):
    #declaring and initializing the billAmount variable to hold the subtotal amount of the customer.
    billAmount = 0
    #calculate the subtotal and store it in the billAmount variable.
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    #deduct the discount from subtotal
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is $'+ str(billAmount))
# putting it all together.
buyingData = enterProducts() #stores product name + quantity as buyingData so it can be printed, and used for furthur calculations.
print(buyingData) #dislays the product name + quantity
membership = input('enter customer membership: ') #specifies Discount tier
makeBill(buyingData, membership) #applies the discount and totals the order.