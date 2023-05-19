var updateButtons = document.getElementsByClassName('update-cart');
let $allLinePrice = $(".line-price");
let $totalPrice = $(".total-price");
let totalPrice = 0;
$allLinePrice.each(function (){
    totalPrice += Number($(this).text());
})
$totalPrice.text(Number(totalPrice))

for(i=0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function (){
        let productId = this.dataset.product;
        let action = this.dataset.action;

        // update product quantity
        let $quantityVal = $(this).parent().prev();
        let quantityVal = Number($quantityVal.text())
        if (action==='add') quantityVal += 1;
        if (action==='remove') quantityVal -= 1;
        if (quantityVal < 1) quantityVal = 1;
        $quantityVal.text(quantityVal);

        // update product line price
        let $price = $(this).parent().parent().next();
        let $linePrice = $(this).parent().parent().next().next();
        let price = Number($price.text())
        let newLinePrice = price * quantityVal
        $linePrice.text(newLinePrice)
        $linePrice.data({"linePrice": newLinePrice})
        $linePrice.addClass("line-price")

        // update total price
        let $allLinePrice = $(".line-price");
        totalPrice = 0
        $allLinePrice.each(function (){
            totalPrice += Number($(this).text())
        })
        $totalPrice.text(totalPrice)

        // Update cart items form
        let formItemId = $(this).parent().attr("id");
        let $formItemQuantity = $(`form>div>input#id_items-${formItemId}-quantity`);
        let $formItemId = $(`form>div>input#id_items-${formItemId}-id`);
        $formItemQuantity.val(quantityVal);


    })

}
