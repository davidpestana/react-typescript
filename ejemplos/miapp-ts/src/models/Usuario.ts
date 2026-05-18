import type Direccion from './Direccion';

type NumeroPositivo = number;

function esNumeroPositivo(value: number): value is NumeroPositivo {
  return value >= 0;
}

type Usuario = {
  nombre: string;
  edad: NumeroPositivo;
  direccion?: Direccion;
};

export { esNumeroPositivo };
export type { Usuario, NumeroPositivo };
export default Usuario;
