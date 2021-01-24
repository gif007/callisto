$(document).ready(function(){
    // Page has loaded

    $("button#get_action").click(function(){
        $.get('/game/get_action/', function(data, status){
            performAction(data);
        });
    });

    function performAction(action) {
        $('#action-view').text(action.text);
        if (action.monster) {
            battle(action);
        };
    };

    function battle(action) {
        $('#action-view').append(`<br />Monster: ${action.monster}`);
        $('#action-view').append(`<br /><button id='attack'>Attack!</button><button id='flee'>Flee!</button>`);
        $('button#attack').click(function(){
            alert('You shoot bullets!!!');
        });
        $('button#flee').click(function(){
            window.location = '/game/workshop';
        });
    };
    
    // End of set up
});

