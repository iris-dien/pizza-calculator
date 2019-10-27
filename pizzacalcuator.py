class PizzaCalcuator:
    # 1. ask manager: obtain the unti price of pizza 
    pepperoni_price = input("what is the price of a pepperoni pizza tonight?")  

    pepperoni_price = eval(pepperoni_price) 

    hawaiian_price = input ("what is the price of a hawiian pizza tonight?")
    hawaiian_price = eval(hawaiian_price) 

    cheese_price = input ("what is the price of a cheese pizza tonight?")
    cheese_price = eval(cheese_price) 


    # 2. ask customer: which pizzas would they like?
    number_of_pepperonis =  0
    number_of_hawaiians = 0
    number_of_cheese = 0 

    # customer can opt to order > 1 pizza type
    # she will enter: 1, 2 and/or 3
    pizzas_selected = input( 
    
        "customer, which pizzas do you want to order? (1, pepperoni, 2. hawaiian, 3. cheese")
    
    if("1" in pizzas_selected):
        #1. ask customer for quantity
        number_of_pepperonis = input( 
            "how many pepperoni pizzas would you like to order?")
        
        number_of_pepperonis = eval(number_of_pepperonis)

    if("2" in pizzas_selected):
        #1. ask customer for quantity
        number_of_hawaiians = input( 
            "how many hawaiian pizzas would you like to order?")
        
        number_of_hawaiians = eval(number_of_hawaiians)

        
    if("3" in pizzas_selected):
        #1. ask customer for quantity
        number_of_cheese = input( 
            "how many cheese pizzas would you like to order?")
        
        number_of_cheese = eval(number_of_cheese)


    #3. calcuator order before tax ( formula : order = price * quantity)
    pepperoni_order = number_of_pepperonis * pepperoni_price
    hawawiian_order = number_of_hawaiians * hawaiian_price
    cheese_order = number_of_cheese * cheese_price
   
   
    total_order = pepperoni_order + hawawiian_order + cheese_order

    print("Here's your order before tax: ", total_order)



    #4. calcuate tax (assume 4%)
    tax_rate = .04 

    sales_tax_amount = total_order  * tax_rate 
    
    
    print("your sales tax amounts to", sales_tax_amount, "at", .04) 


    #5. calculate grand total
    grand_total = total_order + sales_tax_amount 

    print("your grand total comes to", grand_total)  




    