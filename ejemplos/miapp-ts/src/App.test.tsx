import { render, screen } from '@testing-library/react';
import App from './App';

test('muestra el menú de ejemplos del curso', () => {
  render(<App />);
  expect(screen.getByRole('heading', { name: /ejemplos/i })).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /props y tipos/i })).toBeInTheDocument();
});
