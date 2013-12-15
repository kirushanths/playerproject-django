
domready(function() {

	var _managerCntrl = window.ManagerCntrl = {
		$selectToolbar: $('#manager-record-controls'),
		selected: [],
	};

	_managerCntrl.$selectToolbar.hide();

	$('.record-checkbox').click(function(e) {
		var control = ManagerCntrl;
		var toolbar = control.$selectToolbar;
		var array = control.selected;
		var element = $(this);
		var found = false;

		for (var i = array.length - 1; i >= 0; i--) {
			if (array[i][0] == this) {
				array.splice(i, 1);
				element.closest('.list-group-item').removeClass('active');
				element.find('i').addClass('glyphicon-unchecked');
				element.find('i').removeClass('glyphicon-ok');
				found = true;
			}
		};

		if (!found) {
			array.push(element);
			element.closest('.list-group-item').addClass('active');
			element.find('i').addClass('glyphicon-ok');
			element.find('i').removeClass('glyphicon-unchecked');
		}

		toolbar.toggle(array.length > 0);
	});

});