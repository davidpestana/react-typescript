# 30.3. Connect

**PDF: páginas 204–205** (libro: 200–201)

---

Para poder acceder al Store y poder recibir el estado y emitir acciones, vamos a usar el método
connect() que recibe dos parámetros, el primero mapStateToProps y el segundo
mapDispatchToProps. Este método va a inyectarle al componente que indiquemos el estado y
emisores de acciones que necesitemos.

- mapStateToProps es una función que recibe como parámetro el estado y lo mapea a props que
va a pasar a nuestro componente. Tiene que devolver un objeto con la parte del estado que
queremos usar en el componente.

- mapDispatchToProps es una función que recibe como parámetro el método dispatch y que
devuelve un objeto con las funciones que van a emitir las acciones que nos devuelven los action
creators, y lo va a pasar como propiedades al componente. En lugar de una función, podemos
asignarle a mapDispatchToProps un objeto con los actions creators y el se encarga de emitir
las acciones correctas.

Decir también que la ejecución del método connect devuelve un HOC (Higher Order Component)
encargado de pasarle estos datos como propiedades al componente que se le va a pasar como
parámetro.

```tsx
import { accion1, accion2 } from 'store/app/actions';
import { connect } from 'react-redux';

const Cmp = (props) => {
  return (
    <div>
      <p>{props.dato1}</p>
      <button onClick={props.accion1}>Despachar acción 1</button>
      <button onClick={() => props.accion2(192)}>Despachar acción 2</button>
    </div>
  )
}

const mapStateToProps = (state) => {
  return {
    dato1: state.dato1
  }
}

// const mapDispatchToProps = (dispatch) => {
//   return {
//     accion1: () => dispatch(accion1()),
//     accion2: (n) => dispatch(accion2(n))
//   }
```
// }

```tsx
const mapDispatchToProps = {
  return {
```
accion1,

accion2
```tsx
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Cmp);
```
