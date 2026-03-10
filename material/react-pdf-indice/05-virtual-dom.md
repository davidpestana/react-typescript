# 5. Virtual Dom

**PDF: páginas 13–13** (libro: 9–9)

---

## Virtual DOM

Por razones de rendimiento, no es viable volver a renderizar toda la interfaz cada vez que se
realiza un cambio en los datos, por lo que React usa, en memoria, una implementación propia del
DOM, el Virtual DOM. Manipular la representación en memoria del DOM es mucho mas rápido y
eficiente que hacerlo en el DOM real. Nosotros no nos tenemos que preocupar por interactuar con
la API del DOM directamente, nosotros tendremos que interactuar con el Virtual DOM (con los
elementos de React, que conceptualmente parecen HTML pero en realidad son objetos JavaScript) y
React se encargará de realizar esos cambios en el DOM real por nosotros, de la forma más eficiente
posible.

El proceso es el siguiente, cuando se produce algún cambio en el estado de la aplicación, este
cambio se aplica a la representación del DOM en memoria. Después usa un algoritmo de diff para
calcular las diferencias entre el DOM real y el que está en memoria, de donde obtiene los cambios
mínimos a realizar para obtener la estructura del DOM deseada. Y de esta forma solo aplica esos
cambios al DOM real sin necesidad de renderizar más elementos de los necesarios.
