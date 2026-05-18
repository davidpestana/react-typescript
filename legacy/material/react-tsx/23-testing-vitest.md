# 23. Testing con Vitest

[← Índice](README.md) | [← Anterior: Formularios](22-formularios.md)

---

Vitest se integra bien con Vite y React. Para componentes se suele usar **React Testing Library**.

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

Ejemplo de prueba de un componente TSX:

```tsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { Saludo } from './Saludo';

describe('Saludo', () => {
  it('muestra el nombre', () => {
    render(<Saludo nombre="Ana" />);
    expect(screen.getByText(/Hola Ana/)).toBeInTheDocument();
  });
});
```

Configuración en `vite.config.ts`: añadir `test: { environment: 'jsdom', globals: true }` y en `tsconfig` los tipos de Vitest si usas `expect` global.

---

[← Índice](README.md)
