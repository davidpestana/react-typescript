import { Action } from './types';

export const increment = (): Action => ({ type: 'INCREMENT' });
export const decrement = (): Action => ({ type: 'DECREMENT' });
export const setCount = (value: number): Action => ({ type: 'SET', payload: value });

