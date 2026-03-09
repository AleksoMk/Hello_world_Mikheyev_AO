#!/bin/bash
read -p "Введите массу (кг): " WEIGHT
read -p "Введите рост (м): " HEIGHT

BMI=$(bc <<< "scale=0; $WEIGHT / ($HEIGHT * $HEIGHT)")

echo "Ваш ИМТ: $BMI"
