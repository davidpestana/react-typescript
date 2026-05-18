import { useState, type MouseEvent } from 'react';
import './styles.css';

const CODIGO_SECRETO = '3038';
const MAX_DIGITOS = 4;

const PanelCodigoSecreto = () => {
  const [codigoActual, setCodigoActual] = useState('');

  const pulsarTecla = (tecla: string) => {
    setCodigoActual((prev) => {
      if (tecla === 'CLD') return '';
      if (tecla === 'DEL') return prev.slice(0, -1);
      if (prev.length >= MAX_DIGITOS) return prev;
      const next = prev + tecla;
      return next === CODIGO_SECRETO ? 'CODE OK' : next;
    });
  };

  const onTeclaClick = (event: MouseEvent<HTMLButtonElement>) => {
    const tecla = event.currentTarget.dataset.tecla;
    if (tecla) pulsarTecla(tecla);
  };

  const filas: string[][] = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['CLD', '0', 'DEL'],
  ];

  return (
    <div className="panel-codigo-secreto">
      <div className="display" aria-live="polite">
        {codigoActual}
      </div>
      <div className="teclas">
        {filas.map((fila, i) => (
          <div key={i} className="fila-teclas">
            {fila.map((tecla) => (
              <button
                key={tecla}
                type="button"
                className="tecla"
                data-tecla={tecla}
                onClick={onTeclaClick}
              >
                {tecla}
              </button>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default PanelCodigoSecreto;
