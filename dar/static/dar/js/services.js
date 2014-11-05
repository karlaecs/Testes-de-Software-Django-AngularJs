'use strict';
var app = angular.module('smicApp');

app.service('studentService', [
            '$resource',

    function ($resource) {
        var studentsResource = $resource("api/students");

        this.getStudents = function(params, success, error) {
            return studentsResource.query(params, success, error);
        };
    }
]);