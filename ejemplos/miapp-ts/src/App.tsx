import { useState, type ComponentType } from 'react';
import './App.css';
import HolaMundoDemo from './demos/HolaMundo/HolaMundoDemo';
import PanelCodigoSecreto from './demos/PanelCodigoSecreto/PanelCodigoSecreto';
import Click from './demos/Click';
import MiComponente from './demos/MiComponente';
import ContadorReduxDemo from './demos/ContadorRedux';

export type DemoId = 'inicio' | 'props' | 'estado' | 'eventos' | 'ciclo-vida' | 'redux';

type DemoEntry = {
  id: DemoId;
  label: string;
  chapter: string;
  Component?: ComponentType;
};

export const DEMOS: DemoEntry[] = [
  { id: 'inicio', label: 'Inicio', chapter: '' },
  { id: 'props', label: 'Props y tipos', chapter: 'Cap. 14', Component: HolaMundoDemo },
  { id: 'estado', label: 'Panel código secreto', chapter: 'Lab 18.1', Component: PanelCodigoSecreto },
  { id: 'eventos', label: 'Eventos', chapter: 'Cap. 17', Component: Click },
  { id: 'ciclo-vida', label: 'Componente de clase', chapter: 'Cap. 20', Component: MiComponente },
  { id: 'redux', label: 'Contador (store)', chapter: 'Caps. 28–29', Component: ContadorReduxDemo },
];

function Inicio() {
  return (
    <div className="demo-inicio">
      <p>
        Selecciona un ejemplo en el menú. Cada demo corresponde a un tema del manual{' '}
        <strong>React con TypeScript</strong>.
      </p>
      <ul>
        {DEMOS.filter((d) => d.Component).map((d) => (
          <li key={d.id}>
            <strong>{d.label}</strong> — {d.chapter}
          </li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  const [demoId, setDemoId] = useState<DemoId>('inicio');
  const active = DEMOS.find((d) => d.id === demoId) ?? DEMOS[0];
  const DemoView = active.Component;

  return (
    <div className="app-layout">
      <aside className="app-sidebar">
        <h1 className="app-title">Ejemplos</h1>
        <nav aria-label="Demos del curso">
          <ul className="demo-nav">
            {DEMOS.map((d) => (
              <li key={d.id}>
                <button
                  type="button"
                  className={demoId === d.id ? 'demo-nav__btn demo-nav__btn--active' : 'demo-nav__btn'}
                  onClick={() => setDemoId(d.id)}
                >
                  <span className="demo-nav__label">{d.label}</span>
                  {d.chapter ? <span className="demo-nav__chapter">{d.chapter}</span> : null}
                </button>
              </li>
            ))}
          </ul>
        </nav>
      </aside>
      <main className="app-main">
        <header className="demo-header">
          <h2>{active.label}</h2>
          {active.chapter ? <p className="demo-header__chapter">{active.chapter}</p> : null}
        </header>
        <div className="demo-content">
          {demoId === 'inicio' ? <Inicio /> : DemoView ? <DemoView /> : null}
        </div>
      </main>
    </div>
  );
}

export default App;
