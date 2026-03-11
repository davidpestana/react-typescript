# 27. Portals

**PDF: páginas 142–142** (libro: 138–138)

---

## Portals

Los Portals son una de las características de React que nos permite renderizar componentes fuera
del árbol de componentes de nuestra aplicación, entendiendo árbol de componentes, todos aquellos
componentes que cuelgan desde el componente raíz (normalmente el que llamamos App y que se
inyecta en el archivo de index.html). Esto es especialmente útil cuando necesitamos que ciertos
elementos (como modales) se rendericen en una ubicación diferente del árbol DOM.

Para crear un portal en React utilizamos el método ReactDOM.createPortal() que recibe dos
parámetros:

- Aquello que queremos renderizar

- El elemento del DOM donde queremos renderizarlo

ReactDOM.createPortal(contenido, contenedor)
