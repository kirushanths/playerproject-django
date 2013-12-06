
ngapp.config(function($routeProvider){

	$routeProvider
		.when("/compose", { action: "compose" })
		.when("/compose/:userid", { action: "compose" })
        .otherwise({ redirectTo: "/list" });

});

ngapp.controller('InboxController', function($scope, $http, $route, $routeParams, nav, utils) {

	//TODO: make app wide constants
	// $scope.CMType = {
	// 	message: "inbox:message",
	// 	compose: "inbox:compose",
	// 	notification: "app:notification"
	// };
	$scope.MSG_STATUS = {
		UNREAD: "0",
		READ: "1",
		ARCHIVED: "2"
	};

	$scope.selected = false;
	$scope.loaded = false;
	$scope.compose = false;
	$scope.threads = false;
	$scope.target_user_id = false;

	$scope.$on("$routeChangeSuccess", function( $currentRoute, $previousRoute ){
        var renderAction = $route.current.action;

        var userid = ($routeParams.userid || "");
        if (!utils.isNumber(userid)) {
        	userid = false;
        }

        var isCompose = (renderAction== "compose");

        $scope.target_user_id = userid;
        $scope.compose = isCompose
	});

	$scope.$watch('selected', function(value, oldValue) { 
		if (value.messages) {

			var msgs = [];
			_.each(value.messages, function(msg) {
				if (msg.status == $scope.MSG_STATUS.UNREAD) {
					msgs.push(msg);
				}
			});

			$scope.ajaxMessageRead(msgs);
		}
	});

	//initial load
	$scope.refresh = function() {
		$http({
			method: 'POST',
			url: '/api/v1/inbox/messages/' + timestamp(),
			data: $.param(tpp_csrf_token),
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).
		success(function(data, status, headers, config) {
			console.log(data);
			$scope.loaded = true;
			
			if (data.success) {
				var thread_array = [];
				var latest, latestIndex, index = 0;
				var checkForDate = !!$scope.selected;

				//create new array by index, not associated array by thread_id
				_.each(data.threads, function(thr){
					thr.last = _.last(thr.messages);

					if (!checkForDate) {
						var jsdate = moment(thr.last.cdate);
						if (index == 0) {
							latest = jsdate;
							latestIndex = index;
						} else if (latest.diff(jsdate) < 0) {
							latest = jsdate;
							latestIndex = index;
						}
						index++;
					}

					thread_array.push(thr);
				});

				console.log (thread_array);

				$scope.threads = thread_array;

				//if its a refresh, need to update selected reference
				if (checkForDate) {
					var sel_index = threadIndex($scope.selected.thread_id);
					if (sel_index > -1) {
						$scope.selected = $scope.threads[sel_index];
					}
				}
				else if (thread_array.length > 0) {
					$scope.selected = thread_array[latestIndex];
				}
			}
		}).
		error(function(data, status, headers, config) {
			console.error (data);
		});
	};

	var timestamp = function() { return Math.round(new Date().getTime() / 1000); };

	var threadIndex = function (threadid) {
		var foundIndex = -1;
		_.some($scope.threads, function(thread, index) {
			if (thread.thread_id === threadid) {
				foundIndex = index;
				return true;
			}
		});
		return foundIndex;
	};

	$scope.ajaxReply = function(reply_body) {
		var thread = $scope.selected;
		var participants_display = thread.participants_display;
		var target_msg_id = _.first(thread.messages).id;
		var post_data = $.extend ({
			reply_submit: true,
			reply_msg_id: target_msg_id,
			reply_body: reply_body,
		}, tpp_csrf_token);

		$http({
			method: 'POST',
			url: '/api/v1/inbox/reply/' + timestamp(),
			data: $.param(post_data),
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).
		success(function(data, status, headers, config) {
			console.log (data);
			if (data.success) {
				thread.messages.push(data.message);
			}
		}).
		error(function(data, status, headers, config) {
			console.error (data);
		});
	};

	$scope.ajaxMessageRead= function(msgs) {

		var mids = _.pluck(msgs, 'id').join(',');

		var post_data = $.extend ({
			message_read: true,
			msg_ids: mids,
		}, tpp_csrf_token);

		$http({
			method: 'POST',
			url: '/api/v1/inbox/message_read/' + timestamp(),
			data: $.param(post_data),
			headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).
		success(function(data, status, headers, config) {
			console.log (data);
			if (data.success) {
				_.each (msgs, function(msg) {
					msg.status = $scope.MSG_STATUS.READ;
				});
			}
		}).
		error(function(data, status, headers, config) {
			console.error (data);
		});
	};

	$scope.formatTime = function (UTCtimestamp) {
		var now = moment();
		var msg = moment(UTCtimestamp + '+00:00');

		if (now.diff(msg, 'days') < 1) 
			return msg.format('LT');
		else 
			return msg.format('L');
	}

	$scope.threadParticipants = function () {
		var thr = $scope.selected;
		if (thr && thr.participants) {
			$scope.threadScrollDown();
			return thr.participants.display_name;
		} else {
			return "Not Available";
		}
	}

	$scope.threadListClass = function (thr, $first) {
		var ret = $first ? 'first' : '';

		if (!$scope.compose && 
			$scope.selected === thr) {
			ret += ' selected'; 
		}

		if (thr.last.status == $scope.MSG_STATUS.UNREAD) {
			ret += ' unread';
		}

		return ret;
	};

	$scope.threadListClick = function(thr, $event) { 
		$scope.compose = false;
		$scope.selected = thr;
		if (thr.last.status == $scope.MSG_STATUS.UNREAD) {
			$scope.ajaxMessageRead(thr.last.id);
		}
	};

	$scope.inboxReplyKeyPress = function(body, $event) {
		$event.preventDefault();
		$scope.threadViewReplyClick(body);
		$event.target.value = "";
	};

	$scope.threadViewReplyClick = function(body, $event) {
		if (body && body.length > 0) {
			$scope.ajaxReply (body);
		}
		if ($event) {
			$($event.target).prev().val('');
		}
	};

	$scope.threadMessageListClass = function (thread, user, $index, $first) {
		var ret = "";
		if ($first)
			ret = "first";
		else if ($index > 0) {
			var prev = thread.messages[$index - 1]
			if (user == prev.uacc_username)
				ret = "inbox_message_item_same";
		}

		return ret;
	};

	$scope.threadScrollDown = function () {
		var scroll = $("#inbox_message_scroll");
		scroll.scrollTop (scroll[0].scrollHeight);
	};

	$scope.isInboxEmpty = function() {
		return $scope.loaded && (!$scope.threads || $scope.threads.length == 0);
	};

	$scope.refresh();

});
