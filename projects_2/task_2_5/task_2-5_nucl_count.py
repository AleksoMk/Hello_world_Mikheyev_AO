dna = input("Введите последовательность ДНК: ").upper()

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

print ("-----Подсчёт нуклеотидов:-----")
print (f"A:  {count_A}")
print (f"A:  {count_T}")
print (f"A:  {count_G}")
print (f"A:  {count_C}")
print (f"Общая длина: {len(dna)}")