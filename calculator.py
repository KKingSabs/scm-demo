def calculate_discount(price,membertype):
    if membertype == "regular":
        return price *0.2

    if membertype == "premium":
        return price *0.3        

    return price * 0.10
