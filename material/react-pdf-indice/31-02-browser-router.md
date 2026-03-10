# 31.2. Browser Router

**PDF: páginas 217–217** (libro: 213–213)

---

Una vez que se han instalado las librerías tenemos que permitir el uso del routing en nuestra
aplicación para poder usar las funcionalidades que este nos va a proporcionar. Para ello tenemos
que envolver toda nuestra aplicación con el componente BrowserRouter que importaremos desde
el paquete de react-router-dom.

Este componente se va a encargar de interactuar con la API del historial del navegador para poder
poner las URLs en la barra de direcciones, además de ir añadiendo/eliminando estas direcciones en
la pila del historial.

**Archivo:** `/src/app.js`

```tsx
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './components/App';

createRoot(document.getElementById('root')).render(<BrowserRouter><App /><
/BrowserRouter>);
```
Una vez envuelta nuestra nuestra aplicación con ese componente, todos aquellos componentes que
se encuentren por debajo de este en el árbol de componentes, serán capaces de usar las rutas.
