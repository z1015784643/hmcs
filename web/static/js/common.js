;
var common_ops = {
    init:function(){
        // console.log("sommon.js初始化")
        this.eventBind()
    },
    buildUrl:function(path,params){
        var url = ""+path
        return url
    },
    eventBind:function(){

    }
}

$(document).ready(function(){
    common_ops.init();
})