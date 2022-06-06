var typing = document.getElementById('typing');
var typewriter = new Typewriter(typing, {});
        
typewriter
        .typeString('안녕하십니까. 만나서 반갑습니다.')
    .pauseFor(1500)
        .typeString('<br/>')
    .typeString('우리는 모두 인생을 어떻게 살지 고민합니다. 직업이란 인생의 몇가지 선택사항과 같습니다.')
    .pauseFor(1500)  
        .typeString('<br/>') 
    .typeString('여기서 개발자는 프론트, 백엔드... 여러 선택사항이 있습니다.') 
    .pauseFor()                                       
    .start();

    typewriter.pauseFor(1000);
