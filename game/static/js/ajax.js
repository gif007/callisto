function continueBtn(){
    let btn = document.createElement('button');
    btn.innerText = 'Continue';
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', getEvent);

    return btn;
}

function attackBtn(){
    let btn = document.createElement('button');
    btn.innerText = 'Attack';
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', getEvent);

    return btn;
}

function examineBtn(){
    let btn = document.createElement('button');
    btn.innerText = 'Examine';
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', getEvent);

    return btn;
}

function fleeBtn(){
    let btn = document.createElement('button');
    btn.innerText = 'Flee';
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', getEvent);

    return btn;
}

const ALL_BUTTONS = {
    'continue': ()=> continueBtn(),
    'attack': ()=> attackBtn(),
    'examine': ()=> examineBtn(),
    'flee': ()=> fleeBtn(),
};

function getEvent() {
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            eventController(JSON.parse(this.responseText));
            // console.log(JSON.parse(this.responseText));
           
        };
    };

    xhttp.open('GET', '/game/deploy/get_action/', true);
    xhttp.send();
}

function eventController(rsp) {
    // Update the UI
    updateUI(rsp['event']);

    if (rsp['buttons']) {
        populateButtonGroup(rsp['buttons']);
    }

    console.log(rsp['event']);

    function updateUI(event) {
        document.querySelector('h2#title').innerText = event['name'];
        document.querySelector('p#desc').innerText = event['desc'];
        document.querySelector('img#img').setAttribute('src', event['img']);
    }

    function populateButtonGroup(buttons){
        let btngrp = document.querySelector('div#btngrp');
        wipeButtonGroup();
        buttons.forEach(button=>{
            let btn = ALL_BUTTONS[button]();
            btngrp.append(btn);
        })

        function wipeButtonGroup() {
            while (btngrp.firstChild) {
                btngrp.removeChild(btngrp.firstChild);
            }
        }
    }
};

function attackController(action) {
    // This displays the results of the attack round

    // update view

    console.log(action);
};


function getAttack() {
    // This is called by the Attack button
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            attackController(JSON.parse(this.responseText));
        };
    };

    xhttp.open('GET', '/game/deploy/attack', true);
    xhttp.send();
};


$(document).ready(function(){
    // Page has loaded
    document.querySelector('button#continue').addEventListener('click', getEvent);

});
