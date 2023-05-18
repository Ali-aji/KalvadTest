var updateButtons = document.getElementsByClassName('update-cart')

for(i=0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function (){
        var productId = this.dataset.product
        var action = this.dataset.action

        if (user == 'AnonymousUser'){
			//  default items
            console.log("AnonymousUser")
		}else{
			updateUserCart(productId, action)
		}

    })

}

function updateUserCart(productId, action){

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        location.reload()
        console.log(data)
    });
}