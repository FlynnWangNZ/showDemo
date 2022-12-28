$("table").on("click", ".insertRow", function (event) {
    event.preventDefault();

    var newRow = $("<tr>");
    var cols = "";

    // Table columns
    cols += '<td></td>';
    cols += '<td></td>';
    cols += '<td><label class="form-control">SVN version</label></td>';
    cols += '<td><input type="button" class="btn btn-success getVersion" value="GetVersion"></td>';
    cols += '<td><button class="btn btn-danger rounded-0" id ="deleteRow"><i class="fa fa-trash"></i></button</td>';
    cols += '<td><a class="btn btn-primary rounded-0 insertRow"><i class="fa fa-plus"></i></a></td>';

    // Insert the columns inside a row
    newRow.append(cols);
    // Insert the row inside a table
    // $("table").append(newRow);
    $("table > tbody > tr").eq($(this).parent().parent().index()).after(newRow);

    $(this).parent().parent().find("select").clone().appendTo($(this).parent().parent().next().find('td')[1]);

});

// Remove row when delete btn is clicked
$("table").on("click", "#deleteRow", function (event) {
    $(this).closest("tr").remove();

});

// Get SVN version from server
$("table").on("click", ".getVersion", function (event) {
    const component_index = $(this).parent().parent().find("select option:selected").val();
    const $button = $(this);
    $.ajax({
        url: "", data: {'component_index': component_index}, type: "PUT", dataType: "json", success: function (data) {
            $button.parent().parent().find("label").html(data.msg);
        }, error: function (data) {
            console.error(data);
        }
    })
});
