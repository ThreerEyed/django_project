
layui.use(['jquery','layer','form'], function() {
    var $ = layui.jquery
        , layer = layui.layer
        , form = layui.form;


});

layui.use(['upload', 'jquery'], function () {
    var upload = layui.upload,
        $ = layui.jquery
        , layer = layui.layer;

    $(document).ready(function () {
       $.get('/user/login_status/', function (resp) {
           if (resp.code == 200){
               $('#LAY_demo_upload').attr('src', '/media/' + resp.data.avatar)
           }
       })
    });

    var csrf = $('[name=csrfmiddlewaretoken]').val();
    upload.render({
        elem: '.upload-img',
        method: 'POST',
        url: '/user/set_avatar/',
        headers: {'X-CSRFToken': csrf},
        done: function (res) { //上传成功后的回调
            // LAY_demo_upload.src = res.data.src;
            $('#LAY_demo_upload').attr('src', res.src);
            location.href = '/user/set_avatar/'
        }
    });
});