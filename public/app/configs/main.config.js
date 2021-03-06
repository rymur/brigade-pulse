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
    .when('/brigades', {
      templateUrl: './app/views/brigades.html',
      controller: 'brigadesController',
      controllerAs: 'brigades',
      private: false
    })  
    .when('/brigades/projects', {
      templateUrl: './app/views/projects.html',
      controller: 'projectsController',
      controllerAs: 'projects',
      private: false
    }) 
    .when('/projects/:projectId', {
      templateUrl: './app/views/project.html',
      controller: 'projectController',
      controllerAs: 'project',
      private: false
    })
    .when('/brigades/:brigadeName', {
      templateUrl: './app/views/profile.html',
      controller: 'profileController',
      controllerAs: 'brigade',
      private: false
    }) 
    .when('/contributors', {
      templateUrl: './app/views/contributors.html',
      controller: 'contributorsController',
      controllerAs: 'contrib',
      private: false
    })
    .otherwise({
      redirectTo: '/'
    });
}
