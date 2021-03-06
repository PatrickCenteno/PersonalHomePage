$(document).ready( function(){
	/**
	 * Main site content
	 */

	/**
	 * Right now this is unneccessary
	 */
	// Iterates through each element in the content list class and adds slideLeft to it
	// Purpose being that they dont all slide in at once
	// $(".contentList").each( function(){
	// 	$(this).addClass("slideLeft");
	// 	//window.setTimeout(function(){}, 1000);
	// });


	/**
	 * Admin page content
	 */

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
			if (response === "incorrect password"){
				$("#passwordSubmitAlert").show();
				$("#modalPasswordBox").val("");
			}else{
				// Display contents of the page and hide the modal
				$("#passwordAlertModal").modal("hide");
				window.location = "http://localhost:5000/admin_display";
			}
		});
	});

	/**
	 * Event Handlers for submission buttons
	 **/

	// Color Select 
	$("#changeColorButton").click ( function (){
		$primaryColor = $("#primaryColorSelect option:selected").val();
		$secondaryColor = $("#secondaryColorSelect option:selected").val();

		// Send hex values to server with ajax request
		$.ajax({
			type:'post',
			url:'http://localhost:5000/add_info', // Hardcoded for dev purposes
			data:{table_name:'colors', color_one:$primaryColor, color_two:$secondaryColor}
		}).then(function(response){
			alert("Colors changed");
		})
	});


	// Add course button
	$("#addCourseButton").click( function() {
		$("#courseSubmissionModal").modal("show");
	});

	// course modoal submit button
	$("#courseSubmitButton").click( function (){
		$courseName = $("#modalCourseSubBox").val();

		if ($.trim($courseName) === "")
			return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'courses', course_name:$courseName}
		}).then(function(response){
			$("#modalCourseSubBox").val("");
			$("#courseSubmissionModal").modal("hide");
			// Add list item
		});
	});


	// Add language button
	$("#addLanguageButton").click( function() {
		$("#languageSubmissionModal").modal("show");
	});

	// course modoal submit button
	$("#languageSubmitButton").click( function (){
		$language = $("#modalLanguageSubBox").val();

		if ($.trim($language) === "")
			return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'languages', language:$language}
		}).then(function(response){
			$("#modalLanguageSubBox").val("");
			$("#languageSubmissionModal").modal("hide");
			// Add list item
		});
	});


	// Add project button
	$("#addProjectButton").click( function() {
		$("#projectSubmissionModal").modal("show");
	});

	// course modoal submit button
	$("#projectSubmitButton").click( function (){
		$project = $("#modalProjectSubBox").val();
		$projectLink = $("#modalProjectLinkBox").val();

		if ($.trim($project) === "")
			return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'projects', project_description:$project, link:$projectLink}
		}).then(function(response){
			$("#modalProjectSubBox").val("");
			$("#modalProjectLinkBox").val("");
			$("#ProjectSubmissionModal").modal("hide");
			// Add list item
		});
	});

	// Add Work Experience button
	$("#addWorkButton").click( function() {
		$("#workSubmissionModal").modal("show");
	});

	// course modoal submit button
	$("#workSubmitButton").click( function (){

		$place = $("#modalWorkPlaceBox").val();
		$location = $("#modalWorkLocationBox").val();
		$timePeriod= $("#modalWorkTimePeriodBox").val();
		$role = $("#modalWorkRoleBox").val();
		$description = $("#modalWorkDescriptionBox").val();

		// if ($.trim($project) === "")
		// 	return; // exit event handler

		$.ajax({
			type:'post',
			url:"http://localhost:5000/add_info", // Hardcoded for dev purposes
			data:{table_name:'work_experience', place:$place, location:$location, time_period:$timePeriod,
						role:$role, description:$description}
		}).then(function(response){
			$("#modalWorkPlaceBox").val("");
			$("#modalWorkLocationBox").val("");
			$("#modalWorkTimePeriodBox").val("");
			$("#modalWorkRoleBox").val("");
			$("#modalWorkDescriptionBox").val("");
			$("#workSubmissionModal").modal("hide");
			// Add list item
		});
	});

	/**
	 * Delete Functions
	 */

	// Course
	$(".courses").click( function (){
		$idNum = $(this).children("input").attr("value");
		$tableName = "courses";

		$.ajax({
			type:'post',
			url:"http://localhost:5000/delete_info", //hardcoded for dev purposes
			data:{table_name:$tableName, id_num:$idNum}
		}).then(function(response){
			window.location.href = "http://localhost:5000/admin";
		});
	});

	// Languages
	$(".languages").click( function (){
	 	$idNum = $(this).children("input").attr("value");
		$tableName = "languages";

		$.ajax({
			type:'post',
			url:"http://localhost:5000/delete_info", //hardcoded for dev purposes
			data:{table_name:$tableName, id_num:$idNum}
		}).then(function(response){
			window.location.href = "http://localhost:5000/admin";
		});
	});

	// Work Experience
	$(".work_experience").click( function (){
		$idNum = $(this).children("input").attr("value");
		$tableName = "work_experience";

		$.ajax({
			type:'post',
			url:"http://localhost:5000/delete_info", //hardcoded for dev purposes
			data:{table_name:$tableName, id_num:$idNum}
		}).then(function(response){
			window.location.href = "http://localhost:5000/admin";
		});
	});

	// Projects
	$(".projects").click( function (){
		$idNum = $(this).children("input").attr("value");
		$tableName = "projects";

		$.ajax({
			type:'post',
			url:"http://localhost:5000/delete_info", //hardcoded for dev purposes
			data:{table_name:$tableName, id_num:$idNum}
		}).then(function(response){
			window.location.href = "http://localhost:5000/admin";
		});
	});
});