$(document).ready(function(){
    // Page has loaded

    $("button#continue").click(function(){
        // This is the get random event function of the Continue button
    
        let getAction = function () {
            let xhttp = new XMLHttpRequest();
    
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    eventController(JSON.parse(this.responseText));
                    // console.log(JSON.parse(this.responseText));
                   
                };
            };
    
            xhttp.open('GET', '/game/deploy/get_action/', true);
            xhttp.send();
        }();
        });

    function eventController(rsp) {
        // This displays the current event

        // update view

        console.log(rsp['action']);
    };

    function displayAttack(action) {
        // This displays the results of the attack round

        // update view

        console.log(action);
    };
    

    function requestAttack() {
        // This is called by the Attack button
        let xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                displayAttack(JSON.parse(this.responseText));
            };
        };

        xhttp.open('GET', '/game/deploy/attack', true);
        xhttp.send();
    };
    
    // End of set up
});

