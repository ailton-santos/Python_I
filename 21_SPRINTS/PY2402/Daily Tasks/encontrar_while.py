# -*- coding: utf-8 -*-
"""encontrar while

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xb31VD1Z7wQsfEfGDj5S4EnlouDWJyfh
"""

maior=float(0)
menor=float(1000000000000000000)
media=float()
a=float()
while a<10:
 b=float(input('Número {}: '.format(a+1)))
 a=a+1
 if b>maior:
  maior=b
 if b<menor:
  menor=b
 media=media+b
print('O maior número foi: ',maior)
print('O menor número foi: ',menor)
print("a média dos números é: ",soma/10)

