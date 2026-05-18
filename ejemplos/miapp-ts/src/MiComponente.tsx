import { Component } from 'react';

class MiComponente extends Component {
    
    constructor(props:any) {
        super(props)
        console.log('construyendo mi componente')
    }

  componentDidMount() {
        console.log('montando mi componente')
  }

  componentDidUpdate(prevProps:any, prevState:any) {
        console.log('actualizando mi componente')

  }

  componentWillUnmount() {
    console.log('desmontando mi componente')
  }


    render() {
      console.log('en el render');
      return (
        <h1>Mi Componente</h1>
      )
    }
}

export default MiComponente;