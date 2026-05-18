# 27.1. Lab Portals

**PDF: páginas 143–145** (libro: 139–141)

---

En este laboratorio vamos a ver cómo usar React Portals para mostrar un modal en un elemento
```tsx
HTML externo al contenedor donde se muestra la aplicación de React.
```
Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial y vamos a cambiarle el nombre del proyecto a reactjs-portals-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Primero, definimos una etiqueta para el portal del modal en el archivo public/index.html:

**Archivo:** `/public/index.html`

```tsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= htmlWebpackPlugin.options.title %></title>
</head>
<body>
  <div id="root"></div>

  <div id="modal"></div>
</body>
</html>
```
Ahora creamos el componente Modal usando React Portal:

**Archivo:** `/src/components/Modal.jsx`

```tsx
import ReactDOM from 'react-dom';
import './Modal.css'

const Modal = ({ onClose, children }) => {
  return ReactDOM.createPortal(
    <div class="backdrop">
      <div class="modal">
        <button onClick={onClose}>X</button>
        <hr />
        {children}

          </div>
        </div>,
        document.getElementById('modal')
    )
}

export default Modal
```
Creamos los estilos para el modal:

**Archivo:** `/src/components/Modal.css`

.backdrop {
```tsx
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
```
.modal {
```tsx
  position: relative;
  width: 70vw;
  height: 60vh;
  background-color: white;
}
```
Finalmente, implementamos el componente App:

**Archivo:** `/src/components/App.jsx`

```tsx
import React, { useState } from "react"
import Modal from "./Modal"

const App = () => {
  const [isClosed, setIsClosed] = useState(true)

return (
  <div>
    <button type="button" onClick={() => setIsClosed(false)}>Abrir modal</button>

{!isClosed && <Modal onClose={() => setIsClosed(true)}>
```
Hola mundo!
```tsx
      </Modal>}
    </div>
)

export default App
```
