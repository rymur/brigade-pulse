angular
  .module('project-x')
  .config(ProjectXConfig);

function ProjectXConfig($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: './app/views/home.html',
    controller: 'MainController',
    controllerAs: 'main'
  });
}
