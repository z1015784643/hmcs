;
var user_login_ops={
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $('.login_wrap .do-login').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                alert('请求正在处理，请稍后再试')
                return;
            }
            var login_name = $('.login_wrap input[name=login_name]').val()
            var login_pwd = $('.login_wrap input[name=login_pwd]').val()
            // console.log(login_name)
            // console.log(login_pwd)
            var log_name = /^[a-zA-Z0-9_-]{4,16}$/;
            if(login_name == undefined || log_name.test(login_name) == false){
                alert('请输入正确的名字')
                return
            }
            var log_pwd = /^[\w_-]{6,10}$/;
            if(login_pwd == undefined || log_pwd.test(login_pwd) == false){
                alert('请输入正确的密码')
                return
            }
            btn_target.addClass('disabled')

            $.ajax({
                url:common_ops.buildUrl('/user/login'),
                type:'POST',
                data:{'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(resp){
                    btn_target.removeClass('disabled')
                    alert(resp.msg)
                    console.log(resp.msg)
                    console.log(resp.code)
                    if (resp.code === 200 ){
                        console.log('刷新页面')
                        window.location.reload()
                        
                    }
                },
                error:function (resp) {
                    console.log(error)
                }
            })
            // console.log('刷新')
            // window.location.reload()

        })
    }
}

$(document).ready(function(){
    user_login_ops.init();

})