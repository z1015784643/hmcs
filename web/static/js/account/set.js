;
console.log('进入添加用户页面')
var account_set_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $('.wrap_account_set .save').click(function(){
            console.log('开始添加用户')
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                return;
            }
            var nickname = $('.wrap_account_set input[name=nickname]').val();
            console.log(nickname)
            var mobile = $('.wrap_account_set input[name=mobile]').val();
            var email = $('.wrap_account_set input[name=email]').val();
            var login_name = $('.wrap_account_set input[name=login_name]').val();
            var login_pwd = $('.wrap_account_set input[name=login_pwd]').val();
            console.log(nickname)
            $.ajax({
                url:common_ops.buildUrl('/account/set'),
                type:'POST',
                data:{ 'nickname':nickname,'mobile':mobile,'email':email,'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(resp){
                    btn_target.removeClass('disabled')
                    alert(resp.msg)
                    console.log(resp.msg)
                    console.log(resp.code)
                },
                error:function (resp) {
                    console.log(error)
                }
            })

        })
    }
}


$(document).ready(function(){
    account_set_ops.init();
})