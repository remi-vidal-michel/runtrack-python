def market(type, saison):
    if type == "fruit" and saison == "hiver":
        return "Orange, Mandarine et Kiwi"
    elif type == "fruit" and saison == "été":
        return "Poire, Fraise, Cassis"
    elif type == "légume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "légume" and saison == "été":
        return "artichaut, aubergine,navet"

print(market("fruit", "hiver"))
print(market("fruit", "été"))
print(market("légume", "été"))
