# Crea data/muestra.log con una de cada N lineas de data/access.log
N = 100

total = 0
guardadas = 0
with open("data/access.log", encoding="utf-8", errors="ignore") as entrada, \
     open("data/muestra.log", "w", encoding="utf-8") as salida:
    for numero, linea in enumerate(entrada):
        total += 1
        if numero % N == 0:
            salida.write(linea)
            guardadas += 1

print("Lineas leidas:", total)
print("Lineas guardadas en la muestra:", guardadas)
