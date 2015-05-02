angular
  .module('project-x')
  .config(ProjectXConfig);

function ProjectXConfig($routeProvider) {
  'use strict';
  $routeProvider
    .when('/', {
      templateUrl: './app/views/home.html',
      controller: 'MainController',
      controllerAs: 'main',
      private: false
    })
    .when('/brigades/:brigadeId', {
      templateUrl: './app/views/profile.html',
      controller: 'ProfileController',
      controllerAs: 'profile',
      private: false
    })
    .otherwise({
      redirectTo: '/'
    });
}
