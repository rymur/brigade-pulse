angular
  .module('project-x')
  .controller('projectsController', projectsController);
  	function projectsController(){
  		var vm = this;

  		vm.test = "this is the projects page"
  	}