#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    text1 = input("Введите первое предложение: ")
    text2 = input("Введите второе предложение: ")

    plenty1 = set(text1)
    plenty2 = set(text2)

    shared_sym = plenty1.intersection(plenty2)

    print("Общие символы:", shared_sym)