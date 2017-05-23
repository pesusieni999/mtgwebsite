// Collect currently configured options and send them to the server.
function saveOptions() {
    console.log("Testing save button.");
    var options = [];
    $("#options-table > tbody > tr").each(function () {
        var optionText = "";
        var optionId = -1;
        options.push({
            option_text: optionText,
            option_id: optionId
        });
    });

    var tokenId = $("[name='csrfmiddlewaretoken']").val();
    var postUrl = $("#save-url").attr("href");
    var postData = {
        options: options
    };

    $.ajax({
        url: postUrl,
        type: 'POST',
        data: postData,
        beforeSend: function (xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", tokenId);
            }
        }
    })
    .done(function() {
        location.reload();
    })
    .fail(function () {
        alert("Failed to save options. Please refresh page and try again.");
    })
}

function createOption() {
    console.log("Testing create option button.");
    //$("#options-table-body > tbody:last-child").append('<tr><td><input class="form-group option-text-input" type="text" name="option-text" value=""><br/><input class="option-id-input" type="hidden" name="option-id" value="-1"></td><td><button class="remove-option-btn btn btn-default"><span class="glyphicon glyphicon-remove"></span></button></td></tr>');
    $("#options-table").find("tbody").append($("<tr>").html('<td><input class="form-group option-text-input" type="text" name="option-text" value=""><br/><input class="option-id-input" type="hidden" name="option-id" value="-1"></td><td><button class="remove-option-btn btn btn-default"><span class="glyphicon glyphicon-remove"></span></button></td>'))
}

function removeOption(e) {
    $(e.target).parent().parent().parent().remove();
}

$(".remove-option-btn").click(function (e) {
    removeOption(e);
})

$(document).ready(function () {
    // Listener for save button clicks.
    $("#save-options-btn").click(function () {
        saveOptions();
    });

    // Listener for create option button clicks.
    $("#create-option-btn").click(function () {
        createOption();
    });

    /*
    $(".remove-option-btn").click(function (e) {
        removeOption(e);
    })*/
});