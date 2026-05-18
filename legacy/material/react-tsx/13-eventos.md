# 13. Eventos

[← Índice](README.md) | [← Anterior: Renderizado condicional](12-renderizado-condicional.md)

---

Los eventos en React son **sintéticos** (SyntheticEvent). Se tipan con los tipos de React.

```tsx
const FormularioEjemplo = () => {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // ...
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value);
  };

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.currentTarget.disabled = true;
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" onChange={handleChange} />
      <button type="button" onClick={handleClick}>Enviar</button>
    </form>
  );
};
```

Tipos habituales: `React.ChangeEvent<HTMLInputElement>`, `React.MouseEvent<HTMLButtonElement>`, `React.FormEvent<HTMLFormElement>`.

---

[Siguiente: 14. Estado con useState →](14-estado-usestate.md)
