function continueButton(){
    // Return a continue button that calls for a random event
    let btn = document.createElement('button');
    btn.innerHTML = 'Continue';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('event', eventController);
    });

    return btn;
}


function engageButton(){
    // Return an attack button that initiates a battle
    let btn = document.createElement('button');
    btn.innerHTML = 'Engage';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('engage', engageController);
    });

    return btn;
}


function attackButton(){
    // Return an attack button that calls a single round of battle
    let btn = document.createElement('button');
    btn.innerHTML = 'Attack';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        getResource('attack', attackController);
    });

    return btn;
}


function examineButton(){
    // Return an examination button that calls a detail of a Discovery event
    let btn = document.createElement('button');
    btn.innerHTML = 'Examine';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        console.log('not yet implemented')
    });

    return btn;
}


function fleeButton(){
    // Return a flee button that exits combat and returns user to workshop
    let btn = document.createElement('button');
    btn.innerHTML = 'Flee';
    btn.setAttribute('type', 'button');

    btn.addEventListener('click', ()=> {
        window.location = '/game/deploy/flee';
    });

    return btn;
}


// Pack buttons
const ALL_BUTTONS = {
    'continue': ()=> continueButton(),
    'engage': ()=> engageButton(),
    'attack': ()=> attackButton(),
    'examine': ()=> examineButton(),
    'flee': ()=> fleeButton(),
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
        document.querySelector('h2#title').innerHTML = event['name'];
        document.querySelector('p#desc').innerHTML = event['desc'];
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

function engageController(res) {
    // This displays the results of engaging the enemy
    updateUI(res);
    populateButtonGroup();

    function updateUI(res) {
        // Updates top row of deployment UI to inform user of current event
        document.querySelector('h2#title').innerHTML = `Battle`;
        document.querySelector('p#desc').innerHTML = `You have engaged the enemy!\n${res.combat_order.firstPlayer} goes first.`;
        document.querySelector('img#img').setAttribute('src', '/static/img/attacking.png');

        document.querySelector('div.Arena').style.display = 'flex';

        document.querySelector('img#enemyimg').setAttribute('src', res.enemy.img);
        document.querySelector('p#enemyhealth').innerHTML = `${res.enemy.health}`;


        document.querySelector('img#mechimg').setAttribute('src', res.mech.img);
        document.querySelector('p#mechhealth').innerHTML = `${res.mech.health}`;

    }

    function populateButtonGroup() {
        let btngrp = document.querySelector('div#btngrp');
        wipeButtonGroup();

        let _continue = ALL_BUTTONS['attack']();
        let flee = ALL_BUTTONS['flee']();
        btngrp.append(_continue, flee);
        }

    console.log(res);
};

function attackController(res) {
    if (res.dead) {
        console.log(res.dead);
        return
    }

    if (res.mechdied) {
        window.location = '/game/deploy/flee';
        return
    }

    if (res.loot) {
        for (loot in res.loot) {
            console.log(loot + ': ' + res.loot[loot]);
        }
        document.querySelector('p#enemyhealth').innerHTML = `${res.enemy_health}`;
        
        return ;
    }
    document.querySelector('p#desc').innerHTML = `${res.first_player.name} attacks ${res.second_player.name} first!`;
    document.querySelector('p#enemyhealth').innerHTML = `${res.enemy_health}`;
    document.querySelector('p#mechhealth').innerHTML = `${res.mech_health}`;

    console.log(res);
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
