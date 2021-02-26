function continueBtn(){
    // Return a continue button that calls for a random event
    let btn = document.createElement('button');
    btn.innerText = 'Continue';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('event', eventController);
    });

    return btn;
}

function attackBtn(){
    // Return an attack button that initiates a battle
    let btn = document.createElement('button');
    btn.innerText = 'Attack';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('attack', attackController);
    });

    return btn;
}

function attackContinueBtn(){
    // Return an attack button that calls a single round of battle
    let btn = document.createElement('button');
    btn.innerText = 'Continue';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('attack-round', attackRoundController);
    });

    return btn;
}

function examineBtn(){
    // Return an examination button that calls a detail of a Discovery event
    let btn = document.createElement('button');
    btn.innerText = 'Examine';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        console.log('not yet implemented')
    });

    return btn;
}

function fleeBtn(){
    // Return a flee button that exits combat and returns user to workshop
    let btn = document.createElement('button');
    btn.innerText = 'Flee';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        window.location = '/game/deploy/flee';
    });

    return btn;
}

// Pack buttons
const ALL_BUTTONS = {
    'continue': ()=> continueBtn(),
    'attack': ()=> attackBtn(),
    'attack-continue': ()=> attackContinueBtn(),
    'examine': ()=> examineBtn(),
    'flee': ()=> fleeBtn(),
};


function getResource(url, cb) {
    // Places a call to the deployment API for a json response
    fetch(url)
        .then(res => res.json())
        .then(data => cb(data))
}


function wipeButtonGroup() {
    // Empties the action button group
    while (btngrp.firstChild) {
        btngrp.removeChild(btngrp.firstChild);
    }
}


function eventController(res) {
    // Updates the UI according to which event is received
    updateUI(res['event']);

    if (res['buttons']) {
        populateButtonGroup(res['buttons']);
    }

    console.log(res['event']); // Log the event

    function updateUI(event) {
        // Updates top row of deployment UI to inform user of current event
        document.querySelector('h2#title').innerText = event['name'];
        document.querySelector('p#desc').innerText = event['desc'];
        document.querySelector('img#img').setAttribute('src', event['img']);
    }

    function populateButtonGroup(buttons){
        // Updates action button group according to which even was received
        let btngrp = document.querySelector('div#btngrp');

        wipeButtonGroup();

        buttons.forEach(button=>{
            let btn = ALL_BUTTONS[button]();
            btngrp.append(btn);
        })
    }
};

function attackController(res) {
    // This displays the results of the attack round
    updateUI(res);
    populateButtonGroup();

    function updateUI(res) {
        // Updates top row of deployment UI to inform user of current event
        document.querySelector('h2#title').innerText = `Battle`;
        document.querySelector('p#desc').innerText = `You have engaged the enemy!\n${res.combat_order.firstPlayer} goes first.`;
        document.querySelector('img#img').setAttribute('src', '/static/img/attacking.png');

        document.querySelector('div.Arena').style.display = 'flex';

        document.querySelector('img#enemyimg').setAttribute('src', res.enemy.img);
        document.querySelector('p#enemyhealth').innerText = `${res.enemy.health}`;


        document.querySelector('img#mechimg').setAttribute('src', res.mech.img);
        document.querySelector('p#mechhealth').innerText = `${res.mech.health}`;

    }

    function populateButtonGroup() {
        let btngrp = document.querySelector('div#btngrp');
        wipeButtonGroup();

        let _continue = ALL_BUTTONS['attack-continue']();
        let flee = ALL_BUTTONS['flee']();
        btngrp.append(_continue, flee);
        }

    console.log(res);
};

function attackRoundController(rsp) {
    document.querySelector('p#desc').innerText = `${rsp.first_player} attacks ${rsp.second_player} first!`;
    console.log(rsp.move);
}


window.onload = function(){
    // Page has loaded
    document.querySelector('button#continue').addEventListener('click', ()=> {
        getResource('event', eventController);
    });
    document.querySelector('#exit').addEventListener('click', function(){
        window.location = '/game/deploy/flee';
    });

};
