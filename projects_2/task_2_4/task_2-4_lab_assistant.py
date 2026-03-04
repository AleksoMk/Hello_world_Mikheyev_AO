solution_volume = float(input("Объем раствора (в мл):"))
salt_mass = solution_volume * 0.009
water_volume = solution_volume

with open(r"C:\Users\user\Documents\Mikheyev_AO\projects_2\task_2_4\recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"--- Рецепт физиологического раствора ---\n")
    f.write(f"Объем раствора:\t\t{solution_volume} мл\n")
    f.write(f"Масса соли (NaCl):\t{salt_mass:.2f} г\n")
    f.write(f"Объем воды:\t\t{water_volume} мл\n")
    f.write(f"Концентрация:\t\t0.9%\n")

print("Рецепт сохранён в файл recipe.txt")
