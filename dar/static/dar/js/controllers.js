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