const card = document.querySelector('div.MechCardEquipment');

card.addEventListener('click', e => {
    let id = e.target.getAttribute('item-id');
    let typ = e.target.getAttribute('item-type');
    let _class = e.target.getAttribute('item-class');
    if (!id | !typ) {return};
    let url = `/game/workshop/equipment/${typ}/${id}`;
    getResource(url, itemController, _class);
    
})


function getResource(url, cb, _class) {
    // Places a call to the equipment API for a json response
    fetch(url)
        .then(res => res.json())
        .then(data => cb(data, _class))
}


function itemController(rsp, _class) {
    let name = document.createElement('h3');
    let category = document.createElement('p');
    let desc = document.createElement('p');
    let armor = document.createElement('p');

    name.innerHTML = `${rsp.name}`;
    category.innerHTML = `${_class}`;
    desc.innerHTML = `"${rsp.desc}"`;
    armor.innerHTML = `+${rsp.armor} Armor`;

    name.style.cssText = 'font-size: 1.125rem; font-weight: bold;';

    desc.style.cssText = 'font-style: italic;'

    let descriptors = [name, category, armor];

    if (rsp.sight) {
        let sight = document.createElement('p');
        sight.innerHTML = `+${rsp.sight} Sight`;
        descriptors.push(sight);
    }

    if (rsp.speed) {
        let speed = document.createElement('p');
        speed.innerHTML = `+${rsp.speed} Speed`;
        descriptors.push(speed);
    }

    if (rsp.firepower) {
        let firepower = document.createElement('p');
        firepower.innerHTML = `+${rsp.firepower} Firepower`;
        descriptors.push(firepower);
    }

    if (rsp.firerate) {
        let firerate = document.createElement('p');
        firerate.innerHTML = `+${rsp.firerate} Firerate`;
        descriptors.push(firerate);
    }

    descriptors.push(desc);

    let container = document.querySelector('div.MechCardItem');

    if (container.style.display !== 'block') {
        container.style.display = 'block';
    }

    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    descriptors.forEach(a=> {
        container.append(a);
    })

    console.log(rsp, _class);
}


const equip = document.querySelector('h3#equip');
const equipment = document.querySelector('div#equipment');
const stats = document.querySelector('h3#stats');
const statblock = document.querySelector('div#statblock');

equip.addEventListener('click', function(){
    if (equip.className != 'MechCardEquipActive') {
        equip.className = 'MechCardEquipActive';
        stats.className = 'MechCardStatsInactive';
        equipment.style.display = 'flex';
        statblock.style.display = 'none';
    }
})

stats.addEventListener('click', function(){
    if (stats.className != 'MechCardStatsActive') {
        equip.className = 'MechCardEquipInactive';
        stats.className = 'MechCardStatsActive';
        statblock.style.display = 'flex';
        equipment.style.display = 'none';
    }
})

const healbutton = document.querySelector('span#healbutton');

healbutton.addEventListener('click', ()=>{
    fetch('/game/workshop/heal')
        .then(res => res.json())
        .then(data => document.querySelector('span#health').innerHTML = data.mech_health)
})