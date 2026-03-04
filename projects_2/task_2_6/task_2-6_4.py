hero_choice = input("Куда пойдёшь Илья Муромец?").lower().strip()

if hero_choice == "прямо":
    print("Умрёшь")
elif hero_choice == "налево":
    print("Жену найдёшь")
elif hero_choice == "направо":
    print("Богатым станешь")
else:
    print("Не богатырь ты")