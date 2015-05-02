angular
  .module('project-x')
  .controller('MainController', MainController);

function MainController ($http, $routeParams) {
  var vm = this;

  vm.initialize = function() {
    var locations = [];
    var heatmapData = [];
    var map, heatmap;
    var mapOptions = {
      center: { lat: 41.850033, lng: -87.6500523},
      zoom: 5
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);

     $http.get('http://codeforamerica.org/api/organizations.geojson').
        success(function(data) {
          $.each(data.features,function(index, value){locations.push(value.geometry.coordinates)})
          $.each(locations, function(index, value){
            heatmapData.push(new google.maps.LatLng(value[1], value[0]))
          })

        var heatmapGradient = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]

    heatmap = new google.maps.visualization.HeatmapLayer({
      data: heatmapData,
      gradient: heatmapGradient,
      radius: 10
    });

    heatmap.setMap(map);
  });
 }

}




