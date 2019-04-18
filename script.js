// add event listener when the document is done loaded
$(document).ready(function() {
	// listen to button click
	$('.submit-button').click(sendMessageRequest)
	// listen to textbox enter
	$('.textbox').keydown(function(e) {
		if (e.keyCode == 13) sendMessageRequest()
	})
})

function sendMessageRequest() {
	// add self message to the chat list
	var message = 
		'<div id="chattext">\
            You : ' + $(".textbox").val() + '\
        </div>'
    $('.content-body').append(message)

    // send message to another php to be processed
    $.ajax({
    	url: 'doProcess.php',
    	type: "GET",
    	data: {
    		message: $('.textbox').val()
    	},
    	success: function(result) {
    		// append doProcess' response to chat list
    		var message =
	    		'<div id="chattext">\
		            Xyli : ' + result + '\
		        </div>'
			$('.content-body').append(message)
    	}
    })

    // clear sent message just for cleanliness
    $('.textbox').val("")
}