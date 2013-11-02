Dropzone.autoDiscover = false;

$(function() {
  	// Now that the DOM is fully loaded, create the dropzone, and setup the 
  	// event listeners

  	var dazzle_dropzone = new Dropzone("#dazzle-dropzone", {
  		autoProcessQueue: false,
  		previewsContainer: ".dropzone-previews",
  		paramName: "dzfile",
  		uploadMultiple: true,
  		maxFilesize: 2, // MB
  		addRemoveLinks: true,
  		acceptedFiles: "image/*, text/html, text/css, .html, .css"
  	});

  	dazzle_dropzone.on("addedfile", function(file) {
    	/* Maybe display some more file information on your page */
    	console.log('ADDED');
	});

});
