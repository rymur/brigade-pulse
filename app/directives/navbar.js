angular
  .module('project-x.directives.navbar', [])
  .directive('navbar', function() {
    'use strict';
    return {
      restrict: 'E',
      scope: {
        data: '='
      },
      templateUrl: 'app/templates/navbar.html',
      controller: function($scope, $rootScope, $location) {
	$rootScope.$on('$locationChangeSuccess', function(){
		var isBrigade = $location.path().indexOf('brigades') !== -1;
		$('.nav li').removeClass('active')
		var active = isBrigade ? 2 : 1;		
		$('.nav li:nth-child('+ active + ')').addClass('active')
	})
      }
    };
  });
