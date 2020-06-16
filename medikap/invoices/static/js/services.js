var updateButtons = document.getElementsByClassName('update-invoice')
for(i = 0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(){
        var serviceId = this.dataset.service
        var action = this.dataset.action
        var quantity = document.getElementById(serviceId).value
        console.log('serviceId:', serviceId, 'action:', action, 'quan:', quantity)

        if (updateButtons.length > 0) {
            updateInvoiceServices(serviceId, action, quantity)
        }
    })
}


function updateInvoiceServices(serviceId, action, quantity){
    var url = '/invoices/update_invoice/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({
            'serviceId' : serviceId,
            'action' : action,
            'quantity' : quantity
            })
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })
}