angular
  .module('project-x')
  .controller('projectsController', projectsController)
  .controller('projectController', projectController)
  	
  function projectsController(){
  	var vm = this;

  	vm.test = "this is the projects page"
  }

  function projectController($http, $routeParams){
  	var vm = this;
  	vm.test = "THIS WORKS"
  	vm.projectDetails;

  	getBrigadeData();

  	function getBrigadeData(){
      $http.get('http://codeforamerica.org/api/projects/' + $routeParams.projectId)
      .success(function(project){
        vm.projectDetails = project;
        console.log(vm.projectDetails)
      })
    }

  }