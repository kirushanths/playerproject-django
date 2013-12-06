
ngapp.directive('uiFocus', ['$parse', function($parse) {
	return function(scope, element, attr) {
		var fn = $parse(attr['uiFocus']);
		element.bind('focus', function(event) {
			scope.$apply(function() {
				fn(scope, {$event:event});
			});
		});
	}
}]);

ngapp.directive('uiBlur', ['$parse', function($parse) {
	return function(scope, element, attr) {
		var fn = $parse(attr['uiBlur']);
		element.bind('blur', function(event) {
			scope.$apply(function() {
				fn(scope, {$event:event});
			});
		});
	}
}]);