def showReadingGlassesOrder (firstName, lastName, address, country, lenses, blueLightProction):
    if country == "Canada":
        shippingFee = '$25.00'
    elif country == "US":
        shippingFee = '$15.00'
    elif country == "Mexico":
        shippingFee = '$26.50'
    
    if blueLightProction:
        print(f"{firstName} {lastName}\n{address}\n -----------------\n Lenses: {lenses}x (Blue light protection included)\n shipping charges are {shippingFee}.")
    else:
        print(f"{firstName} {lastName}\n{address}\n -----------------\n Lenses: {lenses}x\n shipping charges are {shippingFee}.")


showReadingGlassesOrder("Akshay", "Tandon", "12 Peaceful Place", "Canada", 1.25, False)
showReadingGlassesOrder("Merella", "Fernandez", "126 Main Street", "Canada", 1.35, True)
showReadingGlassesOrder("Rachel", "Nichols", "18 Sunset Blvd", "US", 1.05, True)
showReadingGlassesOrder("Maria", "Dulce", "Paseo de la Reforma", "Mexico", 1.30, False)