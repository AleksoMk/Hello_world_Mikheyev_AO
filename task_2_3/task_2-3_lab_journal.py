researcher = input("ФИО исследователя: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

width = 40
border  = "+" + "=" * (width - 2) + "+"
divider = "+" + "—" * (width - 2) + "+"

journal = (
    f"{border}\n"
    f"|{'ЭЛЕКТРОННЫЙ ЛАБОРАТОРНЫЙ ЖУРНАЛ':^{width - 2}}|\n"
    f"{border}\n"
    f"| {'ФИО исследователя : ' + researcher:<{width - 4}} |\n"
    f"| {'Дата              : ' + date:<{width - 4}} |\n"
    f"| {'Эксперимент       : ' + experiment:<{width - 4}} |\n"
    f"{divider}\n"
    f"| {'Вывод:':<{width - 4}} |\n"
    f"| {conclusion:<{width - 4}} |\n"
    f"{border}\n"
)

with open("journal.txt", "w", encoding="utf-8") as f:
    f.write(journal)

print(journal)
print("Журнал сохранён в journal.txt")