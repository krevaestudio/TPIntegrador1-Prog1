# Trabajo Práctico Integrador – TUPaD - Programacion I 📑

## Info del grupo

**Alumnos:**
- Juan Barbero
- Andres Muñoz

**Comisión:**
Número 25

**Autoridades**
**Profesor:** Bruselario, Sebastian
**Tutor:** Carbonari, Veronica

**Fecha:** 09-06-2025
---

## Tema: Análisis de algoritmos

**Introducción**
El análisis de algoritmos es una práctica fundamental en la informática que nos permite medir y predecir el rendimiento de un programa. Entender cómo la elección de un algoritmo impacta el tiempo de ejecución y el consumo de memoria es crucial para construir software escalable y eficiente.
En este trabajo, se analiza esta idea a través de un problema clásico: el cálculo de la sucesión de Fibonacci. Se analizarán dos enfoques muy diferentes: uno recursivo simple y otro iterativo optimizado. A través de la implementación y medición de ambos, se demostrará cuantitativamente cómo una mejor aproximación algorítmica puede llevar a mejoras de rendimiento exponenciales y significativas.

**Marco teórico**
El análisis de algoritmos es el estudio teórico y práctico del rendimiento de los algoritmos. Su objetivo principal es optimizar dos recursos computacionales clave:
- Tiempo de ejecución (Complejidad Temporal): Cuánto tarda un algoritmo en completarse en función del tamaño de la entrada.
- Uso de memoria (Complejidad Espacial): Cuánta memoria adicional necesita un algoritmo para ejecutarse.


**Conceptos clave**
- **Notación Big-O:** Es el lenguaje estándar para describir la complejidad de un algoritmo. Se enfoca en el "peor caso" y describe cómo crece el tiempo de ejecución a medida que aumenta el tamaño de la entrada (por ejemplo: O(1) - constante, O(n) - lineal, O(n2) - cuadrático, O(2n) - exponencial).
- **Tiempo de ejecución real:** Es el tiempo medido en segundos que un programa tarda en ejecutarse. Se puede medir en Python con librerías como time.
- **Complejidad espacial:** Se refiere a la cantidad de memoria adicional (variables, estructuras de datos) que el algoritmo utiliza, sin contar la memoria de los datos de entrada.

---

## Caso práctico
Se analiza y compara dos algoritmos para calcular el n-ésimo número de la sucesión de Fibonacci.

**Link a video Explicativo y desarrollo**
[text](https://youtu.be/Bqx7XqDOyMY)

**Qué es la sucesión de Fibonacci?**
La sucesión de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores, comenzando con 0 y 1. Por ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

---

## Resultados obtenidos
- Ambos algoritmos calculan correctamente el n-ésimo número de Fibonacci.
- El tiempo de ejecución del algoritmo recursivo crece de forma exponencial. Para un n cercano a 40, ya tarda varios segundos, mientras que para n=50 sería impracticable.
- El algoritmo **iterativo** es drásticamente más rápido. Su tiempo de ejecución crece linealmente con n y puede calcular términos muy altos (Como el número 1000000 utilizado en el caso práctico) en segundos.
Los resultados prácticos confirman de manera contundente el análisis teórico de la notación Big-O.

---

## Conclusiones
La elección del algoritmo es determinante para el rendimiento de una aplicación. Como se demostró con el cálculo de Fibonacci, una solución recursiva puede ser computacionalmente inviable, mientras que una solución iterativa, aunque quizás menos directa al principio, ofrece un rendimiento y una escalabilidad muy superiores. Antes de implementar una solución, especialmente una recursiva, es importante analizar si realiza cálculos redundantes. En esos casos, técnicas como la iteración o la memoización (un paso intermedio que guarda resultados previos) son alternativas mucho más eficientes. Este proyecto subraya la importancia de no solo resolver un problema, sino de resolverlo eficientemente.

---

## Bibliografía

- Fundamentals of Data Structures in C++ E. *Horowitz, S. Sahni, D. Mehta Computer Science Press, 1995* 
- Python Time Documentacion Oficial (https://docs.python.org/3/library/time.html)
- Notacion Big-O (https://msmk.university/big-o-notation/)