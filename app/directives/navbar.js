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
        var isProject = $location.path().indexOf('projects') !== -1;
        if (isBrigade) {
          $('.nav li').removeClass('active')
          $('.nav li:nth-child(2)').addClass('active')
        } else if (isProject) {
          $('.nav li').removeClass('active')
          $('.nav li:nth-child(2)').addClass('active')
        } else {
          $('.nav li').removeClass('active')
          $('.nav li:nth-child(1)').addClass('active')
        }

      })
    }
  };
});
