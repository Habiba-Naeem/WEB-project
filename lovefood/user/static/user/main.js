document.addEventListener('DOMContentLoaded', () => {
    //buttons
    var add_to_cart =  document.querySelectorAll(".add-to-cart");
    
    add_to_cart.forEach(cart =>{
        //add the selected product to cart
        cart.addEventListener("click", ()=>{

            var dishdiv = cart.parentElement.parentElement;
            dishid = dishdiv.dataset.dishid;
            restaurantid = dishdiv.dataset.restaurantid; 
            //the object item
            const item = {
                "dishid": dishid,
                "restaurantid": restaurantid
            }
            const convert = JSON.stringify(item);

            //request
            const request = new XMLHttpRequest();
            request.open('GET', `/cart/cart_item/${convert}`, true);

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                if (data.success){
                    alert("Added to cart!");
                }
                else{
                    alert("Please login to add to cart");
                }
            }
            
            request.send();
            return false;
        }) 
    })
    

})