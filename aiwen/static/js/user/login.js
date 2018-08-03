
layui.use(['jquery','layer','form'], function() {
    var $ = layui.jquery
        , layer = layui.layer
        , form = layui.form;

    $('#login_form').submit(function () {
            var data = $('#login_form').serialize();
            $.ajax({
                url: '/user/login/',
                type: 'POST',
                dataType: 'json',
                // headers: {'X-CSRFToken': csrf_token},
                data: data,
                success: function (resp) {
                    if (resp.code == 200){
                        if('login'.indexOf(resp.url)){
                            location.href = '/article/index/'
                        }else{
                            location.href = resp.url
                        }
                    } else {
                        layer.alert(resp.msg)
                    }
                },
                error: function (resp) {

                }
            });
            return false
        });

});




