# 26. Suspense

**PDF: páginas 137–137** (libro: 133–133)

---

[← Índice](README.md) | [← Anterior: 25.2. Lab Hoc Cargar Datos](25-02-lab-hoc-cargar-datos.md) | [Siguiente: 26.1. Lab Suspense →](26-01-lab-suspense.md)

---

## Suspense (lazy loading)

En aplicaciones que son muy grandes, descargarnos toda la aplicación la primera vez que se entra
puede tardar más tiempo del que debería tardar. Para solucionar este problema tenemos la carga
perezosa o lazy loading.

El lazy loading nos ayuda a decrementar el tiempo de arranque de la aplicación. La primera vez
que entramos en la aplicación, no necesitamos cargar todo. Solo cargaremos aquello que el usuario
espera ver.

El resto de la aplicación, aquellas partes en las que no se suele entrar solo se cargarán una vez que
el usuario entre en ellas. De esta forma nuestra aplicación se va a ir descargando a trozos según el
usuario los vaya necesitando evitándole esperas superiores a las necesarias.

```tsx
En React podemos realizar el lazy loading con React.Suspense y React.lazy.
```
El primero es un componente que envuelve a los componentes que todavía no se han renderizado
porque se están descargando, y con el que haremos que se muestre un componente mientras se
descargan y renderizan.

El segundo es una función que se encarga de cargar de forma diferida el componente que
mostraremos dentro de Suspense.

```tsx
const ComponentePerezoso = React.lazy(() => import('./ComponentePerezoso'));

function MiComponente() {
  return (
     <React.Suspense fallback={<p>Loading...</p>}>
       <div>
         <ComponentePerezoso />
       </div>
     </React.Suspense>
  );
}
```