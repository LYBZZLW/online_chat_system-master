/*
* url：请求地址
* rurl：跳转地址
* msg：消息提示
* */

function del(url, rurl, msg) {
    $("#btn-del").click(function () {
        if (window.confirm("确定要注销用户吗？")) {
            $('#del_judge').val('yes')
            var data = $("#form-data").serialize();
            $.ajax({
                url: url,
                data: data,
                dataType: "json",
                type: "POST",
                success: function (res) {
                    if (res.code == 1) {
                        //状态code：1表示成功！
                        alert(msg);
                        location.href = rurl;
                    } else {
                        //不成功
                        alert('发生错误')
                    }
                }
            });
        }
    });
}