angular.module('project-x')
.filter('eventDate', function(){
    'use strict'

    return function(input){
        //var dateArray = input.split(" ");
        //console.log(dateArray);
        //return dateArray[0];
        var monthArray = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        var date = new Date(input);
        return date.getDay() + ' ' + monthArray[date.getMonth() -1] + ' ' + date.getFullYear()
    }
})