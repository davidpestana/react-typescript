# 28. React Hooks

**PDF: páginas 146–146** (libro: 142–142)

---

[← Índice](README.md) | [← Anterior: 27.1. Lab Portals](27-01-lab-portals.md) | [Siguiente: 28.1. Reglas Hooks →](28-01-reglas-hooks.md)

---

## React Hooks

En la versión 16.8 de React, se han añadido los React Hooks, que son funciones que permiten usar
características de React en los componentes funcionales que antes no se podían usar, como por
ejemplo el estado.

Además, otra ventaja de estas funciones es que nos van a permitir reutilizar lógica entre los
distintos componentes, algo que antes conseguiamos con los Higher Order Components cuyo
principal problema era que si inspeccionabamos el árbol de componentes, este se volvía demasiado
grande y por tanto dificil de seguir.

Usando los componentes funcionales, ya no vamos a tener que preocuparnos por el objeto this que
tantos problemas puede traer sobre todo a aquellas personas que todavía no se manejan bien con
JavaScript.

Ahora en lugar de tener la lógica repartida en distintos métodos del ciclo de vida de los
componentes, podemos agruparla en uno de los hooks que veremos.

### 28.1. Reglas de los React Hooks

Para usar los hooks correctamente, tenemos que tener en cuenta las siguientes reglas:

- Hay que declarar los hooks al inicio de la función del componente.

- No se pueden usar los hooks dentro de componentes de clases. Solo podemos llamar a los hooks
desde los componentes funcionales y los custom hooks.

- No debemos llamar a estas funciones dentro de bucles, condicionales o funciones anidadas
porque React se basa en el orden en que llamamos a los hooks para guardar el estado del
```tsx
componente. Si el orden de ejecución cambia, React no será capaz de preservar el estado.
```