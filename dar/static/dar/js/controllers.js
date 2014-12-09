'use strict';
var app = angular.module('smicApp');

app.controller('StudentController', [
                '$scope',
                'studentService',
    function ($scope, studentService) {
        studentService.getStudents({}, function(data) {
            $scope.students = data;
        });
    }
]);

app.controller('DisciplineController', [
                '$scope',
                'disciplineService',
    function ($scope, disciplineService) {
        disciplineService.getDisciplines({}, function(data) {
            $scope.disciplines = data;
        });
    }
]);

app.controller('SecretariatController', [
                '$scope',
                'secretariatService',
    function ($scope, secretariatService) {
        secretariatService.getSecretariats({}, function(data) {
            $scope.secretariats = data;
        });
    }
]);