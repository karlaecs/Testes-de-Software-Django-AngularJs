'use strict';

var app = angular.module('smicApp', ['ngRoute', 'ngResource']);

app.config(['$routeProvider',
            '$resourceProvider',
            '$interpolateProvider',
            '$httpProvider',
    function ($routeProvider, $resourceProvider, $interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $routeProvider.
        when('/students', {
            templateUrl: 'static/dar/partials/student-list.html',
            controller: 'StudentController'
        }).
        when('/disciplines', {
            templateUrl: 'static/dar/partials/discipline-list.html',
            controller: 'DisciplineController'
        }).
        when('/secretariats', {
            templateUrl: 'static/dar/partials/secretariat-list.html',
            controller: 'SecretariatController'
        }).
        otherwise({
            redirectTo: '/students'
        });
}]);