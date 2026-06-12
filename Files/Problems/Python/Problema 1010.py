# -*- coding: utf-8 -*-

PriPart = input().split()
PriItem = {
        "Codigo": int(PriPart[0]),
        "Quantidade": int(PriPart[1]),
        "Valor": float(PriPart[2])
}

SegPart = input().split()
SegItem = {
        "Codigo": int(SegPart[0]),
        "Quantidade": int(SegPart[1]),
        "Valor": float(SegPart[2])
}

ValorTotal = (PriItem["Quantidade"] * PriItem["Valor"]) + (SegItem["Quantidade"] * SegItem["Valor"])

print(f"VALOR A PAGAR: R$ {ValorTotal:.2f}") 
