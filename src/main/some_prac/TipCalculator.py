def calculate_tips(meal_price, custom_tip):
    _lst = []
    _min = 0.15
    _max = 0.20

    meal_price = meal_price.split("$")
    amount = float(meal_price[1]) 

    custom_tip = custom_tip.split("%")
    tip = int(custom_tip[0])/100
  
    _lst.append("$"+(str(round((_min * amount),2))))
    _lst.append("$"+str(round((_max * amount),2)))
    _lst.append("$"+str( round((tip * amount),2)))


    return _lst
    

print(calculate_tips("$89.67", "26%"))