# Parcial 2 Python MUTANTES
+ Nombre y Apellido: Gonzalo Diego Murguia
+ Legajo: 51601
+ Email Escolar: gonzalo.murguia@alumnos.frm.utn.edu.ar
+ Email: gonzalo.murguia@outlook.es
## Proyecto Mutantes
El proyecto consiste en desarrollar un programa que pueda detectar si un humano es mutante basándose en su secuencia de ADN.
## Explicación del código
El código consta de dos partes principales: la función esMutante y el bucle que solicita al usuario que ingrese las secuencias de ADN.
## Función esMutante
La función esMutante toma como parámetro un array de Strings que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representan cada base nitrogenada del ADN.

La función esMutante verifica si hay más de una secuencia de 4 letras iguales en horizontal, vertical o diagonal en el array de cadenas. Si encuentra más de una secuencia de 4 letras iguales, devuelve “El ADN es de un mutante”. De lo contrario, devuelve “El ADN es de una persona normal”.

## Bucle de entrada de ADN
Además, se creó un bucle que solicita al usuario que ingrese 6 secuencias de ADN. Si la secuencia ingresada es válida (es decir, contiene solo las letras A, T, G, C y tiene una longitud de 6), la secuencia se agrega a la lista dna. Si la secuencia no es válida, el programa solicita al usuario que ingrese una nueva secuencia.

## Cómo correrlo
Para correr el programa, simplemente necesitas tener Python instalado en tu computadora. Luego, puedes copiar y pegar el código en un archivo .py y ejecutarlo desde la línea de comandos. El programa te pedirá que ingreses las secuencias de ADN una por una. Después de ingresar las 6 secuencias, el programa te dirá si el ADN es de un mutante o de una persona normal.

Caso mutante:{“ATGCGA”,“CAGTGC”,“TTATGT”,“AGAAGG”,“CCCCTA”,“TCACTG”}; Caso no mutante: {“ATGCGA”,“CAGTGC”,“TTATTT”,“AGACGG”,“GCGTCA”,“TCACTG”};
