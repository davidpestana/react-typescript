# 29. Redux

**PDF: páginas 187–187** (libro: 183–183)

---

## Redux

Redux es una librería que surge para entender como fluyen los cambios en los datos a través de la
aplicación. Redux está influenciado por el patrón Flux propuesto por el equipo de Facebook.

Redux está pensado sobre todo para usarlo con React, pero no impide usarlo con cualquier otra
librería o framework como podría ser Angular, Backbone…

Redux tiene actions, action creators, un store y action objects que usa para cambiar el estado de
la aplicación. También introduce los reducers que son funciones puras que devuelven el nuevo
estado basándose en los argumentos que recibe (el estado actual y una action).

Redux sigue 3 principios:

- El estado de la aplicación se almacena en un único objeto global inmutable.

- Los cambios en el estado se definen a través de las actions.

- Los reducers son los encargados de realizar los cambios al estado.
