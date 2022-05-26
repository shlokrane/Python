def calculate(distance,no_of_passengers):
    fuel_cost = (distance / 10) * 70
    price_earned = no_of_passengers * 80
    if fuel_cost < price_earned:
        profit = price_earned - fuel_cost
        return profit
    else:
        return -1

distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))