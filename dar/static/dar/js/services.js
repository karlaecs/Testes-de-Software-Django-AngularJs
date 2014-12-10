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

app.service('disciplineService', [
            '$resource',

    function ($resource) {
        var disciplinesResource = $resource('api/disciplines');
        var disciplinesByDepartamentResource = $resource('api/disciplines/departament');

        this.getDisciplines= function(params, success, error) {
            return disciplinesResource.query(params, success, error);
        };

        this.getdisciplinesByDepartament= function(params, success, error) {
            return disciplinesByDepartamentResource.query(params, success, error);
        };
    }
]);

app.service('secretariatService', [
            '$resource',

    function ($resource) {
        var secretariatsResource = $resource("api/secretariats");

        this.getSecretariats= function(params, success, error) {
            return secretariatsResource.query(params, success, error);
        };
    }
]);