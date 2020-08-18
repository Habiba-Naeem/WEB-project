document.addEventListener('DOMContentLoaded', () => {
  
})
//window.addEventListener('load', (event) => {

window.onload = function () {
    getlist();
}
function getlist() {
    fetch(`getlist`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            console.log(data.itemlist);
            data.itemlist.forEach(addlistmemeber);
        })
};

function addlistmemeber(member) {
    console.log("member:")
    console.log(member);
    const list = document.getElementById('dish-list');
    itemdiv = document.createElement('div');
    item = document.createElement('a');
    item.innerHTML = member["dish_id"] + ": " + member["dish_name"];
    item.className = "dish-list-item";
    item.href = "#";
    itemdiv.append(item);
    list.append(itemdiv);
};

document.addEventListener('click', event => {

    const element = event.target;
    if (element.className === 'dish-list-item') {
        //itemdiv = element.parentElement;
        dish_name = element.innerHTML;
        console.log(dish_name);
        count = 0;
        for (i = 0; i <= dish_name.length; i++) {
            if (dish_name.charAt(i) === ":") {
                break;
            }
            count++;
            console.log(count);
        }
        dish_id = dish_name.substring(0, count);
        console.log(dish_id);
        getItem( dish_name, dish_id);
    }
});
function getItem(dish_name, dish_id) {
    fetch(`get${dish_id}`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            console.log("here")
            console.log(data.item["name"])
            addItem(data.item, dish_id);
        })
};

function addItem(content, dish_id) {
    console.log(content["name"]);
    console.log(content["summary"]);
    console.log(content["nationality"]);
    console.log(content["no_of_serving"]);
    console.log(content["picture"]);
    console.log(content["glutten_free"]);
    console.log(content["customizable"]);    
    console.log(content["price"]);

    const namediv = document.createElement('div');
    namediv.className = "namediv";
    const name = document.createElement('p');
    name.className = "dish-name";
    name.innerHTML = content["name"];
    namediv.append(name);

    const summarydiv = document.createElement('div');
    summarydiv.className = "summarydiv";
    const summary = document.createElement('p');
    summary.className = "dish-summary";
    summary.innerHTML = content["summary"];
    summarydiv.append(summary);

    const nationalitydiv = document.createElement('div');
    nationalitydiv.className = "nationalitydiv";
    const nationality = document.createElement('p');
    nationality.className = "dish-nationality";
    nationality.innerHTML = content["nationality"];
    nationalitydiv.append(nationality);

    const no_of_servingdiv = document.createElement('div');
    no_of_servingdiv.className = "no_of_servingdiv";
    const no_of_serving = document.createElement('p');
    no_of_serving.className = "dish-no_of_serving";
    no_of_serving.innerHTML = content["no_of_serving"];
    no_of_servingdiv.append(no_of_serving);

    const glutten_freediv = document.createElement('div');
    glutten_freediv.className = "glutten_freediv";
    const glutten_free = document.createElement('p');
    glutten_free.className = "glutten_free-name";
    glutten_free.innerHTML = content["glutten_free"];
    glutten_freediv.append(glutten_free);

    const customizablediv = document.createElement('div');
    customizablediv.className = "customizablediv";
    const customizable = document.createElement('p');
    customizable.className = "customizable-name";
    customizable.innerHTML = content["customizable"];
    customizablediv.append(customizable);

    const pricediv = document.createElement('div');
    pricediv.className = "pricediv";
    const price= document.createElement('p');
    price.className = "dish-price-name";
    price.innerHTML = content["price"];
    pricediv.append(price);
    console.log("appendingdone");

    console.log("In append function");

    const dishdiv = document.createElement('div');
    console.log(dishdiv)
    
    dishdiv.append(namediv);
    dishdiv.append(summarydiv);
    dishdiv.append(nationalitydiv);
    dishdiv.append(no_of_servingdiv);
    dishdiv.append(glutten_freediv);
    dishdiv.append(customizablediv);
    dishdiv.append(pricediv)
    console.log("appended to main div");
    display_items(content["name"], dish_id);
    //console.log(document.getElementById('testing').innerHTML);
}


function display_items(dish_name, dish_id) {
    // Open new request to get render page.
    console.log("ok");

    const request = new XMLHttpRequest();
    // request.open('GET', '/seller/' + seller + '/' + dish_name);
    request.open(`GET`, `/seller/${dish_id}`, true);
    //request.open('GET', `/price/${item_name}/${size}`, true)
    request.onload = () => { window.location.replace(`${dish_id}`) };
    request.send();
    console.log("ok2")
}
/*
          const request = new XMLHttpRequest();
          request.open('POST', '/retrievemessages');
          request.onload = () => {
              const data = JSON.parse(request.responseText);
              data.forEach(add_message);
          };
          const data = new FormData();
          data.append('channel', channel)

          request.send(data);
*/