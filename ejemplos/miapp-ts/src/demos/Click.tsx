import type { MouseEvent } from 'react';

const Click = () => {
  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    const textoIntro = `${'wat'.repeat(16)} Batman!`;
    const utterance = new SpeechSynthesisUtterance(textoIntro);
    utterance.rate = 0.8;
    window.speechSynthesis.speak(utterance);
  };

  return (
    <div>
      <p>Pulsa el botón para probar un manejador de evento tipado.</p>
      <button type="button" onClick={handleClick}>
        Que suene la intro
      </button>
    </div>
  );
};

export default Click;
