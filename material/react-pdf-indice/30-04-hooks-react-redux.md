# 30.4. Hooks React Redux

**PDF: páginas 206–206** (libro: 202–202)

---

Con la llegada de los React Hooks muchas librerías se han actualizado para permitir usar la
funcionalidad de ellas usando este tipo de funciones.

En el caso de React Redux se han añadido dos hooks que nos van a permitir sustituir a la función
connect por ellos.

Estos hooks son:

- useSelector: este hook se encarga de obtener parte del estado que se almacena en el store. Este
hook recibe como parámetro una función en la que obtenemos el estado y con la que tenemos
que devolver un objeto con la parte de este que queramos usar en el componente.

- useDispatch: este hook nos devuelve una referencia a la función dispatch con la que vamos a
poder despachar las acciones que nos devuelven los action creators.

- useStore: este hook nos devuelve el objeto store de Redux para trabajar directamente con las
funciones que nos proporciona, como por ejemplo, getState o dispatch.

```tsx
import { useSelector, useDispatch, useStore } from 'react-redux';
import { accion1, accion2 } from 'store/app/actions';

const Cmp = () => {
  const store = useStore();
  console.log(store.getState());

const dato1 = useSelector(state => state.dato1);
const dispatch = useDispatch();

    return (
      <div>
        <p>{dato1}</p>
        <button onClick={() => dispatch(accion1())}>Despachar acción 1</button>
        <button onClick={() => dispatch(accion2(192))}>Despachar acción 2</button>
      </div>
    )
}

export default Cmp;
```
