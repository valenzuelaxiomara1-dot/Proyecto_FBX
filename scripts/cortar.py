with open('data/access.log', encoding='utf-8', errors='ignore') as entrada, \
     open('data/muestra.log', 'w', encoding='utf-8') as salida:
    for n, linea in enumerate(entrada):
        if n % 100 == 0:
            salida.write(linea)
print("¡Muestra creada con éxito!")