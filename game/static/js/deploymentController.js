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

function fireButton(){
    // Return a fire button that calls a round of battle on behalf of the mech
    let btn = document.createElement('button');
    btn.innerHTML = 'Fire';
    btn.setAttribute('type', 'button');
    btn.setAttribute('id', 'firebutton');
    btn.style.cssText = 'width: 100%; margin-top: 1rem;';

    btn.addEventListener('click', ()=>{
        getResource('attack', attackController);
    })

    return btn
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
    'fire': ()=> fireButton(),
    'examine': ()=> examineButton(),
    'flee': ()=> fleeButton(),
};


async function getResource(url, cb) {
    // Places a call to the deployment API for a json response
    try {
        let resource = await fetch(url);

        if (!resource.ok) {
            throw new Error('The requested resource could not be found');
        } else {
            let data = await resource.json();
            cb(data);
        }
    } catch (err) {
        console.log(err.message);
    }
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
    wipeButtonGroup();

    function updateUI(res) {
        // Updates top row of deployment UI to inform user of current event
        document.querySelector('h2#title').innerHTML = `Battle`;
        document.querySelector('p#desc').innerHTML = `You have engaged the enemy!\n${res.currentPlayer.name} goes first.`;
        document.querySelector('img#img').setAttribute('src', '/static/img/attacking.png');

        document.querySelector('div.Arena').style.display = 'flex';

        document.querySelector('img#enemyimg').setAttribute('src', res.enemy.img);
        document.querySelector('p#enemyhealth').innerHTML = `${res.enemy.health}`;


        document.querySelector('img#mechimg').setAttribute('src', res.mech.img);
        document.querySelector('p#mechhealth').innerHTML = `${res.mech.health}`;

        if (res.currentPlayer.isMech) {
            let fireButton = ALL_BUTTONS['fire']();
            document.querySelector('div#mechstats').appendChild(fireButton);
            document.querySelector('img#enemyimg').classList.remove('Attacking');
            document.querySelector('img#mechimg').classList.add('Attacking');
        } else {
            document.querySelector('img#mechimg').classList.remove('Attacking');
            document.querySelector('img#enemyimg').classList.add('Attacking');
            // call attack for enemy
        }
    }
    console.log(res);
};

function attackController(res) {
    // Initiate a round of combat
    if (res.dead) { // dummy code to handle enemy death gracefully until looting system is set up
        console.log(res.dead);
        
        return
    }

    if (res.mechdied) { // You failed in combat and are sent back to the workshop
        window.location = '/game/deploy/flee';
        return
    }

    if (res.loot) {
        // Dummy code to display dummy loot
        document.querySelector('p#enemyhealth').innerHTML = `${res.enemy_health}`;
        document.querySelector('img#enemyimg').classList.remove('Attacking');
        document.querySelector('img#mechimg').classList.add('Attacking');
        let lootList = [];
        for (loot in res.loot) {
            lootList.push(`${loot}: ${res.loot[loot]}`);
        };
        let lootString = lootList.join(', ');
        document.querySelector('p#desc').innerHTML = `Mech is victorious!<br />Loot: ${lootString}`;
        
        return ;
    }
    if (res.isMech) {
        document.querySelector('p#desc').innerHTML = `Mech is attacking`;
        document.querySelector('img#enemyimg').classList.remove('Attacking');
        document.querySelector('img#mechimg').classList.add('Attacking');
    } else {
        document.querySelector('p#desc').innerHTML = `Enemy is attacking`;
        document.querySelector('img#mechimg').classList.remove('Attacking');
        document.querySelector('img#enemyimg').classList.add('Attacking');
    }

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
