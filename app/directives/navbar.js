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
      controller: function($scope) {


      }
    };
  });
