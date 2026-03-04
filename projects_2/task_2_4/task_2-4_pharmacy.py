capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите вместимость одной упаковки (шт): "))

full_packs = capsules // pack_size
remaining = capsules % pack_size

print("--- Отчет о фасовке ---")
print(f"Полных упаковок:\t{full_packs} шт")
print(f"Остаток капсул:\t\t{remaining} шт")