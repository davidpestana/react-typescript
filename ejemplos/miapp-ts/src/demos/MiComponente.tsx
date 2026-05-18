import { Component } from 'react';

type MiComponenteProps = Record<string, never>;

class MiComponente extends Component<MiComponenteProps> {
  constructor(props: MiComponenteProps) {
    super(props);
    console.log('constructor: MiComponente');
  }

  componentDidMount() {
    console.log('componentDidMount: MiComponente');
  }

  componentDidUpdate(prevProps: MiComponenteProps) {
    console.log('componentDidUpdate: MiComponente', { prevProps });
  }

  componentWillUnmount() {
    console.log('componentWillUnmount: MiComponente');
  }

  render() {
    return (
      <div>
        <p>Abre la consola del navegador (F12) para ver los mensajes del ciclo de vida.</p>
        <h3>MiComponente (clase)</h3>
      </div>
    );
  }
}

export default MiComponente;
