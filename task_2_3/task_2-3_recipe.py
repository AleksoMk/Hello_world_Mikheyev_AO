medium_name = input("Название питательной среды: ")
agar_concentration = input("Концентрация агара (%): ")
sterilization_temp = input("Температура стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\nКонцентрация агара: {agar_concentration}%\nТемпература стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")
