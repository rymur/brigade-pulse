angular
  .module('project-x')
  .controller('brigadesController', brigadesController)
  .controller('profileController', profileController);

  function brigadesController(){
  	var vm = this;
    vm.test = "This is the brigades page"	 
  }
  
  function profileController ($http, $routeParams) {
	var vm = this;

	vm.test = "this is the brigade profile page"
  };

