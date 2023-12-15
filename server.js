//express 쓰기 위한 기본적인 문법
const express = require('express');

const app = express(); //express 인스턴스

//서버 어디다가 열지 설정
//8080 포트에 서버 띄워달라

app.listen(8080, function(){
    console.log('listen on 8080') 
}); 
//http://localhost:8080 주소 치고 들어가면 Cannot GET / 메세지 뜸

app.get('/my', function(요청, 응답){
    응답.send('펫 용품할 수 있는 사이트 입니다.')
});