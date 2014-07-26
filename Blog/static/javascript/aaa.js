
var app=angular.module('blog', ['ngCookies'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

app.directive('topPanel', function(){
	return{
		restrict: 'E',
		templateUrl: '/static/javascript/template/toppanel.html'
	}
});

app.directive('comments', function(){
	return{
		restrict: 'E',
		templateUrl: '/static/javascript/template/comments.html'
	}
});

app.controller('userInfo', ['$scope', '$cookies', function($scope, $cookies){
	$scope.info = function(isLog, isAdmin, nick){
		if(isLog == 'True'){
			$scope.isLog = true;
		}else{
			$scope.isLog = false;}
		if(isAdmin == 'True'){
			$scope.isAdmin = true;
		}else{
			$scope.isAdmin = false;}
		$scope.nick = nick;
		$scope.token = $cookies['csrftoken'];
	};
}]);
	

app.controller('EntriesAll', ['$scope', '$http', function($scope, $http){
	$scope.page = 1;
	$scope.getEntries = function(){
		$scope.entries=[];
		$http({method: 'GET', url: '/api-root/entries/?page='+$scope.page+'&format=json'}).success(function(data, status, headers, config){
			$scope.entries = data.results;
			if(data.previous == null){$scope.prev=false;}else{$scope.prev=true;};
			if(data.next == null){$scope.next=false;}else{$scope.next=true;};
			if(data.count == 0){$scope.no_entries=true;}else{$scope.no_entries=false;};
		});
	};
}]);

app.controller('delComment', ['$scope', '$http', function($scope, $http){
	this.delete_comment = function(id){
		$http({method: 'DELETE', url: '/api-root/commentsedit/'+id+'/', headers:{'X-CSRFToken':$scope.token}})
			.success(function(data, status, headers, config){
		})
			.error(function(data, status, headers, config){
				alert(status);
		});
	};
}]);

app.controller('editComment', ['$scope', '$http', function($scope, $http){
	this.edit_comment = function(comm){
		$http({method: 'PUT', url: '/api-root/commentsedit/'+comm.id+'/', data: comm, headers:{'X-CSRFToken':$scope.token}})
			.success(function(data, status, headers, config){
		})
			.error(function(data, status, headers, config){
				alert(status);
		});
	};
}]);

app.controller('hideEditCtrl', function(){
	this.ctrl = false;
	this.ctrl2 = false;
});
//sending comments
app.controller('sendCtrl', ['$scope', '$http', function($scope, $http){
	$scope.send = function(opin, comm, id){
		opin.entry = id;
		opin.nick = $scope.nick;
		$http({method: 'POST', url: '/api-root/comments/', data: opin, headers:{'X-CSRFToken':$scope.token}})
			.success(function(data, status, headers, config){
				//$scope.getEntries(); //uncoment for autorefresh after adding comment
				opin.add_date = 'Now';
				comm.push(opin);
				$scope.opinion = {};
			})
			.error(function(data, status, headers, config){alert(status);});
	};
}]);

app.controller('userCheck', ['$http', function($http){
	var t = this;
	t.userlist = [];
	$http({method: 'GET', url: '/api-root/user/?format=json'}).success(function(data, status, headers, config){
			t.userlist = data;
		});
	t.nick = '';
	t.reg = '';
	this.check = function(){
		t.reg = 'mySuccess';
		for(var i in t.userlist){
			if(t.userlist[i].username == t.nick){t.reg='myError';};
		if(!t.nick)t.reg='myError';
		};
	};
}]);



	
