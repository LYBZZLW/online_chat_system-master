/*
* k：名称，face
* w：宽度，200
* h：高度，200
* url：上传地址
* */

function upload(k, w, h, url) {
    $("#upload_" + k).click(function () {
        var img = $("#file_" + k)[0].files[0];
        if (img) {
            var formData = new FormData();
            formData.append("img", img);
            $.ajax({
                url: url,
                type: "POST",
                dataType: "json",
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
                success: function (res) {
                    if (res.code == 1) {
                        var image = res.image;
                        var content = "<img src='/static/uploads/" + image + "' style='width: 200px;200px;'>";
                        $("#image_" + k).empty();
                        $("#image_" + k).append(content);
                        $("#input_" + k).attr("value", image);
                    }
                }
            });
        }
    });

}