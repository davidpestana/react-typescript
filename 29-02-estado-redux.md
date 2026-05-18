# 29.2. Estado Redux

**PDF: páginas 189–189** (libro: 185–185)

---

[← Índice](README.md) | [← Anterior: 29.1. Instalacion Redux](29-01-instalacion-redux.md) | [Siguiente: 29.3.1. Action Creators →](29-03-01-action-creators.md)

---

El estado de la aplicación es cualquier información necesaria para representar la interfaz de
usuario en un momento dado. Pueden ser desde datos externos que podemos obtener del servidor
al estado de la interfaz de usuario como si un modal se está mostrando o si un menú está
desplegado.

Imaginad que tenemos una aplicación con varios componentes en la que cada componente tiene su
propio estado, va a funcionar bien. Pero si empieza a crecer puede ser un poco difícil de seguir
todas las actualizaciones o cambios ya que hay que ir mirando en cada componente el estado que
tiene. Redux propone tener todos los estados en un mismo lugar, en un objeto global inmutable, de
esta forma va a resultar mucho más fácil de ver todos los datos de la aplicación.

Cuando vamos a construir aplicaciones usando Redux, lo primero en lo que hay que pensar es en
definir la estructura que vamos a necesitar para guardar todos los datos del estado (en un objeto
JavaScript).