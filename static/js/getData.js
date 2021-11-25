$(document).ready(() => {
    const token = sessionStorage.getItem("token") || ``;
    const title_update = $("#title-update");

    const url = `http://localhost:8000/api/v1/event/`;

    // click delete
    $('.click_delete').click((e) => {
        if (!confirm("You sure to delete this item?")) {
            return;
        }
        const id = $(e.target).attr("event-id")
        // handle submit
        handleDelete(id, token);
    });

    // click update
    $(".click_detail").click((e) => {
        const id = $(e.target).attr("event-id");
        // get item
        getItem(id, token);
    })

    // form update
    $("#form-update").submit(function (e) {
        e.preventDefault();

        var form = $(this);
        var id = $('input[name=id]').val();

        handleUpdate(form, id, token);
    });

    // function
    const getItem = (id, token) => {

         var request = $.ajax({
            url: `${url}${id}/`,
            method: "GET",
            headers: {'Authorization': `token ${token}`}
        });

        request.done(function (msg) {
            $('input[name=title]').val(msg['title']);
            $('input[name=body]').val(msg['body']);
            $('input[name=id]').val(msg['id']);
            $('input[name=client_id]').val(msg['client_id']);
            $('input[name=type]').val(msg['type']);
            title_update.text(`Update Event ${id}`);

            $('#staticBackdrop').modal('show');
        });

        request.fail(function (jqXHR) {
            console.log(jqXHR);
        });
    }

    const handleUpdate = (form, id, token) => {
        var request = $.ajax({
            url: `${url}${id}/`,
            method: "PUT",
            headers: {'Authorization': `token ${token}`},
            dataType: 'json',
            data: form.serialize()
        });

        request.done(function (msg) {
            location.reload();
        });

        request.fail(function (jqXHR) {
            console.log(jqXHR.responseJSON);
        });
    };

    const handleDelete = (id, token) => {
        var request = $.ajax({
            url: `${url}${id}/`,
            method: "DELETE",
            headers: {'Authorization': `token ${token}`}
        });

        request.done(function (msg) {
            console.log(msg);
            location.reload();
        });

        request.fail(function (jqXHR, textStatus) {
            console.log(jqXHR);
            console.log(textStatus);
        });
    }
})

