angular
  .module('project-x')
  .controller('ProfileController', ProfileController);

function ProfileController ($http, $routeParams) {
  var vm = this;

  vm.city = 'Nashville';

  vm.show = function() {
    vm.city = 'city';
    vm.website = 'website';
    vm.brigadeName = 'brigade-name';

  };
}
