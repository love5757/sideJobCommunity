var chicken = new Object();
    chicken.title = "삼성전자의 공채사원을 모집합니다";
    chicken.name = "(주)삼성전자";
    chicken.content = "공채사원을 모집합니다. 할 사람? 손";
    JSON.stringify(chicken);

    new Vue({

        el: '#app',
        data: chicken
    })