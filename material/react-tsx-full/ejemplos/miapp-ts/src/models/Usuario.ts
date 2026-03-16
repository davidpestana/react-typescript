import Direccion from "./Direccion"

type NumeroPositivo = number;

function esNumeroPositivo(value: number): value is NumeroPositivo {
  if (value < 0) {
    console.error('El número tiene que ser mayor a 0');
    return false;
  }
  return true;
}


type Usuario =  {
  nombre: string,
  edad: NumeroPositivo,
  direccion?: Direccion
}

export default Usuario