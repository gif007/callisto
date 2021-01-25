$(document).ready(function(){
    // Page has loaded

    // $("button#get_action").click(function(){
    //     $.get('/game/get_action/', function(data, status){
    //         performAction(data);
    //     });
    // });

    $("button#get_action").click(function(){
        getAction();
        });

    function performAction(action) {
        $('#action-view').text(action['text']);
        if (action['enemy']) {
            battle(action);
        };
        $('#action-view').append(`Still using: ${action['mech']}`);
        // console.log(action);
    };

    function battle(action) {
        $('#action-view').append(`<br />Enemy: ${action['enemy']}`);
        $('#action-view').append(`<br /><button id='attack'>Attack!</button><button id='flee'>Flee!</button>`);
        $('button#attack').click(function(){
            alert('You shoot bullets!!!');
        });
        $('button#flee').click(function(){
            window.location = '/game/deploy/flee';
        });
    };

    function getAction() {
        let xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                performAction(JSON.parse(this.responseText));
            };
        };

        xhttp.open('GET', '/game/get_action/', true);
        xhttp.send();
    };
    
    // End of set up
});

