document.addEventListener('DOMContentLoaded', () => {
    alert("I am working!")
    getlist();
    // getitems();

    function getlist() {
        fetch(`/getlist`)
            .then(response => response.json())
            .then(data => {
                data.itemlist.forEach(addlistmemeber);
            })

    }

    function addlistmemeber(member) {
        list = document.getElementById('dish-list');
        itemdiv = document.createElement('div');
        item = document.createElement('p');
        item.innerHTML = member;
        item.className = "list-item";
        itemdiv.append(item);
        list.append(itemdiv);
    }

    /* function getitems() {
         //const start = 1;
         // const end = 10;
         //counter = end + 1;
         seller_name = document.getElementById('seller_name').innerHTML;
         // Get new posts and add posts
         fetch(`/getitems`)
             .then(response => response.json())
             .then(data => {
                 //data.items.forEach(addItem);
             })
     };
 
     function addItem(content) {
         item = document.createElement('div');
         item.className = "item";
 
 
     }
 */
})