import type Usuario from '../../models/Usuario';
import './HolaMundo.css';

type SugusProps = {
  sabor: string;
  color: string;
};

const Sugus = ({ sabor, color }: SugusProps) => (
  <div className="sugus" style={{ backgroundColor: color }}>
    <span className="sugus__label">{sabor}</span>
  </div>
);

type HolaMundoProps = Usuario;

const HolaMundo = ({ nombre, edad, direccion }: HolaMundoProps) => {
  const calle = direccion?.calle ?? 'sin calle';
  const numero = direccion?.numero ?? 0;

  const sabores: SugusProps[] = [
    { sabor: 'fresa', color: '#EA464C' },
    { sabor: 'limón', color: '#FDE23A' },
    { sabor: 'piña', color: '#227BBE' },
  ];

  return (
    <section className="hola-mundo">
      <h3>
        Hola {nombre}, {edad} años
      </h3>
      <p>
        Dirección: {calle} {numero}
      </p>
      <div className="hola-mundo__sugus">
        {sabores.map((s) => (
          <Sugus key={s.sabor} {...s} />
        ))}
      </div>
    </section>
  );
};

/** Datos de ejemplo para el demo del menú */
const usuarioEjemplo: Usuario = {
  nombre: 'Ana',
  edad: 28,
  direccion: { calle: 'Mayor', numero: 12 },
};

export default function HolaMundoDemo() {
  return <HolaMundo {...usuarioEjemplo} />;
}
