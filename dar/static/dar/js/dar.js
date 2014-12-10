'use strict';
var app = angular.module('smicApp');

app.directive('showDisciplines', function () {
    return {
        restrict: 'E',
        templateUrl: 'static/dar/partials/discipline-show.html'
    };
});