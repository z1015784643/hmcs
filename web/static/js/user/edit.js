;
var user_edit_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        // 获取保存的按钮
        $('.user_edit_wrap .save').click(function(){
            var btn_target = $(this)
                if (btn_target.hasClass("disabled")){
                    alert('正在处理，稍后再试')
                    return;
                }
            
            var nickname_value = $('.user_edit_wrap input[name=nickname]').val();
            var email_value = $('.user_edit_wrap input[name=email]').val()
            console.log(nickname_value)
            console.log(email_value)
            if ( !nickname_value || nickname_value.length < 1){
                alert('请输入正确的姓名')
                return false
            }
            if ( !email_value || email_value.length < 1 ){
                alert('请输入正确的邮箱号')
                return false
            }

            $.ajax({
                url:common_ops.buildUrl('/user/edit'),
                type:'POST',
                data:{'nickname':nickname_value,'email':email_value},
                dataType:'json',
                success:function(resp){
                    btn_target.removeClass('disabled')
                    console.log(resp)
                    console.log(resp.code)
                    btn_target.removeClass('disabled')
                },
                // error:function (resp) {
                //     console.log(error)
                // }
            })
        })
    }
}
$(document).ready(function(){
    user_edit_ops.init()
})