import { useState } from "react";
import './styles.css'


const PanelCodigoSecreto = () =>  {

  const [codigoActual, setCodigoActual] = useState<string>('')
  const [codigoSecreto] = useState<string>('3038')


  const handleClick = (event: React.MouseEvent<HTMLDivElement>) =>  {
    const tecla = (event.target as HTMLElement).textContent ?? '';

    setCodigoActual(prev => {
        const next =
        tecla === 'CLD'
            ? ''
            : tecla === 'DEL'
            ? prev.slice(0, -1)
            : prev.length < 4
            ? prev + tecla
            : prev;

        return next === codigoSecreto ? 'CODE OK' : next;
    });       
 }


   
    return (
      <div className="panel-codigo-secreto">
        <div className="display">
            { codigoActual} 
        </div>
        <div className="teclas" onClick={handleClick}>
          <div className="fila-teclas">
             <button type="button" className="tecla">1</button>
             <button type="button" className="tecla">2</button>
             <button type="button" className="tecla">3</button>
          </div>
          <div className="fila-teclas">
             <button type="button" className="tecla">4</button>
             <button type="button" className="tecla">5</button>
             <button type="button" className="tecla">6</button>
          </div>
          <div className="fila-teclas">
             <button type="button" className="tecla">7</button>
             <button type="button" className="tecla">8</button>
             <button type="button" className="tecla">9</button>
          </div>
          <div className="fila-teclas">
             <button type="button" className="tecla">CLD</button>
             <button type="button" className="tecla">0</button>
             <button type="button" className="tecla">DEL</button>
          </div>
        </div>
      </div>
    )

}
export default PanelCodigoSecreto;