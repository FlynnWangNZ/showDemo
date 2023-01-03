$("#submit").on("click", function (event) {
    if (formValidation()) {
        const hexCode = $("#hexCode").val();
        const project = $("#project").val();
        $.ajax({
            url: "",
            data: {"project": project, "hexCode": hexCode},
            type: "POST",
            dataType: "json",
            success: function (data) {
                $("#readable").jsonViewer(data, {collapsed: false, withQuotes: true})
            },
            error: function (data) {
                console.error(data);
            }
        })
    }
    // prevent default submit form
    return false;
})
