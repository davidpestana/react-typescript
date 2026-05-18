const generador = (cadena:string) => () => { 
    const textoIntro = new Array(16).join('wat') + ' Batman!' ;
    const configSpeech = new SpeechSynthesisUtterance(textoIntro);
    configSpeech.rate = 0.8;
    window.speechSynthesis.speak(configSpeech);

}

export default generador