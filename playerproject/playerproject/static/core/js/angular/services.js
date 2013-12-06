// ngapp.factory('socket', function ($rootScope) {
//     var socket = io.connect(':100', {secure: true});
    
//     socket.socket.on('error', function (reason){
//         console.error('Unable to connect CM: ', reason);
//     });

//     return {
//         on: function (eventName, callback) {
//             socket.on(eventName, function () {  
//                 var args = arguments;
//                 $rootScope.$apply(function () {
//                     callback.apply(socket, args);
//                 });
//             });
//         },
//         emit: function (eventName, data, callback) {
//             socket.emit(eventName, data, function () {
//                 var args = arguments;
//                 $rootScope.$apply(function () {
//                     if (callback) {
//                         callback.apply(socket, args);
//                     }
//                 });
//             })
//         }
//     };
// });

ngapp.factory('utils', function() {
    return {
        timestamp : function() { 
            return Math.round(new Date().getTime() / 1000); 
        },
        isNumber : function(n) {
            return !isNaN(parseFloat(n)) && isFinite(n);
        }
    };
});

ngapp.factory('model', function() {
    return {

    };
});

ngapp.service('nav', function() {
    var navbar = {
        inboxCount: 0
    };
    
    return {
        getInboxCount: function() {
            return navbar.inboxCount;
        },
        setInboxCount: function(value) {
            navbar.inboxCount = value;
        }
    }
});