$( document ).ready(function() {
	
	console.log("Welcome to Currency_Converter");
	
});

function onconvertbutclick(){
	currency = $('#currency').val();
	amount = $('#amount').val();

	$.ajax({
            url: "/converter/",
            type: "GET",
	    data: {"currency":currency,"amount":amount},
            contentType: 'application/json; charset=utf-8',
            success: function(resultData) {
		content = " Dollar : " +resultData['dollar']+" | Euro : " +resultData['euro']+" | Yen : " +resultData['yen']
		$('#show_convert').text(content);
            },
            error : function(jqXHR, textStatus, errorThrown) {
		console.log(textStatus)
		alert(textStatus);
            },
        });
}