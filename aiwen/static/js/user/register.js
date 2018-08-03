
layui.use(['jquery','layer','form'], function() {
    var $ = layui.jquery,
        layer=layui.layer,
        form = layui.form;

        // layer.config({
        //     skin: 'layer.css'
        // });

        //======register=====
        function isUsername(str){
            var reg = /^[a-zA-Z0-9_]+$/;
            return reg.test(str);
        }

        //=====验证码=====
        $(".change_captcha").click(function () {
            var v_code_img = $("#captcha").attr("src");
            $("#captcha").attr('src', v_code_img + '&' + Date.parse(new Date()));
        });

        $('#register_form').submit(function () {
            var data = $('#register_form').serialize();
            $.ajax({
                url: '/user/register/',
                type: 'POST',
                dataType: 'json',
                // headers: {'X-CSRFToken': csrf_token},
                data: data,
                success: function (resp) {
                    if (resp.code == 200){
                        layer.confirm('登录成功',{
                            btn: ['确认']
                        }, function () {
                            location.href = '/user/login/'
                        })
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