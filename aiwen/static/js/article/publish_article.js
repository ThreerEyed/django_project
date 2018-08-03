
layui.use(['layer', 'form', 'layedit', 'upload', 'jquery'], function () {
        var $ = layui.jquery,
            form = layui.form,
            layedit = layui.layedit;

        layui.cache.page = 'index';
        layui.cache.user = {
            username: '游客',
            uid: 2,
            avatar: '/image/default.png',
            experience: 110,
            sum: 0,
            vip: 0,
            sex: ''
        };
        layui.config({version: Date.parse(new Date())}).extend({'fly': '/static/js/index'}).use('fly');

        //edit:change init
        var bigcat = $("#bigcat").val();
        var subcat = $("#subcat").val();
        if (subcat) {
            $('#parentid').val(bigcat);
            var subcat_html = $('#bigcat_' + bigcat).html();
            $('#catid').html(subcat_html);
            $('#catid').val(subcat);
            form.render('select');
        }


        //change select
        form.on('select(parentid)', function (data) {
            var bigcat = data.value;
            var subcat_html = $('#bigcat_' + bigcat).html();
            $('#catid').html(subcat_html);
            form.render('select');
        });


        // //创建一个编辑器
        // var editIndex = layedit.build('LAY_demo_editor', {
        //     height: 300,
        //
        //     tool: [ 'strong','italic','underline','|','left', 'center', 'right', '|','image'],
        //     uploadImage:{
        //         url: '/ajax/upload_news_thumb' //接口url
        //         ,type: 'post' //默认post
        //     }
        // });

        //自定义验证规则
        form.verify({
            title: function (value) {
                if (value.length < 5) {
                    return '标题不能少于5个字符！';
                }
            }
            , description: function (value) {
                if (value.length < 5) {
                    return '摘要不能少于5个字符！';
                }
            }

            , catid: function (value) {
                if (value == 0) {
                    return '栏目不能为空！';
                }
            }
            , content: function (value) {
                // layedit.sync(editIndex);
                if (value == '') {
                    return '内容不能为空！';
                }
            }
        });


        $(".change_code").click(function () {
            $("#captcha").attr('src', $("#captcha").attr("src") + '&' + Date.parse(new Date()));
        });

        $('#del_thumb').click(function () {
            if (confirm('确定删除封面？')) {
                LAY_demo_upload.src = '/image/default.png';
                $('#thumbid').val(0);
            }
        });

    });