# 30.2. Provider

**PDF: páginas 203–203** (libro: 199–199)

---

[← Índice](README.md) | [← Anterior: 30.1. Instalacion React Redux](30-01-instalacion-react-redux.md) | [Siguiente: 30.3. Connect →](30-03-connect.md)

---

Esta librería nos provee de un componente Provider que recibe como propiedad el store y da
acceso al store a todos los componentes que están por debajo de el en el árbol de componentes. De
esta forma no tenemos que pasar, como propiedad, el store a todos los componentes para que estos
tengan acceso a el.

```tsx
import { createRoot } from 'react-dom/client'
```
// Importaciones
```tsx
import { Provider } from 'react-redux';

const store = configStore();
createRoot(document.getElementById('root')).render(<Provider store={store}><App /></Provider>);
```