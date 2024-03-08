$(document).ready(function () {
    var successMessage = $("#jq-notification");

    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var productId = $(this).data("product-id");
        var addToCartUrl = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: addToCartUrl,
            data: {
                product_id: productId,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                displayNotification(data.message);
                goodsInCartCount.text(++cartCount);
                $("#cart-items-container").html(data.cart_items_html);
            },
            error: function () {
                console.log("Error adding product to cart");
            },
        });
    });

    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var cartId = $(this).data("cart-id");
        var removeFromCartUrl = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: removeFromCartUrl,
            data: {
                cart_id: cartId,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                displayNotification(data.message);
                goodsInCartCount.text(cartCount -= data.quantity_deleted);
                $("#cart-items-container").html(data.cart_items_html);
            },
            error: function () {
                console.log("Error removing product from cart");
            },
        });
    });

    $(document).on("click", ".decrement, .increment", function () {
        var url = $(this).data("cart-change-url");
        var cartId = $(this).data("cart-id");
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());
        var change = $(this).hasClass("increment") ? 1 : -1;

        if (change === -1 && currentValue <= 1) return;
        $input.val(currentValue + change);
        updateCart(cartId, currentValue + change, change, url);
    });

    function updateCart(cartId, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartId,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                displayNotification(data.message);
                var goodsInCartCount = $("#goods-in-cart-count");
                goodsInCartCount.text(parseInt(goodsInCartCount.text() || 0) + change);
                $("#cart-items-container").html(data.cart_items_html);
            },
            error: function () {
                console.log("Error updating cart");
            },
        });
    }

    function displayNotification(message) {
        successMessage.html(message).fadeIn(400);
        setTimeout(() => successMessage.fadeOut(400), 7000);
    }

    var notification = $('#notification');
    if (notification.length) {
        setTimeout(() => notification.alert('close'), 7000);
    }

    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body').modal('show');
    });

    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    $("input[name='requires_delivery']").change(function () {
        $("#deliveryAddressField").toggle($(this).val() === "1");
    });

    $('#id_phone_number').on('input', function (e) {
        var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
        e.target.value = !x[2] ? x[1] : `(${x[1]}) ${x[2]}${x[3] ? '-' + x[3] : ''}`;
    });

    $('#create_order_form').on('submit', function (e) {
        var phoneNumber = $('#id_phone_number').val();
        var regex = /^\(\d{3}\) \d{3}-\d{4}$/;

        if (!regex.test(phoneNumber)) {
            $('#phone_number_error').show();
            e.preventDefault();
        } else {
            $('#phone_number_error').hide();
            $('#id_phone_number').val(phoneNumber.replace(/[()\-\s]/g, ''));
        }
    });
});
