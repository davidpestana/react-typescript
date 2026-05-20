import { useReducer } from 'react'
import {
  calculadoraReducer,
  estadoInicial,
  type AccionCalculadora,
  type Operador,
} from './calculadoraReducer'
import './App.css'

function App() {
  const [estado, dispatch] = useReducer(calculadoraReducer, estadoInicial)

  const enviar = (accion: AccionCalculadora) => () => dispatch(accion)
  const op = (o: Operador) => enviar({ type: 'operador', op: o })

  return (
    <div className="app">
      <header className="cabecera">
        <h1>Calculadora</h1>
        <p className="subtitulo">
          Estado con <code>useReducer</code> y acciones tipadas.
        </p>
      </header>

      <div
        className="calculadora"
        role="application"
        aria-label="Calculadora básica"
      >
        <output className="pantalla" aria-live="polite">
          {estado.pantalla}
        </output>

        <div className="teclado">
          <button
            type="button"
            className="btn btn-secundario"
            onClick={enviar({ type: 'limpiar' })}
          >
            AC
          </button>
          <span className="hueco" aria-hidden />
          <button type="button" className="btn btn-operador" onClick={op('/')}>
            ÷
          </button>
          <button type="button" className="btn btn-operador" onClick={op('*')}>
            ×
          </button>

          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '7' })}
          >
            7
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '8' })}
          >
            8
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '9' })}
          >
            9
          </button>
          <button type="button" className="btn btn-operador" onClick={op('-')}>
            −
          </button>

          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '4' })}
          >
            4
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '5' })}
          >
            5
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '6' })}
          >
            6
          </button>
          <button type="button" className="btn btn-operador" onClick={op('+')}>
            +
          </button>

          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '1' })}
          >
            1
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '2' })}
          >
            2
          </button>
          <button
            type="button"
            className="btn"
            onClick={enviar({ type: 'digito', digito: '3' })}
          >
            3
          </button>
          <button
            type="button"
            className="btn btn-igual"
            onClick={enviar({ type: 'igual' })}
          >
            =
          </button>

          <button
            type="button"
            className="btn span-2"
            onClick={enviar({ type: 'digito', digito: '0' })}
          >
            0
          </button>
          <button type="button" className="btn" onClick={enviar({ type: 'punto' })}>
            ,
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
