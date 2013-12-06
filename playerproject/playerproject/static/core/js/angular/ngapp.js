// var app = angular.module('myApp', ['myApp.filters', 'myApp.directives']);
var ngapp = angular.module('ngapp', []);

ngapp.directive('tooltip', function () {
    return {
        restrict:'A',
        link: function(scope, element, attrs)
        {
   //      	$(element)
   //              .attr('title',scope.$eval(attrs.tooltip))
   //              .tooltip({placement: "right"});

   //          var elem = $(element),
			// 	corners = ['left center', 'right center'],
			// 	flipIt = elem.parents('span.right').length > 0;

   //      	.qtip({
			// 	overwrite: false,
			// 	content: error,
			// 	position: {
			// 		my: corners[ flipIt ? 0 : 1 ],
			// 		at: corners[ flipIt ? 1 : 0 ],
			// 		viewport: $(window)
			// 	},
			// 	show: {
			// 		event: false,
			// 		ready: true
			// 	},
			// 	hide: false,
			// 	style: {
			// 		classes: 'qtip-red' // Make it red... the classic error colour!
			// 	}
			// })
			// // If we have a tooltip on this element already, just update its content
			// .qtip('option', 'content.text', error);


   //          $(element)
   //              .attr('title',scope.$eval(attrs.tooltip))
   //              .tooltip({placement: "right"});
        }
    }
})