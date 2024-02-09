#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = set("aeiouyаеёиоуыэюя")

    text = input("Введите предложение: ")

    count = sum(1 for char in text.lower() if char in vowels)

    print("Количество гласных в строке:", count)