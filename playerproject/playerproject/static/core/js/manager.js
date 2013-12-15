
domready(function() {

	var _managerCntrl = window.ManagerCntrl = {
		$selectToolbar: $('#manager-record-controls'),
		$compareButton: $('#manager-compare'),
		selected: [],
	};

	_managerCntrl.$selectToolbar.hide();

	$('.record-checkbox').click(function(e) {
		var control = ManagerCntrl;
		var toolbar = control.$selectToolbar;
		var compare = control.$compareButton;
		var array = control.selected;
		var element = $(this);
		var found = false;
		var id = element.attr('data-record');

		for (var i = array.length - 1; i >= 0; i--) {
			
			if (array[i] == id) {
				array.splice(i, 1);
				element.closest('.list-group-item').removeClass('active');
				element.find('i').addClass('glyphicon-unchecked');
				element.find('i').removeClass('glyphicon-ok');
				found = true;
			}
		};

		if (!found) {
			array.push(id);
			element.closest('.list-group-item').addClass('active');
			element.find('i').addClass('glyphicon-ok');
			element.find('i').removeClass('glyphicon-unchecked');
		}

		toolbar.toggle(array.length > 0);
		compare.attr('href', compare.attr('data-django').replace('abc', array.join('/')));
	});

});