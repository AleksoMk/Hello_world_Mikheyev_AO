donor_blood_type = input("Введите группу крои донора:" ).upper().strip()
recipient_blood_type = input("Введите группу крови реципиента:").upper().strip()
if donor_blood_type in ("A", "B", "AB", "0") and recipient_blood_type in ("A", "B", "AB", "0"):
    if donor_blood_type == recipient_blood_type or donor_blood_type == "0":
        print ("Переливание возможно")
    print("Переливание невозможно")
else:
    print("В лабораторию на опыты")