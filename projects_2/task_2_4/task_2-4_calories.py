protein_mass = float(input("Массу белков в продукте (г)"))
fat_mass = float(input("Массу жиров в продукте (г)"))
carbohydrate_mass = float(input("Массу углеводов в продукте (г)"))

caloric_content = protein_mass*4+fat_mass*9+carbohydrate_mass*4
print (caloric_content)