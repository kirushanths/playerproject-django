function get_random_color() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random() * 15)];
    }
    return color;
}

//Function to create a legend
function legend(parent, data) {
    parent.className = 'legend';
    var datas = data.hasOwnProperty('datasets') ? data.datasets : data;

    datas.forEach(function(d) {
        var title = document.createElement('span');
        title.className = 'title';
        title.style.borderColor = d.hasOwnProperty('fillColor') ? d.fillColor : d.color;
        title.style.borderStyle = 'solid';
        parent.appendChild(title);
        var text = document.createTextNode(d.title);
        title.appendChild(text);
    });

}
Array.prototype.remove = function(set){return this.filter(
    function(e,i,a){return set.indexOf(e)<0}
)};

domready(function() {
	var active_players = [];
	$('.player-active').each(function(index, value){
		active_players.push($(this).attr('data-record'));
	});

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
				active_players.push(id);
				element.find('i').addClass('glyphicon-unchecked').css('color','lightgreen');
				element.find('i').removeClass('glyphicon-ok');
				found = true;
			}
		};

		if (!found) {
			array.push(id);
			element.find('i').addClass('glyphicon-remove').css('color','red');
			element.find('i').removeClass('glyphicon-unchecked');
		}

		toolbar.toggle(array.length > 0);
		active_players = active_players.remove(array);
		$('select[name="add-players"]').toggle(array.length == 0);

		if(active_players.length > 0){
		compare.attr('href', compare.attr('data-django').replace('abc', active_players.join('/')));
		} else{
		compare.attr('href', '/dashboard/manager/');
		}
	});

	$('select[name="add-players"]').change(function() {
		var control = ManagerCntrl;
		var compare = control.$compareButton;
		var selectedVal = $(this).val();
		active_players.push(selectedVal);
		var url =  compare.attr('data-django').replace('abc', active_players.join('/'))
		location.href = url;
	});

});