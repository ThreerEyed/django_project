/**
 * 自定义js
 *
 */

//===== 百度统计 =====
// var _hmt = _hmt || [];
// (function() {
//     var hm = document.createElement("script");
//     hm.src = "https://hm.baidu.com/hm.js?bf923227d5ecb0a725bb3ca3dc85e7d8";
//     var s = document.getElementsByTagName("script")[0];
//     s.parentNode.insertBefore(hm, s);
// })();


//=====第三方登录：QQ登录
// var oauth={
//     childWindow:null,
//     url:'https://graph.qq.com/oauth2.0/authorize?client_id=101135247&response_type=code&state=1&scope=get_user_info&redirect_uri=https%3a%2f%2fwww.itgoodboy.com%2fqqlogin',
//     toQzoneLogin:function(){
//         this.childWindow = window.open(this.url,'TencentLogin','width='+(window.screen.availWidth)+',height='+(window.screen.availHeight)+',menubar=0,scrollbars=1,resizable=1,status=1,titlebar=0,toolbar=0,location=1');
//     },
//     toQzoneLogout:function(){
//         this.childWindow.close();
//     }
// };

function heartBeat(ws) {
    if(ws && ws.readyState == 1) {
        ws.send(JSON.stringify({type :'ping'}))
    }
}

layui.use(['jquery','layer','form'], function() {
    var $ = layui.jquery
        ,layer=layui.layer
        ,form = layui.form;

    // //======register=====
    // function isUsername(str){
    //     var reg = /^[a-zA-Z0-9_]+$/;
    //     return reg.test(str);
    // }

    //======  统计在线人数  ======
    // function statisticsUser(userOnline) {
    //     ws = new WebSocket("wss://www.itgoodboy.com:4431");
    //     ws.onopen = function(){
    //         ws.send(JSON.stringify({type: 'statistics',userOnline:userOnline}));
    //     };
    //     ws.onmessage = function(e){
    //         var msg = JSON.parse(e.data);
    //         $('#userTotal').html(msg.userTotal);
    //         $('#pageTotal').html(msg.pageTotal);
    //     };
    //
    //     setInterval('heartBeat(ws)', 20000);
    // }


    // form.verify({
    //     username: function(value){
    //         if(value.length < 6 || value.length >20){
    //             return '账号长度为6~20个字符！';
    //         }
    //
    //         if (!isUsername(value)) {
    //             return '用户名只能是【字母/数字/下划线】组合';
    //         }
    //     },
    //     password: function(value){
    //         if(value.length < 6 || value.length >20){
    //             return '密码长度为6~20个字符！';
    //         }
    //     },
    //     passwordAgain: function(value){
    //         if(value.length < 6 || value.length >20){
    //             return '确认密码有误！';
    //         }
    //     }
    // });


    //=====login-status=====
    $(document).ready(function(){
        $.get('/user/login_status/', function(res){
            if (res.code == 200) {
                var loginStatus = '<li class="layui-nav-item layui-hide-xs">' +
                    '<a class="fly-nav-avatar" href="/user/my/">' +
                    '<img src="/media/'+res.data.avatar+'">' +
                    '<cite class="layui-hide-xs"> '+res.data.nickname+' </cite>' +
                    '</a>' +
                    '</li>' +
                    '<li class="layui-nav-item">' +
                    '<a href="/user/setting/"><i class="iconfont icon-shezhi" style="top: 0; font-size: 21px;"></i> 设置</a>' +
                    '</li>' +
                    '<li class="layui-nav-item">' +
                    '<a href="/user/logout/"><i class="iconfont icon-tuichu" style="top: 0; font-size: 21px;"></i> 退出</a>' +
                    '</li>';


                //admin
                if (res.admin) {
                    var admin_tab = '<li class="layui-hide-xs layui-hide-sm layui-show-md-inline-block"><span class="fly-mid"></span></li>' +
                        '<li class="layui-hide-xs layui-hide-sm layui-show-md-inline-block">' +
                        '<a href="//www.itgoodboy.com/admin/user_list" target="_blank" style="color:orangered;">后台管理</a></li>';
                    $('#nav-search').append(admin_tab);
                }

            } else {
                var loginStatus = '<li class="layui-nav-item"><a class="iconfont icon-touxiang layui-hide-xs" href="/login"></a></li>' +
                    '<li class="layui-nav-item"><a href="/user/login/">登入</a></li>' +
                    '<li class="layui-nav-item"><a href="/user/register">注册</a></li>';
            }

            $('#loginStatus').html(loginStatus);

            //======  统计在线人数 start  ======
            // statisticsUser(res.userOnline);
            //======  统计在线人数 end  ======

        }, 'json');
    });



    // //=====收藏，取消收藏=====
    // $('#collection_up').click(function(){
    //     $.get('/my/collection/up?uuid='+$(this).attr('data'), function(data){
    //
    //         layer.alert(data.msg, {
    //             'icon':data.icon,
    //             'time':1200,
    //             end:data.action ? (function(){
    //                 window.location.href = window.location;
    //             }) : ''
    //         });
    //     });
    // });


    // $('#collection_down').click(function(){
    //     $.get('/my/collection/down?uuid='+$(this).attr('data'), function(data){
    //
    //         layer.alert(data.msg, {
    //             'icon':data.icon,
    //             'time':1200,
    //             end:data.action ? (function(){
    //                 window.location.href = window.location;
    //             }) : ''
    //         });
    //     });
    // });

    //=====验证码=====
    $(".change_captcha").click(function () {
        var v_code_img = $("#captcha").attr("src");
        $("#captcha").attr('src', v_code_img + '&' + Date.parse(new Date()));
    });

    //===== delete article =====

    // $('#article_delete').click(function(){
    //     var uuid = $(this).attr('data');
    //     layer.confirm('确定删除？', {icon: 3, title:'提示'}, function(){
    //         $.get('/admin/delete?uuid='+uuid, function(data){
    //             layer.alert(data.msg, {
    //                 'icon':data.icon,
    //                 'time':1200,
    //                 end:data.action ? (function(){
    //                     window.location.href = window.location;
    //                 }) : ''
    //             });
    //         });
    //     });
    // });

});


// //360自动收录功能
// (function(){
//     var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?d81035cbcce727eff97b602591e082ec":"https://jspassport.ssl.qhimg.com/11.0.1.js?d81035cbcce727eff97b602591e082ec";
//     document.write('<script src="' + src + '" id="sozz"><\/script>');
// })();

