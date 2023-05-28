def get_recipe_price(prices, optionals=None, **ingredients):
    if optionals:
        for option in optionals:
            prices.pop(option)

    cost = 0
    for ingredient, amount in ingredients.items():
        cost += prices[ingredient] * (amount // 100)
    return cost


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))
