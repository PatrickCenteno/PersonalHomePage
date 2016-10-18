$(document).ready( function(){
	// Add Admin page listeners here
	// Display passowrd modal on page load
	$("#passwordAlertModal").modal("show");

	// Event handler for password modal on admin page
	// Ajax call to check password
	$("#passwordSubmitButton").click( function() {
		// TODO: input validation
		$passwordInput = $.trim($("#modalPasswordBox").val());

		$.ajax({
			type:'post',
			url:"http://localhost:5000/check_password", // Hardcoded for dev purposes
			data:{password:$passwordInput}
		}).then(function(response) {
			if (response === "password correct"){
				$("#passwordAlertModal").modal("hide");
			}else{
				$("#passwordSubmitAlert").show();
				$("#modalPasswordBox").val("");
			}

		});
	});

});