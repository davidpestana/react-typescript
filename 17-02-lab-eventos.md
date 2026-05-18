# 17.2. Lab Eventos

**PDF: páginas 64–65** (libro: 60–61)

---

[← Índice](README.md) | [← Anterior: 17.1. Tipos Eventos](17-01-tipos-eventos.md) | [Siguiente: 18. Estados →](18-00-estados.md)

---

En este laboratorio vamos a ver como detectar el evento click para hacer que nuestro navegador
cante la intro de la serie de dibujos de Batman, pero mal cantada.

Vamos a copiar la plantilla del proyecto que se ha realizado en el laboratorio reactjs-proyecto-
inicial-lab y vamos a cambiarle el nombre del proyecto a reactjs-eventos-lab.

Es posible que sea necesario volver a instalar las dependencias del proyecto para
que funcione correctamente. Para ello solo tenemos que lanzar el comando npm
install dentro de la carpeta del proyecto.

Ahora vamos a levantar el servidor de desarrollo con el comando:

```tsx
$ npm start
```
Lo primero que vamos a hacer es crear un botón y la función que se encargará de hacer que el
navegador hable.

**Archivo:** `/reactjs-eventos-lab/src/components/App.tsx`

```tsx
const App = () => {
  const handleClick = () => {}

    return (
      <div>
        <button type="button">Que suene la intro</button>
      </div>
    )
}

export default App
```
Ahora vamos a rellenar la función de handleClick.

Empezaremos añadiendo el código que genera el texto que queremos que diga el navegador. Este
texto se lo pasaremos al constructor de SpeechSynthesisUtterance.

Con la instancia generada vamos a cambiar el valor de rate para que hable un poco más lento de lo
que por defecto hace.

Y por último llamaramos a window.speechSynthesis.speak para pasarle la configuración anterior
y que finalmente nos cante mal la intro.

**Archivo:** `/reactjs-eventos-lab/src/components/App.tsx`

```tsx
const App = () => {

const handleClick = () => {
  const textoIntro = new Array(16).join(1-'wat') + ' Batman!';
  const configSpeech = new SpeechSynthesisUtterance(textoIntro);
  configSpeech.rate = 0.8;
  window.speechSynthesis.speak(configSpeech);
}

    return (
      <div>
        <button type="button">Que suene la intro</button>
      </div>
    )
}

export default App
```
Finalmente, si pulsamos el botón, vemos que no hace nada, y esto se debe a que nos falta poner el
evento onClick y asignarle la función que queremos que se ejecute.

**Archivo:** `/reactjs-eventos-lab/src/components/App.tsx`

```tsx
const App = () => {
  const handleClick = () => {
    const textoIntro = new Array(16).join(1-'wat') + ' Batman!';
    const configSpeech = new SpeechSynthesisUtterance(textoIntro);
    configSpeech.rate = 0.8;
    window.speechSynthesis.speak(configSpeech);
  }

    return (
      <div>
        <button type="button" onClick={handleClick}>Que suene la intro</button>
      </div>
    )
}

export default App
```
Ahora ya debería de escucharse la into al pulsar el botón.
