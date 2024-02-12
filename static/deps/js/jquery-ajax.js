$(document).ready(function () {
    var successMessage = $("#jq-notification");

    function showSuccessMessage(message) {
        successMessage.html(message);
        successMessage.fadeIn(400);
        setTimeout(function () {
            successMessage.fadeOut(400);
        }, 3000);
    }

    function updateCartUI(data, change) {
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        cartCount += change;
        goodsInCartCount.text(cartCount);

        var cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(data.cart_items_html);
    }

    $(document).on("click", ".add-to-cart, .remove-from-cart", function (e) {
        e.preventDefault();

        var url = $(this).attr("href");
        var data = {
            product_id: $(this).data("product-id"),
            cart_id: $(this).data("cart-id"),
            csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
        };

        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: function (data) {
                showSuccessMessage(data.message);
                updateCartUI(data, (data.quantity_deleted || 1) * (url.includes("add") ? 1 : -1));
            },
            error: function () {
                console.log("Error processing the cart action.");
            },
        });
    });

    $(document).on("click", ".decrement, .increment", function () {
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());
        var newValue = $(this).hasClass('increment') ? currentValue + 1 : currentValue - 1;

        if (newValue >= 1) {
            $input.val(newValue);
            var cartID = $(this).data("cart-id");
            var url = $(this).data("cart-change-url");
            updateCart(cartID, newValue, url);
        }
    });

    function updateCart(cartID, quantity, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                showSuccessMessage(data.message);
                updateCartUI(data, 0);
            },
            error: function () {
                console.log("Error updating cart.");
            },
        });
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

    document.getElementById('id_phone_number').addEventListener('input', function (e) {
        var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
        e.target.value = !x[2] ? x[1] : `(${x[1]}) ${x[2]}-${x[3] || ''}`;
    });

    $('#create_order_form').on('submit', function (event) {
        var phoneNumber = $('#id_phone_number').val();
        var regex = /^\(\d{3}\) \d{3}-\d{4}$/;

        if (!regex.test(phoneNumber)) {
            $('#phone_number_error').show();
            event.preventDefault();
        } else {
            $('#phone_number_error').hide();
            $('#id_phone_number').val(phoneNumber.replace(/[()\-\s]/g, ''));
        }
    });
});
