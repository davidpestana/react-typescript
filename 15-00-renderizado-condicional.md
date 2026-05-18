# 15. Renderizado Condicional

**PDF: páginas 54–55** (libro: 50–51)

---

[← Índice](README.md) | [← Anterior: 14.4. Lab Propiedades](14-04-lab-propiedades.md) | [Siguiente: 16. Listas →](16-00-listas.md)

---

## Renderizado condicional

En nuestras aplicaciones de React nos vamos a encontrar con algunos casos en los que tendremos
que pintar un componente u otro dependiendo de alguna condición.

Por ejemplo, cuando estamos logueados veremos el botón de Logout, pero cuando no lo estemos
tendríamos que ver el botón de Login. Entonces, tendremos que usar el renderizado condicional
para indicar cual de los dos botones se pintan.

En React esto lo podemos conseguir hacer con instrucciones de JavaScript ya que no tenemos
directivas al igual que ocurre en otros frameworks como Vue o Angular que se encarguen de ello.

Así que la idea es utilizar una instrucción if-else de JavaScript para devolver estos dos
componentes o etiquetas.

```tsx
if (logueado) {
  return <button>Logout</button>

} else {

  return <button>Login</button>
}
```
Lo de arriba serviría, pero es algo que no está bien visto dentro de React, por lo que tenemos que
buscar alguna otra instrucción que permita hacer lo mismo. El operador ternario, condicion ?
loQueSeEjecutaSiEsTrue : loQueSeEjecutaSiEsFalse.

```tsx
return (
  <div>
    {logueado ? <button>Logout</button> : <button>Login</button>}
  </div>
)
```
El operador ternario sería la opción correcta para pintar un componente u otro en función de una
condición.

Otras veces solo querremos pintar un elemento si cumplimos una condición, pero en el caso de que
no se cumpla la condición no debería de pintarse nada.

```tsx
return (
  <div>
    {condicion ? <p>El componente</p> : null}
  </div>
)
```
El código anterior sirve, porque se pinta un párrafo, o no se pinta nada, pero es más común utilizar
el operador and para evitar tener que poner ese null del operador ternario.

```tsx
return (
  <div>
    {condicion && <p>El componente</p>}
  </div>
)
```
