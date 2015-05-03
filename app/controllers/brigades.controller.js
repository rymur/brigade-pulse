angular
  .module('project-x')
  .controller('brigadesController', brigadesController)
  .controller('profileController', profileController);

  function brigadesController($http){
  	var vm = this; 
    vm.getBrigadeNameFormat = function(name){
      formattedName = name.replace(/ /g,"-");
      return formattedName;
    }

    vm.brigades;
    vm.brigadesLength;

    getBrigadeData();

    function getBrigadeData(){
      $http.get('http://codeforamerica.org/api/organizations?per_page=1000')
      .success(function(brigades){
        vm.brigades = brigades.objects;
        vm.brigadesLength = brigades.objects.length;
      })
    }

    vm.leadChar = function (city, subString){
      
      return city.toLowerCase().indexOf(subString.toLowerCase()) == 0
    }
  }

  function profileController ($http, $routeParams) {
    var vm = this;
    vm.brigadeName = $routeParams.brigadeName;
    vm.brigadeDetails;
    getBrigadeData();

    function getBrigadeData(){
      $http.get('http://codeforamerica.org/api/organizations/' + vm.brigadeName)
      .success(function(data){
        vm.brigadeDetails = data;
        console.log(data);
      })
    }
  };

