$(document).ready(() => {
    const nav = $(".navbar-nav");
    nav.attr("display", "none");

    var token = getParameter("token");
    if (token != null) {
        sessionStorage.setItem("token", token);
        nav.attr("display", "flex");
    }


    var div_error = $('#error-text');
    div_error.css("display", 'none');

    function getParameter(parameterName) {
        var result = null,
            tmp = [];
        location.search
            .substr(1)
            .split("&")
            .forEach(function (item) {
                tmp = item.split("=");
                if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
            });
        if (result === "") return null
        return result;
    }

    /*
        const form = $("#form-login");

        form.submit((e) => {
            // e.preventDefault();
            var login_url = `http://localhost:8000/check/`;
            login(login_url, form);
        });

            const login = (url, form) => {
                var request = $.ajax({
                    url: url,
                    method: "POST",
                    dataType: 'json',
                    data: form.serialize()
                });
                request.done(function (msg) {
                    console.log(msg)
                });

                request.fail(function (jqXHR, statusMess) {
                    console.log(statusMess)
                    div_error.text(jqXHR.responseJSON);
                    div_error.css("display", 'block');
                });
            }

            const handleSubmit = (form) => {
                const base_url = `http://localhost:8000`;

                var request = $.ajax({
                    url: `${base_url}/user/api/token/`,
                    method: "POST",
                    dataType: 'json',
                    data: form.serialize()
                });

                request.done(function (msg) {
                    try {
                        localStorage.setItem("token", msg['access']);
                        console.log('save token success!!!')
                    } catch (error) {
                        console.log(error.message)
                        return;
                    }
                    var login_url = `${base_url}/`

                    login(login_url, form);
                });

                request.fail(function (jqXHR) {
                    div_error.text(jqXHR.responseJSON.detail);
                    div_error.css("display", 'block');
                });
            }
             * */
})
