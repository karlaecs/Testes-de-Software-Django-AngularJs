var darControllers = angular.module('smicApp.controllers', []);

darControllers.controller('StudentController', function StudentController($scope, Student) {
  $scope.students = {};
   
  Student.query(function(response) {
    $scope.students = response;
  });
});

darControllers.controller('DepartamentController', function DepartamentController($scope, Departament) {
  $scope.departaments = {};

  Departament.query(function(response) {
    $scope.departaments = response;
  });
});

darControllers.controller('SecretariatController', function SecretariatController($scope, Secretariat) {
  $scope.secretariats = {};

  Secretariat.query(function(response) {
    $scope.secretariats = response;
  });
});

darControllers.controller('CourseController', function CourseController($scope, Course) {
  $scope.courses = {};

  Course.query(function(response) {
    $scope.courses = response;
  });
});

darControllers.controller('DisciplineController', function DisciplineController($scope, Discipline) {
  $scope.disciplines = {};

  Discipline.query(function(response) {
    $scope.disciplines = response;
  });
});

