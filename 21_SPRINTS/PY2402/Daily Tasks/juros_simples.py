# -*- coding: utf-8 -*-
"""Juros simples

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sVD1v96SapvOJJUv-0vEWURo1I2xAf6q
"""

a=float(input("Digite o valor da compra: "))

b=float(input("Digite em quantas vezes voçê deseja pagar: "))

j=float

if b>4.9 and b<12:
  j=5
elif b>11.9 and b<14:
  j=12.4
elif b>13.9:
 j=15.3
else:
  j=-5

v=float(a+(a/100)*j)

print("O valor da compra é: ",v)