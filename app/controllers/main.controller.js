angular
  .module('project-x')
  .controller('MainController', MainController);

function MainController($http, $routeParams) {
  var vm = this;

  vm.initialize = function() {
      var locations = [];
      var heatmapData = [];
      vm.brigades = [];
      var map, heatmap;
      var mapOptions = {
        center: {
          lat: 42.879094,
          lng: -97.381205
        },
        zoom: 4,
        styles: [{
          "stylers": [{
            "visibility": "on"
          }, {
            "saturation": -100
          }, {
            "gamma": 0.54
          }]
        }, {
          "featureType": "road",
          "elementType": "labels.icon",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "water",
          "stylers": [{
            "color": "#4d4946"
          }]
        }, {
          "featureType": "poi",
          "elementType": "labels.icon",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "poi",
          "elementType": "labels.text",
          "stylers": [{
            "visibility": "simplified"
          }]
        }, {
          "featureType": "road",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#ffffff"
          }]
        }, {
          "featureType": "road.local",
          "elementType": "labels.text",
          "stylers": [{
            "visibility": "simplified"
          }]
        }, {
          "featureType": "water",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#ffffff"
          }]
        }, {
          "featureType": "transit.line",
          "elementType": "geometry",
          "stylers": [{
            "gamma": 0.48
          }]
        }, {
          "featureType": "transit.station",
          "elementType": "labels.icon",
          "stylers": [{
            "visibility": "off"
          }]
        }, {
          "featureType": "road",
          "elementType": "geometry.stroke",
          "stylers": [{
            "gamma": 7.18
          }]
        }]
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

      $http.get('http://codeforamerica.org/api/organizations.geojson').
      success(function(data) {
        $.each(data.features, function(index, value) {
          heatmapData.push({
            location: new google.maps.LatLng(value.geometry.coordinates[1], value.geometry.coordinates[0])
          });
          vm.brigades.push(value.properties.name);
        });

        var heatmapGradient = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(255, 0, 91, 1)',
          'rgba(255, 0, 63, 1)',
          'rgba(255, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
<<<<<<< HEAD
        ]

    heatmap = new google.maps.visualization.HeatmapLayer({
      data: heatmapData,
      gradient: heatmapGradient,
      radius: 20
    });

    heatmap.setMap(map);
  });
 }
}



=======
        ];
        
          heatmap = new google.maps.visualization.HeatmapLayer({
            data: heatmapData,
            gradient: heatmapGradient,
            radius: 10
          });
>>>>>>> 01b54bf2276269d6ce21d9335ac2276511dad668

          heatmap.setMap(map);
        });
      };
      }
