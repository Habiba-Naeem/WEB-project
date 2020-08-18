function count(){
    var count = 0;
    document.querySelectorAll("#cart-item-total").forEach( t =>{
        count = parseFloat(t.dataset.total) + count;
    })
    document.querySelector("#total").textContent = "$" + count.toFixed(2);
    document.querySelector("#totalhidden").value = count.toFixed(2);
    return count.toFixed(2);    
}

document.addEventListener('DOMContentLoaded', () => {
    var rows = document.querySelectorAll(".row");
    var cancel = document.querySelectorAll(".cancel");

    rows.forEach( row => {
        const prices = row.querySelector("#product-price");
        const quantity = row.querySelector("#quantity");
        var total = row.querySelector("#cart-item-total");
    
        total.textContent = "$" +  (prices.dataset.price * parseInt(quantity.value)).toFixed(2);
        total.setAttribute("data-total", `${(prices.dataset.price * parseInt(quantity.value)).toFixed(2)}`);
        
        quantity.addEventListener("change",()=>{
            total.textContent = "$" +  (prices.dataset.price * parseInt(quantity.value)).toFixed(2);
            total.setAttribute("data-total", `${(prices.dataset.price * parseInt(quantity.value)).toFixed(2)}`);
            count();

            const request = new XMLHttpRequest();
            request.open('GET', `/cart/quantity/${row.id}/${quantity.value}`);

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                if( data.success ){
                    alert("added");
                }
                else {
                    console.log("unsuccessful")
                }
            };

            request.send();
            return false;
        })
    })
    count();

    cancel.forEach( can =>{
        can.addEventListener("click", ()=>{
            const parent = can.parentNode.parentNode;
            const id = parent.id;
            console.log(id);

            var table = document.querySelector("#table");
            table.deleteRow(parent.rowIndex);
            count();

            const request = new XMLHttpRequest();
            request.open('GET', `/cart/cancel/${id}`, true);

            request.send();
            return false;
            
        })
    })
/*
    var submit_order = document.querySelector("#submit_order");

    submit_order.addEventListener("click", ()=>{
        
        rows.forEach( row => {
            const quantity = row.querySelector("#quantity");
            row.append(row.id);
            q.append(quantity.value);
            
        })
        item = {
            "rowid": row,
            "quantity": q
        }
        console.log(item)
        const convert = JSON.stringify(item);
        //document.querySelector("#payment-form").action = `/cart/order/${convert}`;
    })*/

})