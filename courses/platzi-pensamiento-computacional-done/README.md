# Curso de Introducción al Pensamiento Computacional con Python

https://platzi.com/cursos/python-cs/

## Modulo: programas númericos

### Enumeración Exhaustiva

* También llamado "adivina y verifica".
* Consiste en probar todas las posibilidades hasta encontrar la respuesta.
* El problema con este algoritmo es que si la solución no es exacta o no está dentro del espacio de busqueda, no es posible encontrar la solución. Por ejemplo: la raiz cuadrada de 27.

### Aproximación de Soluciones

* Similar a la `enumeración exhaustiva` pero no necesita una respuesta exacta.
* Podemos aproximar soluciones con un margen de error que llamaremos `epsilon`.
* Aqui toca encontrar un trade-off entre ser precisos y rapidos, debido a que este algoritmo suele ser muy lento entre más precisos queramos ser.

### Búsqueda Binaria

* Es uno de los algoritmos más importantes y más eficientes.
* Cuando la respuesta del problema dado, se encuentra en un conjunto ordenado es posible utilizar búsqueda binaria.
* En la busqueda binaria el espacio de busqueda se corta a la mitad en cada iteración por lo que se vuelve más eficiente.

## Modulo: funciones, alcance y abstracción

### Docstring
Auto Docstring: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
Python Docstring: https://www.datacamp.com/tutorial/docstrings-python

### Recursividad
**Algoritmica**: Una forma de crear soluciones utilizando el principio de "divide y venceras".
**Programatica**: Una técnica programática mediante la cual una función se llama así misma.

Cualquier función recursiva podemos representarla como un loop. Por ejemplo: los factoriales.
```python
def factorial(n):
    if n == 1: # caso base para que no se vuelva un loop infinito
        return 1
    return n * factorial(n -1)
```
Python tiene un limite de recursividad que se puede conocer usando la libreria `sys.getrecursionlimit()`.

## Modulo: Pruebas y Debugging

### Pruebas de caja negra

Se llaman pruebas de caja negra porque asumimos que no conocemos la implementación o función que se está testeando, simplemente se le dan `inputs` y se valida que los `outputs` que da la función sean correctos.
Este tipo de pruebas son muy importantes dentro de dos subtemas dentro del testing que se llaman *unit testing* y *integration testing*.

**Unit test:** También conocidas como pruebas unitarias y lo que hacen es probar función por función viendo que nuestro código en cada uno de los modulos funcione.

**Integration testing:** Es cuando vemos que todos los modulos funcionan entre sí.

La idea es seguir la metodología *Test Driven Development (TDD)* que es una metdología donde nos dedicamos primero a escribir las pruebas de nuestro código, y luego si programamos las funcionalidades.

https://platzi.com/blog/que-es-y-como-funciona-tdd/

### Pruebas de caja de cristal

Se basan en el flujo del programa. A diferencia de las pruebas de caja negra, esta asumen que nosotros conocemos toda la implementación o función y busca probar todos los posibles caminos que existen en nuestra función. 

Estas pruebas son buenas cuando tenemos que hacer *regression testing* es decir que descubrimos un bug una vez el programa ya salió a producción y para poderlo determinar tenemos que saber cómo está estructurado el código.

* Si dentro del código tenemos ramificaciones, es decir, `if{} else{}` entonces debemos probar qué pasa cuando entramos en `if` cuando entramos en `elif` y cuando entramos al `else` en el caso de python. 

* Si tenemos un loop (`for, recursiones`), debemos probar qué pasa cuando no entramos al loop, cuando entramos una vez y cuando entramos más de una vez. 

* Si tenemos un `while loop`, tenemos que hacer una prueba en donde la condición de entrada sea falsa y una prueba en donde veamos los *break statements* como se comportan.

### Debugging

La mejor forma de evitar bugs es con los tests, sin embargo muchas veces no es suficiente.

**Reglas generales:**

* No te molestes con el debugger. Aprender a utilizar el print statement.
* Estudiar los datos disponibles.
* Utilizar los datos para crear hipotesis y experimentos. Método cientifico.
    + Debugear es un proceso de búsqueda. Cada prueba debe acotar el espacio de búsqueda.
    + Búsqueda binaria con print statements.
* Tener mente abierta. Si entendieramos el programa, probablemente no habrían bugs.
* Llevar un registro de los bugs que se han tratado, preferentemente en la forma de tests.
* Explicar el programa a otra persona. De preferencia que no tenga contexto.
* Vete a dormir.

**Errores comunes:**

* Pasar los argumentos en un orden incorrecto
* Nombres escritos de manera errónea
* No inicializar una variable que era necesaria inicializar
* Tratar de comparar 2 flotantes con igualdad exacta, en lugar de usar una aproximación
* Usar un “is” cuando era un “==” o viceversa
* Las funciones pueden tener efectos secundarios

## Algunas links de interes:

https://github.com/karlbehrensg/introduccion-pensamiento-computacional
