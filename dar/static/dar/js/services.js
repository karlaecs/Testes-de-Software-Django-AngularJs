// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('smicApp.services', ['ngResource'])
  .factory('Departament', function($resource) {
    return $resource('/api/departaments/:id');
  })
  .factory('Secretariat', function($resource) {
    return $resource('/api/secretariats/:id');
  })
  .factory('Course', function($resource) {
    return $resource('/api/courses/:id');
  })
  .factory('Student', function($resource) {
    return $resource('/api/students/:id');
  })
 .factory('Discipline', function($resource) {
    return $resource('/api/disciplines/:id');
  })
