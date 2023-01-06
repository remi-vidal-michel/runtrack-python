fruits = ["pomme","cerise","orange"]
def listfruits():
    var = fruits[0]
    fruits[0] = fruits[2]
    fruits[2] = var
    return fruits