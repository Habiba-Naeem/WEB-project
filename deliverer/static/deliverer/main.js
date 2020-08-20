document.addEventListener('DOMContentLoaded', () =>{
    var confirm_delivery = document.querySelectorAll(".confirm_delivery");

    confirm_delivery.forEach(d =>{
        d.addEventListener("click", ()=>{
            var id = d.parentElement.parentElement.parentElement;
            console.log(id)
            id = parseInt(id.dataset.order)
            const request = new XMLHttpRequest();
            request.open('GET', `/deliverer/${id}`);
            request.onload = () => {
                const data = JSON.parse(request.responseText);
                if(data.success){
                    alert("successful")
                    var status = document.querySelectorAll(".status");
                    status.forEach(s=>{
                        var parent = s.parentElement.parentElement;
                        if (id === parseInt(parent.dataset.order)){
                            s.innerHTML = "Delivered"; 
                            s.className = " mx-auto alert alert-success py-2 ";
                        }
                    })
                }
                else{
                    alert("unsuccesssufl")
                }
            };
            request.send();
            return false;
        })
    })
})