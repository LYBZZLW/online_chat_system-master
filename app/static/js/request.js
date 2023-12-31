/*
* url：请求地址
* rurl：跳转地址
* fields：验证字段
* msg：消息提示
* */
function request(url, rurl, fields, msg) {
    $("#btn-sub").click(function () {
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
                    //不成功，验证字段
                    for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error_" + fields[k]).empty();
                        } else {
                            $("#error_" + fields[k]).empty();
                            $("#error_" + fields[k]).append(
                                res[fields[k]]
                            );
                        }
                    }
                }
            }
        });
    });
}