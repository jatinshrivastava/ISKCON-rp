$("#chapter").change(function () {
    var chapter = $(this).val();
    var url = $("#ShlokaForm").attr("data-shlokas-url");
    //console.log(url); // get the url of the `load_cities` view
    // get the selected country ID from the HTML input

    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
            'chapter': chapter // add the country id to the GET parameters
        },
        success: function (data) {
            // `data` is the return of the `load_cities` view function
            $("#shloka_no").html(
                data
            );
            // console.log(
            //  data
            // ); 
        }
    });

});