# -*- coding: utf-8 -*-

Nome = input()
SalarioFixo = float(input())
VendasNoMes = (float(input())) * 0.15
Salario = SalarioFixo + VendasNoMes

print(f"TOTAL = R$ {Salario:.2f}")
