reagent_name = input()
reagent_quantity = int(input())

report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

print(report)

f = open("inventory.txt", "w", encoding="utf-8")
print(report, file=f)
f.close()