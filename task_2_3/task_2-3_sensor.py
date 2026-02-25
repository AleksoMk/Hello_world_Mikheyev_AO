operator_name = input("Имя оператора: ")
pressure_value = input("Значение датчика давления: ")

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")
