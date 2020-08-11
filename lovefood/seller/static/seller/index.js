document.addEventListener('DOMContentLoaded', () => {

})
//window.addEventListener('load', (event) => {

window.onload = function () {
    const seller = document.getElementById('seller-name').innerHTML;
    console.log(seller);
    getlist(seller);
}
//});

function getlist(seller) {
    fetch(`${seller}/getlist`)
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
        seller = document.getElementById('seller-name').innerHTML;
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
        getItem(seller, dish_name, dish_id);
    }
});
function getItem(seller, dish_name, dish_id) {
    fetch(`${seller}/get${dish_id}`)
        .then(response => {
            console.log('Response:', response)
            return response.json();
        })
        .then(data => {
            addItem(data.item, seller, dish_id);

        })
};

function addItem(content, seller, dish_id) {
    console.log(content["name"]);
    console.log(content["summary"]);
    console.log(content["nationality"]);
    console.log(content["no_of_serving"]);
    console.log(content["picture"]);
    console.log(content["glutten_free"]);
    console.log(content["customizable"]);

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

    /* namediv = document.createElement('div');
     namediv.className = "namediv";
     name = document.createElement('p');
     name.className = "dish-name";
     name.innerHTML = content["name"];
 */
    console.log("appendingdone");

    console.log("In append function");
    const dish = document.getElementById('dish');
    dish.append(namediv);
    dish.append(summarydiv);
    dish.append(nationalitydiv);
    dish.append(no_of_servingdiv);
    dish.append(glutten_freediv);
    dish.append(customizablediv);
    console.log("appended to main div");
    display_items(seller, content["name"], dish_id);
    //console.log(document.getElementById('testing').innerHTML);
}


function display_items(seller, dish_name, dish_id) {
    // Open new request to get render page.
    console.log("ok");

    const request = new XMLHttpRequest();
    // request.open('GET', '/seller/' + seller + '/' + dish_name);
    request.open(`GET`, `/seller/${seller}/get_dish_no_${dish_id}`, true);
    //request.open('GET', `/price/${item_name}/${size}`, true)
    request.onload = () => { window.location.replace(`${seller}/${dish_id}`) };
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