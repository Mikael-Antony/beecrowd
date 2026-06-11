# -*- coding: utf-8 -*-
PriLinha = input()
PriPart = PriLinha.split()
PriItem = {
        "Codigo": PriPart[1],
        "Quantidade": float(),
        "Valor": float()
}
SegLinha = input()
SegPart = SegLinha.split()
SegItem = {
        "Codigo": int(),
        "Quantidade": float(),
        "Valor": float()
}
print(type(PriPart[1]), type(SegPart[1]))
