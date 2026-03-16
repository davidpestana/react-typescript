import Usuario from "../models/Usuario"


const Sugus = ({sabor}: {sabor:string}) => <div>Sugos de {sabor}</div>



const HolaMundo = ({nombre, edad, direccion:{calle, numero}={calle: "desconocida", numero:0}}: Usuario) => {
 
    return <>{ ['fresa','limon','pina'].map((sabor,pos) => <Sugus key={pos} sabor={sabor} />) } </>
}
     
export default HolaMundo;