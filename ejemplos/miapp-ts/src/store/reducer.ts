import { Action, State } from './types';

export const initialState: State = {
  count: 0,
};

export function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 };
    case 'DECREMENT':
      return { ...state, count: state.count - 1 };
    case 'SET':
      return { ...state, count: action.payload };
    default:
      return state;
  }
}

