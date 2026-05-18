const Click = () => {
  const handleClick = (event:React.MouseEvent<HTMLButtonElement>) => {
    console.log(event)
    const textoIntro = new Array(16).join('wat') + ' Batman!';
    const configSpeech = new SpeechSynthesisUtterance(textoIntro);
    configSpeech.rate = 0.8;
    window.speechSynthesis.speak(configSpeech);
  }

    return (
      <div>
        <button type="button" onClick={handleClick}>Que suene la intro</button>
      </div>
    )
}

export default Click