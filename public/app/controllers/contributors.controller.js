angular
  .module('project-x')
  .controller('contributorsController', contributorsController);

  function contributorsController(){

  	var vm = this;

  	vm.test = "this is the contributors page"
  }