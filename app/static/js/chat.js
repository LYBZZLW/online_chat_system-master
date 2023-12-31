$(document).ready(function () {
    //1.定义长连接
    var conn = null;
    //2.获取频道名称
    $.ajax({
        url: "/channel/",
        type: "GET",
        async: false,
        success: function (res) {
            var channel_data = res.data;
            for (k in channel_data) {
                var html = "";
                html += "<option value=\"" + channel_data[k][0] + "\" style=\"color: black;\">" + channel_data[k][1] + "</option>"
                $("#selectChannel").append(html)
            }
        }
    });
    //3.获取昵称，头像，频道号
    var name = $("#input_name").val();
    var face = $("#input_face").val();
    var channel = $("#selectChannel option:selected").val();


    // 追加聊天消息框
    function append_msg(name, data) {
        if (data.channel == channel) {
            var html = "";
            if (data.code == 2) {
                if (name == data.name) {
                    //代表我自己
                    html += "<div class=\"row\">";
                    html += "<div class=\"col-md-3\"></div>";
                    html += "<div class=\"col-md-9\">";
                    html += "<div class=\"media\">";
                    html += "<div class=\"media-body\">";
                    html += "<h6 class=\"user-nickname text-right\">" + data.name + "[" + data.dt + "]</h6>";
                    html += "<div class=\"alert alert-success\" role=\"alert\">";
                    html += data.content;
                    html += "</div>";
                    html += "</div>";
                    html += "<img class=\"ml-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                    html += "</div></div></div>";
                } else {
                    html += "<div class=\"row\">";
                    html += "<div class=\"col-md-9\">";
                    html += "<div class=\"media\">";
                    html += "<img class=\"mr-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                    html += "<div class=\"media-body\">";
                    html += "<h6 class=\"user-nickname\">" + data.name + "[" + data.dt + "]</h6>";
                    html += "<div class=\"alert alert-info\" role=\"alert\">";
                    html += data.content;
                    html += "</div>";
                    html += "</div>";
                    html += "</div></div>";
                    html += "<div class=\"col-md-3\"></div>";
                    html += "</div>";
                }
            } else if (data.code == 1) {
                html += "<p class='text-center text-success'>欢迎" + data.name + "进入聊天室！<img src='/static/images/rorse.gif'><img src='/static/images/rorse.gif'><img src='/static/images/rorse.gif'></p>"
            }
            $("#chat-list").append(html);
            SyntaxHighlighter.highlight();
            $("#chat-list").scrollTop($("#chat-list").scrollTop() + 9999999);
        }
    }

    // 初始加载信息
    function load_msg() {
        $("#chat-list").empty()
        $.ajax({
            url: "/msg/",
            type: "POST",
            dataType: "json",
            success: function (res) {
                var msg_data = res.data;
                for (var k in msg_data) {
                    append_msg(name, msg_data[k]);
                }
                var enter_data = {
                    code: 1,
                    name: name,
                    face: face,
                    channel: channel
                };
                conn.send(JSON.stringify(enter_data));
            }
        });
    }

    // 更新UI函数
    function update_ui(event) {
        var data = event.data;
        data = JSON.parse(data);
        append_msg(name, data);
    }

    //4.定义连接
    function connect() {
        //之前连接没有断开先将其断开
        disconnect();
        var transports = [
            "websocket", "xhr-streaming",
            "iframe-eventsoure", "iframe-htmlfile",
            "xhr-polling", "iframe-xhr-polling",
            "jsonp-polling"
        ];
        conn = new SockJS("http://" + window.location.host + "/chatroom", transports);
        //客户端发起连接
        conn.onopen = function () {
            load_msg()
        };
        //双向通信
        conn.onmessage = function (event) {
            update_ui(event);
        };
        //关闭连接
        conn.onclose = function () {
            conn = null;
        }
    }

    //5.断开连接
    function disconnect() {
        if (conn != null) {
            conn.close();
            conn = null;
        }
    }

    // 执行连接
    if (conn == null) {
        connect();
    } else {
        disconnect();
    }

    // 获取表单数据
    function getFormData() {
        var arr = $("#form-data").serializeArray();
        var obj = {};
        $.map(arr, function (n, i) {
            obj[n['name']] = n['value'];
        });
        return obj
    }

    // 发送信息
    $("#send_msg").click(function () {
        var msg_data = getFormData();
        if (msg_data.content) {
            msg_data.code = 2;
            msg_data.channel = channel;
            console.log(msg_data)
            ue.setContent('');
            conn.send(JSON.stringify(msg_data));
        } else {
            alert("发送消息不能为空！");
        }
    });

    // 切换频道时重新加载信息
    $('#selectChannel').on('change', function () {
        channel = $("#selectChannel option:selected").val();
        load_msg();
    })
});