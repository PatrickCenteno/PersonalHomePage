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

	/**
	 * Event Handlers for submission buttons
	 **/

	// Add course button
	$("#addCourseButton").click( function() {
		$("#courseSubmissionModal").modal("show");
	});

	// course modoal submit button
	$("#courseSubmitButton").click( function (){
		$courseName = $("modalCourseSubBox").val();

		if ($.trim($courseName) === "")
			return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'courses', course_name:$courseName}
		}).then(function(response){
			console.log(response);
			// Add list item
		});
	});


	// Add language button
	$("#addLanguageButton").click( function() {
		$("#languageSubmissionModal").modal("show")
	});

	// course modoal submit button
	$("#courseSubmitButton").click( function (){
		$language = $("modalLanguageSubBox").val();

		if ($.trim($language) === "")
			return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'languages', language:$language}
		}).then(function(response){
			console.log(response);
			// Add list item
		});
	});
});