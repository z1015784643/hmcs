;
var user_login_ops={
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $('.login_wrap .do-login').click(function(){
            var login_name = $('.login_wrap input[name=login_name]').val()
            var login_pwd = $('.login_wrap input[name=login_pwd]').val()
            console.log(login_name)
            console.log(login_pwd)
            if(login_name == undefined ||login_name.length<1){
                alert('请输入正确的名字')
                return
            }
            if(login_pwd == undefined ||login_pwd.length<1){
                alert('请输入正确的密码')
                return
            }

            $.ajax({
                url:common_ops.buildUrl('/user/login'),
                type:'POST',
                data:{'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(resp){
                    alert(resp.msg)
                }
            })

        })
    }
}

$(document).ready(function(){
    user_login_ops.init();

})