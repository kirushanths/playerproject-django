String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g, '');};
String.prototype.ltrim=function(){return this.replace(/^\s+/,'');};
String.prototype.rtrim=function(){return this.replace(/\s+$/,'');};
String.prototype.fulltrim=function(){return this.replace(/(?:(?:^|\n)\s+|\s+(?:$|\n))/g,'').replace(/\s+/g,' ');};

$.fn.findAndSelf = function(selector) {
    return this.find(selector).add(this.filter(selector));
  };

$.fn.duplicate = function(count, cloneEvents) {
       var tmp = [];
       for ( var i = 0; i < count; i++ ) {
               $.merge( tmp, this.clone( cloneEvents ).get() );
       }
       return this.pushStack( tmp );
};

$.fn.draggableXY = function(options) { 
  var defaultOptions = { 
    distance: 5, 
    dynamic: false 
  }; 
  options = $.extend(defaultOptions, options); 

  this.draggable({ 
    distance: options.distance, 
    start: function (event, ui) { 
      ui.helper.data('draggableXY.originalPosition', ui.position || {top: 0, left: 0}); 
      ui.helper.data('draggableXY.newDrag', true); 
    }, 
    drag: function (event, ui) { 
      var originalPosition = ui.helper.data('draggableXY.originalPosition'); 
      var deltaX = Math.abs(originalPosition.left - ui.position.left); 
      var deltaY = Math.abs(originalPosition.top - ui.position.top); 

      var newDrag = options.dynamic || ui.helper.data('draggableXY.newDrag'); 
      ui.helper.data('draggableXY.newDrag', false); 

      var xMax = newDrag ? Math.max(deltaX, deltaY) === deltaX : ui.helper.data('draggableXY.xMax'); 
      ui.helper.data('draggableXY.xMax', xMax); 

      var newPosition = ui.position; 
      if(xMax) { 
        newPosition.top = originalPosition.top; 
      } 
      if(!xMax){ 
        newPosition.left = originalPosition.left; 
      } 

      return newPosition; 
    } 
  }); 
};

 

window.dazzlejQuery = jQuery.noConflict();
window.dazzlejQuery(function(){ 
 
	setupDefaults();
	dzEngine.runEngine();
});

function setupDefaults()
{  
	var dz$ = window.dazzlejQuery;
	dz$.noty.defaults = {
	  layout: 'top',
	  theme: 'defaultTheme',
	  type: 'alert',
	  text: '',
	  dismissQueue: true, // If you want to use queue feature set this true
	  template: '<div class="noty_message"><span class="noty_text"></span><div class="noty_close"></div></div>',
	  animation: {
	    open: {height: 'toggle'},
	    close: {height: 'toggle'},
	    easing: 'swing',
	    speed: 500 // opening & closing animation speed
	  },
	  timeout: 5000, // delay for closing event. Set false for sticky notifications
	  force: false, // adds notification to the beginning of queue when set to true
	  modal: false,
	  closeWith: ['click'], // ['click', 'button', 'hover']
	  callback: {
	    onShow: function() {},
	    afterShow: function() {},
	    onClose: function() {},
	    afterClose: function() {}
	  },
	  buttons: false // an array of buttons
	};
}

var dzEngine = (function(){

	var dz$ = window.dazzlejQuery;
	var websiteUrl = 'http://10.30.0.2' + window.location.pathname;
	var updateUrl = "http://10.30.0.2/update" + window.location.pathname;
	var notyQueue = {};
	var imageToolbar;
	var linkToolbar;
	var copyToobar;
	var removeToolbar;
	var copyRemoveTarget;
	var nextId = 10000; //temporary


	function setNextId()
	{	
		var maxId = 0;
		dz$('[dzid]').each(function(index)
		{
			try
			{
				var ident = parseInt(this.getAttribute('dzid')); 
				if (ident && ident > maxId)
				{
					maxId = ident;
				}
			}
			catch(err)
			{
			}
		});  
		nextId = maxId+1;
	}

	/**
	 *	IMAGE FUNCTIONS
	 */
	function runImageEngine() 
	{ 
		var toolbar = createImageToolbar(); 
		toolbar.hide();

		var tags = document.getElementsByTagName('*');
	    var element;

		for (var i = 0, len = tags.length; i < len; i++) 
		{
		    element = tags[i];
		    if (element.nodeName == "BODY")	continue;
		   
		    var imageUrl = getImageFromElement(element);

		    if (imageUrl == null) continue;

		    element.className = ".dz-image";

		    addImageToolbar(element, imageUrl, toolbar);
		}
	}

	function createImageToolbar()
	{  
		var toolbar = dz$("<div id='dz-imageToolbar'> \
						  		<div class='dz-title'>Modify Image</div> \
						   		<div class='dz-preview'></div> \
						   		<div class='dz-text'>Click or drag file here </div> \
						   </div>");
		toolbar.appendTo('body');

		toolbar.hide();
		var dropzone = new Dropzone(toolbar.get(0), 
		{  
			parallelUploads: 5,
			clickable: true,
			maxFilesize: 5 ,
			url: updateUrl,
			previewsContainer: ".dz-preview",
			accept: function(file, done) {  
				done();
			}
		});

		toolbar.dropzone = dropzone; 

		addImageHandlers(dropzone);

		return toolbar;
	} 

	function addImageHandlers(dropzone)
	{
		dropzone.on("addedfile", function(file)
		{   
			if (notyQueue[file]) notyQueue[file].close();
			var notyid = noty({text: 'Uploading file...', timeout:false});
			notyQueue[file] = notyid;
		});


		dropzone.on("error", function(file, message) { 
			if (notyQueue[file])
			{
				notyQueue[file].close(); 
				notyQueue[file] = null;
			}

			noty({text: 'An error occurred during upload.', type:'error'});

		}); 

		dropzone.on("success", function(file, response) { 
			if (notyQueue[file])
			{
				notyQueue[file].close(); 
				notyQueue[file] = null;
			}

			noty({text: 'Upload successful', type:'success'});

			if (response)
			{
				updateElementImage(file.targetElement, response);
			} 
		});
	}

	function addImageToolbar(element)
	{    

		var toolbar = imageToolbar; 
		  
		if (element.nodeName == "BODY")	return;
		   
		var imageUrl = getImageFromElement(element);
 
		if (imageUrl == null) return;
  
		if (!element.getAttribute('dzid')) return;

		element.className = ".dz-image";
 
	    dz$(element).hover(
			function(){     
				toolbar.show();
				toolbar.position({
					my: "center",
    				at: "right top+10",
    				of: this,
    				collision: "fit"
				}); 
				var previewFile = { name: "previewFile", size: 0 };
				toolbar.dropzone.options.addedfile.call(toolbar.dropzone, previewFile);
				toolbar.dropzone.options.thumbnail.call(toolbar.dropzone, previewFile, getImageFromElement(this));
				toolbar.dropzone.options.targetElement = this;
				toolbar.dropzone.options.targetElementId = this.getAttribute('dzid'); 
			},
			function(){
			}
		); 
	}

	function updateElementImage(element, imageUrl)
	{ 
		if (!element || !imageUrl) return;
	 
		if (element.nodeName == "IMG")
		{  
			$(element).attr("src", imageUrl);
		}
		else
		{  
			$(element).css("background-image", 'url("' + imageUrl + '")'); 
	    }
	}

	function getImageFromElement(element)
	{
		if (element.nodeName == "IMG")
		{
			var image = element.src;
			if (image)
			{
				return image;
			}
		}
		if (element.currentStyle)
	    {
	    	var image = element.currentStyle['backgroundImage'];
	        if( image !== 'none' && image.match(/\.(jpg|jpeg|png|gif)/))
	        { 
	            return image.replace('url(','').replace(')','');
	        }
	    }
	    else if (window.getComputedStyle)
	    {
	    	var image = document.defaultView.getComputedStyle(element, null).getPropertyValue('background-image');
	        if( image !== 'none' && image.match(/\.(jpg|jpeg|png|gif)/))
	        {  
	            return image.replace('url(','').replace(')','');
	        }
	    }
	    return null;
	}	

	/**
	 *	TEXT FUNCTIONS
	 */
	function runTextEngine()
	{   
		dz$('[dzid]').each(function(index)
		{
			if (!dz$(this).text().fulltrim().length) 
				return;

			var text = dz$(this).clone().find('[dzid]').remove().end().text();
			text = text.replace(/^\s+|\s+$/g,''); 

			if (!text.length) return;
 		
 			if (!dz$(this).parents(".dz-editor").length)
			{ 
				dz$(this).addClass("dz-editor");
				addHalloEditor(this);
				addHalloHandlers(this);
			} 
		}); 
	}

	function addHalloEditor(element)
	{
		if (element.tagName == 'DIV' || element.tagName == 'SECTION')
		{
			dz$(element).hallo({
		        plugins: {
			      'halloformat': {}, 
			      'halloblock':{},
			      'hallojustify': {},
			      'hallolists': {},
			      'halloreundo': {},
			      'halloheadings': {},
			      'hallolink': {}
		        }
		    });
		}
		else
		{
			dz$(element).hallo({
				plugins:{
					'halloformat': {}, 
					'halloreundo': {},
					'hallolink': {}
				}
			});
		}
	}

	function addHalloHandlers(element)
	{
		dz$(element).bind('hallodeactivated', function(event){ 
				var el = dz$(event.target);

				if (!el.hasClass('dzmodified')) return;

				var ident = el.attr("dzid");
				var newValue = el.html();

				saveData({'requestType':'updateText', 'id': ident,'value':newValue });

				el.removeClass('dzmodified');
			}
		);

		dz$(element).bind('hallomodified', function(event){
				var el = dz$(event.target);
				if (!el.hasClass('dzmodified'))
				{
					el.addClass('dzmodified')
				}
			}
		);
	}

	/**
	 *	MOVEMENT FUNCTIONS
	 */
	function runSortEngine(elements)
	{
		//dz$( "img" ).draggableXY();
		var handler = function(index)
		{  

		}
		
		var selector = 'div [dzid]'; //TEMPORARY

	 	if (elements)
	 	{
	 		dz$(elements).findAndSelf(selector).each(handler);
	 	}
	 	else
	 	{
	 		dz$(selector).each(handler);
	 	}
	}

	/**
	 *	COPY REMOVE FUNCTIONS
	 */

	function runCopyRemoveEngine(elements)
	{ 
		var handler = function(index)
	 	{
	 		addCopyRemoveToolbars(this, copyToolbar, removeToolbar);
	 	};

	 	// ADD SUPPORT FOR <li> elements
	 	var selector = 'div [dzid]'; //TEMPORARY

	 	if (elements)
	 	{
	 		dz$(elements).findAndSelf(selector).each(handler);
	 	}
	 	else
	 	{
	 		dz$(selector).each(handler);
	 	}
	}

	function addCopyRemoveToolbars(element, copy_toolbar, remove_toolbar)
	{ 
		dz$(element).hover(
			function(){   
				copy_toolbar.show();
				remove_toolbar.show();
				copy_toolbar.position({
					my: "center-45 center",
    				at: "center bottom+5",
    				of: this, 
    				collision: "fit"
				});   
				remove_toolbar.position({
					my: "center+45 center",
    				at: "center bottom+5",
    				of: this, 
    				collision: "fit"
				});

				$(this).data('bgcolor', $(this).css('outline'));
		        $(this).css('outline','1px solid rgba(255,0,0,.5)');

				checkToolbarOverlap();	
				copyRemoveTarget = element;
			},
			function()
			{
				$(this).css('outline', $(this).data('bgcolor'));
			}
		);
	}


	function addChildrenIds(elem) {
    	$(elem).find("[dzid]").each(function() {
    		nextId++;
    		$(this).attr('dzid', nextId);    	
    	})
	}

	function createCopyToolbar()
	{
		var toolbar = dz$("<div id='dz-copyToolbar'> \
						  		<div class='dz-title'>Copy</div> \
						   </div>");
		toolbar.appendTo('body'); 
		toolbar.hide();

		dz$(toolbar).click(function()
		{ 
			var result = dz$(copyRemoveTarget).clone().insertAfter(copyRemoveTarget); 
			var ident = dz$(copyRemoveTarget).attr('dzid'); 
 
			result.attr('dzid', nextId); 
			saveData({'requestType':'copyElement', 'id': ident, 'nextId':nextId });

			addChildrenIds(result);
				
			runCopyRemoveEngine(result);
			runImageEngine(result); 	
			runLinkEngine(result);
			setNextId();
		});

		return toolbar;
	}

	function createRemoveToolbar()
	{
		var toolbar = dz$("<div id='dz-removeToolbar'> \
						  		<div class='dz-title'>Remove</div> \
						   </div>");
		toolbar.appendTo('body'); 
		toolbar.hide();

		dz$(toolbar).click(function()
		{
			dz$(copyRemoveTarget).remove();
			var ident = dz$(copyRemoveTarget).attr('dzid'); 
			console.log(ident);
			saveData({'requestType':'removeElement', 'id': ident });
		});

		return toolbar;
	}

	/**
	 * LINK FUNCTIONS
	 */ 
	 function runLinkEngine(elements)
	 {
	 	var handler = function(index)
	 	{
	 		addLinkToolbar(this);
	 	};

	 	var selector = 'img:not([href]), [href]:not([rel]), [href][rel="external"]';

	 	if (elements)
	 	{
	 		dz$(elements).findAndSelf(selector).each(handler);
	 	}
	 	else
	 	{
	 		dz$(selector).each(handler);
	 	}
	 }

	function addLinkToolbar(element)
	{   
		var toolbar = linkToolbar;

		var linkUrl = element.getAttribute('href');

		if (this.tagName ==  "IMG" && dz$(this).parent().attr("href"))
		{
			return;
		}
		else if (linkUrl && (!linkUrl.indexOf(websiteUrl) && linkUrl.length > websiteUrl.length + 1))
		{
			return;
		}   

	    dz$(element).hover(
			function(){     
				var linkUrl = this.getAttribute('href');
				if (!linkUrl)
				{
					toolbar.children(".dz-title").text("Insert Link");
				}
				else
				{
					toolbar.children(".dz-title").text("Modify Link"); 
				} 

				toolbar.show();
				toolbar.position({
					my: "center",
    				at: "right top+50",
    				of: this, 
    				collision: "fit"
				});   

				dz$("#dz-link-text").val(linkUrl);
				dz$("#dz-link-text").data("target",element);
				dz$("#dz-link-text").data("linkUrl",linkUrl); 

				checkToolbarOverlap();
			},
			function(){
			}
		); 
	}

	function createLinkToolbar()
	{  
		var toolbar = dz$("<div id='dz-linkToolbar'> \
						  		<div class='dz-title'>Modify Link</div> \
						  		<div class='dz-input'><input type='text' id='dz-link-text'></input></div> \
						   </div>");
		toolbar.appendTo('body');
		toolbar.hide();

		var delay;
		dz$("#dz-link-text").keyup(function() { 
			var el = dz$(this);  
			var url =  el.data("linkUrl");
			if (!url || el.attr('href') != url)
			{ 
				el.data("target").setAttribute('href', el.val()); 

				var target = dz$(el.data("target"));
				var ident = target.attr("dzid");
				var newValue = el.val();
				clearTimeout(delay);
       			delay = setTimeout(function(){saveData({'requestType':'updateLink', 'id': ident,'value':newValue })}, 3000); 
				
			} 
		});

		return toolbar;
	}

	/**
	 * HELPERS
	 */

	function checkToolbarOverlap()
	{  
		var hit = dz$(linkToolbar).collision(imageToolbar); 
 		var lastToolbar;

		if (hit.length)
		{ 
			if (linkToolbar.position().left == imageToolbar.position().left || 
				linkToolbar.position().top == imageToolbar.position().top)
			{ 
				linkToolbar.position({
					my: "center",
					at: "center bottom+30",
					of: imageToolbar,
					collision:"fit"
				}); 
				lastToolbar = linkToolbar;
			}
		}

		hit = dz$(imageToolbar).collision(removeToolbar);
		var next_hit = dz$(linkToolbar).collision(removeToolbar);

		if (hit.length || next_hit.length)
		{
			if (next_hit.length && !lastToolbar) lastToolbar = linkToolbar;
			if (hit.length && !lastToolbar) lastToolbar = imageToolbar;
			copyToolbar.position({ 
				my: "center-45 center",
				at: "center bottom+15",
				of: lastToolbar,
				collision:"fit"
			});
			removeToolbar.position({ 
				my: "center+45 center",
				at: "center bottom+15",
				of: lastToolbar,
				collision:"fit"
			});
		} 



	}

	var saveData = function(data)
	{  
		console.log(data);    
		dz$.post(updateUrl, data, function(response)
		{
			console.log(response); 
		});
	}

	/**
	 * PUBLIC!
	 */
	return {
		runEngine: function()
		{	
			imageToolbar = createImageToolbar();  
			linkToolbar = createLinkToolbar();  
			copyToolbar = createCopyToolbar();
			removeToolbar = createRemoveToolbar();

			runCopyRemoveEngine();
			runImageEngine();
			runLinkEngine();
			runTextEngine();
			runSortEngine();
			setNextId();
		}
	};

})();
