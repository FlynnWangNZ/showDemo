(() => {
    setEmailTitleSendTo();
})();


$("table").on("click", ".insertRow", function (event) {
    event.preventDefault();

    var newRow = $("<tr>");
    var cols = "";

    // Table columns
    cols += '<td></td>';
    cols += '<td></td>';
    cols += '<td><input class="form-control version" placeholder="SVN version" required><div class="invalid-feedback">No version number</div></td>';
    cols += '<td><input type="button" class="btn btn-success getVersion" value="GetVersion"></td>';
    cols += '<td><button class="btn btn-danger rounded-0" id ="deleteRow"><i class="fa fa-trash"></i></button</td>';
    cols += '<td><a class="btn btn-primary rounded-0 insertRow"><i class="fa fa-plus"></i></a></td>';

    // Insert the columns inside a row
    newRow.append(cols);
    // Insert the row inside a table
    // $("table").append(newRow);
    $("table > tbody > tr").eq($(this).parent().parent().index()).after(newRow);

    $(this).parent().parent().find("select").clone().appendTo($(this).parent().parent().next().find('td')[1]);

    setEmailTitleSendTo();
});

// Remove row when delete btn is clicked
$("table").on("click", "#deleteRow", function (event) {
    $(this).closest("tr").remove();

    setEmailTitleSendTo();
});

// Get SVN version from server
$("table").on("click", ".getVersion", function (event) {
    const componentIndex = $(this).parent().parent().find("select option:selected").val();
    $(this).parent().parent().find(".version").val(getVersion(componentIndex).msg);
});

// Define async ajax function to get SVN version number
function getVersion(componentIndex) {
    var ret = "";
    $.ajax({
        url: "",
        data: {'component_index': componentIndex},
        type: "PUT",
        dataType: "json",
        async: false,
        success: function (data) {
            ret = data
        },
        error: function (data) {
            console.error(data);
        }
    })
    return ret;
}

// When select changes
$("table").on("change", "#component", function (event) {
    setEmailTitleSendTo();
});

// Auto change email title
function setEmailTitleSendTo() {
    var emailTitle = "Version Release ";
    var sendTo = "DevOpsTeam QATeam SETeam "
    var component2EmailTeam = {
        "1": "FrontTeam",
        "2": "AndroidTeam",
        "3": "iOSTeam",
        "4": "GateWayTeam",
        "5": "MicroServiceTeam",
        "6": "AdminSiteTeam",
        "7": "CRMTeam"
    }
    $(".component").each(function (index) {
        emailTitle += $("option:selected", this).text() + ' ';
        sendTo += component2EmailTeam[$("option:selected", this).val()] + ' ';
    })
    $("#emailTitle").text(emailTitle);
    $("#sendTo").text(sendTo);
}

// Get database file SVN version
$("#dbFile").on("click", function () {
    var labelValue = "None";
    const $sendTo = $("#sendTo");
    var sendTo = $sendTo.text();
    if ($(this).is(":checked")) {
        labelValue = getVersion("0").msg;
        sendTo += "DBA";
    }else {
        sendTo = sendTo.replaceAll("DBA", "");
    }
    $("#dbFileVersion").val(labelValue);
    // append dba to sendTo
    $sendTo.text(sendTo);
});

// Set attention with isUrgent
$("#isUrgent").on("click", function(){
    var $attention = "<div>SQL files should be executed first!</div>";
    if($(this).is(":checked")){
        $attention += "<div>URGENT! Please upgrade to this version ASAP</div>";
    }
    $("#attention").html($attention);
});
