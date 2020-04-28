;
$(function () {
    function Ajax(id,acts){
        $.ajax({
            url:common_ops.buildUrl("/account/removeOrRecover"),
            type:'POST',
            data:{'id':id,'acts':acts},
            dataType:'json',
            success:function (resp) {
                alert(resp.msg);
                window.location.reload()
            }
        })
    }
    $('.wrap_search .search').click(function () {
        $('.wrap_search').submit()
    });
    $('.remove').click(function () {
        id = $(this).attr("data");
        Ajax(id,'remove')
    });
    $('.recover').click(function () {
        id = $(this).attr("data");
        Ajax(id,'recover')
    });
})