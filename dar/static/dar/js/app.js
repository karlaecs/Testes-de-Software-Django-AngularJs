angular.module('smicApp', [
  'ui.router',
  'ngResource',
  'smicApp.services',
  'smicApp.controllers'
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing
    $urlRouterProvider.otherwise('/');
    $stateProvider
      .state('students', {
        url: '/',
        templateUrl: 'static/dar/partials/student-list.html',
        controller: 'StudentController'
      })
      .state('departaments', {
        url: '/',
        templateUrl: 'static/dar/partials/departament-list.html',
        controller: 'DepartamentController'
      })
      .state('secretariats', {
        url: '/',
        templateUrl: 'static/dar/partials/secretariat-list.html',
        controller: 'SecretariatController'
      })
      .state('courses', {
        url: '/',
        templateUrl: 'static/dar/partials/course-list.html',
        controller: 'CourseController'
      })
      .state('disciplines', {
        url: '/',
        templateUrl: 'static/dar/partials/discipline-list.html',
        controller: 'DisciplineController'
      })
  });
