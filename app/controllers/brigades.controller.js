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
    vm.search = "";

    getBrigadeData();

    function getBrigadeData(){
      $http.get('https://cfn-brigadepulse.firebaseio.com/brigadeInfo.json')
      .success(function(brigades){
        vm.brigades = brigades;
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
    vm.brigadeProjects;

    getBrigadeData();

    function getBrigadeData(){
      $http.get('http://codeforamerica.org/api/organizations/' + vm.brigadeName)
      .success(function(data){
        vm.brigadeDetails = data;
      })

      $http.get('http://codeforamerica.org/api/organizations/' + vm.brigadeName + '/projects?per_page=100')
      .success(function(data){
        vm.brigadeProjects = data.objects;
        vm.brigadeProjectsTotal = data.total;
      })
    }
  };
