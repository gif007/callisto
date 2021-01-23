$(document).ready(function(){
    $("#get_action").click(function(){
        $.get('/game/get_action/', function(data, status){
            alert("Data: " + data.data + "\nStatus: " + status);
        });
    });
});