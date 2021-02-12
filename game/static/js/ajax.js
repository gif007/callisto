$(document).ready(function(){
    // Page has loaded

    $("button#get_action").click(function(){
        // This is the getRandomEvent function of the Continue button
    
        let getAction = function () {
            let xhttp = new XMLHttpRequest();
    
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    performAction(JSON.parse(this.responseText));
                    // console.log(JSON.parse(this.responseText));
                   
                };
            };
    
            xhttp.open('GET', '/game/deploy/get_action/', true);
            xhttp.send();
        }();
        });

    function performAction(rsp) {
        // $('#attack').remove();
        // $('#flee').remove();
        // $('.deployed-card-text').text(action['text']);
        
        // if (action['enemy']) {
        //     $('#get_action').remove();
        //     battle(action);
        // };
        console.log(rsp['action']);
    };

    function performAttack(action) {
        // $('#attack').remove();
        // $('#flee').remove();
        // $('.deployed-card-text').text(action['text']);
        
        // if (action['enemy']) {
        //     $('#get_action').remove();
        //     battle(action);
        // };
        console.log(action);
    };

    function battle(action) {
        $('.deployed-card-text').text(`You have engaged in combat with ${action['enemy']}`);
        $('.deployed-card-button-group').prepend(`<button id='attack'>Attack!</button><button id='flee'>Flee!</button>`);
        $('button#attack').click(function(){
            attack();
        });
        $('button#flee').click(function(){
            window.location = '/game/deploy/flee';
        });
    };

    

    function attack() {
        let xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                performAttack(JSON.parse(this.responseText));
            };
        };

        xhttp.open('GET', '/game/deploy/attack', true);
        xhttp.send();
    };
    
    // End of set up
});

