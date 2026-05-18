import { StoreProvider, useStore } from '../store/store';
import { decrement, increment } from '../store/actions';

function Contador() {
  const { state, dispatch } = useStore();

  return (
    <div className="contador-demo">
      <p>Contador con <code>useReducer</code> y contexto (patrón tipo Redux).</p>
      <div className="contador-demo__controls">
        <button type="button" onClick={() => dispatch(decrement())} aria-label="Decrementar">
          −
        </button>
        <span className="contador-demo__valor">{state.count}</span>
        <button type="button" onClick={() => dispatch(increment())} aria-label="Incrementar">
          +
        </button>
      </div>
    </div>
  );
}

export default function ContadorReduxDemo() {
  return (
    <StoreProvider>
      <Contador />
    </StoreProvider>
  );
}
