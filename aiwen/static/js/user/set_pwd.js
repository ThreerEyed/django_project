
layui.use(['jquery', 'layer', 'form'], function () {
    var $ = layui.jquery,
        layer = layui.layer,
        form = layui.form;
    
    $(document).ready(function () {
        $('#set_pwd').submit(function (e) {
            e.preventDefault();
            var csrf = $('[name=csrfmiddlewaretoken]').val();
            var data = $('#set_pwd').serialize();
            $.ajax({
                url: '/user/set_pwd/',
                type: 'POST',
                dataType: 'json',
                data: data,
                // headers: {'X-CSRFToken': csrf},
                success: function (resp) {
                    if (resp.code==200){
                        layer.msg('修改成功', {
                            time: 2000,
                            btn: ['好的']
                        });
                    } else {
                        layer.alert(resp.msg)
                    }
                }
            })
        })
    })
});