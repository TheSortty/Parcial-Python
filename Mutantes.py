def esMutante(dna):
    contadorDeCoincidencia = 0
    for i in range(6):
        for j in range(3):
            if dna[i][j:j+4].count(dna[i][j]) == 4:
                contadorDeCoincidencia += 1
            if dna[j][i] == dna[j+1][i] == dna[j+2][i] == dna[j+3][i]:
                contadorDeCoincidencia += 1
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                contadorDeCoincidencia += 1
            if dna[i][5-j] == dna[i+1][4-j] == dna[i+2][3-j] == dna[i+3][2-j]:
                contadorDeCoincidencia += 1
    return "UN MUTANTE D: (ADN mutante)" if contadorDeCoincidencia > 1 else "Todo correcto, persona normal!"

dna = []
for i in range(6):
    while True:
        cadena = input("Ingrese la " + str(i+1) + " secuencia del ADN: ").upper()
        if set(cadena) <= set("ATGC") and len(cadena) == 6:
            dna.append(cadena)
            break
        else:
            print("SECUENCIA INVALIDA. !Ingrese una secuencia de 6 caracteres con las letras A, T, G, C. :D")
print(esMutante(dna))