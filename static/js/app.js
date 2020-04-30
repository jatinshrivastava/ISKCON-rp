$(function () {
    console.log("Hello!");
});
$.ajax({
    url: '',
    type: 'get',
    dataType: 'json',
    success: function (data) {
        var data = jQuery.parseJSON(data);
        $("#get-chapter").click(function (event) {
            $('#shloka_chapter').val(data[0].chapter);
        });

    }
});