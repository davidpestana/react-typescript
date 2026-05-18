import React, { createContext, useContext, useMemo, useReducer } from 'react';
import { initialState, reducer } from './reducer';
import { Action, State } from './types';

type Store = {
  state: State;
  dispatch: React.Dispatch<Action>;
};

const StoreContext = createContext<Store | undefined>(undefined);

export const StoreProvider = ({ children }: { children: React.ReactNode }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const value = useMemo(() => ({ state, dispatch }), [state]);

  return <StoreContext.Provider value={value}>{children}</StoreContext.Provider>;
};

export const useStore = () => {
  const context = useContext(StoreContext);
  if (!context) throw new Error('useStore must be used inside StoreProvider');
  return context;
};

