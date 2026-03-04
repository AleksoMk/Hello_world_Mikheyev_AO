ph = float(input("Введи значение pH:"))

if 7 < ph <= 14:
    print("Щелочная среда")
elif 0 <= ph < 7:
    print("Кислая среда")
elif ph == 7:
    print("Нейтральная среда")
else:
    print("Не может такого быть")