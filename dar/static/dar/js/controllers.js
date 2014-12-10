'use strict';
var app = angular.module('smicApp');

app.controller('StudentController', [
                '$scope',
                'studentService',
                'disciplineService',
    function ($scope, studentService, disciplineService) {
        studentService.getStudents({}, function(data) {
            $scope.students = data;
        });

        $scope.listDisciplines = function(departament_id, sid) {
            disciplineService.getdisciplinesByDepartament({'id' : departament_id}, function(data) {
                $scope.disciplinesByDepartament = data;

            });

        };

        $scope.log = ' ';
        $scope.matriculateStudent = function(discipline, student) {
            var disciplineCredits = discipline.number_credit,
                disciplineOffered = discipline.offered,
                disciplineCourse = discipline.course,
                disciplineDepartament = discipline.departament,
                disciplineReq = discipline.disciplines,
                disciplineType = discipline.type,
                studentCreditsMandatory = student.credit_mandatory,
                studentCreditsElective = student.credit_elective,
                studentCourse = student.course,
                studentDisciplines = student.disciplines,
                studentDepartament = student.departament,
                studentType = student.type,
                graduation = 1,
                minCredit = 170,
                cont = 0,
                sizeDiscipline = disciplineReq.length;

            function checkDisciplines() {
                for(var i=0; i< sizeDiscipline; i++) {
                    for(var j=0; j < studentDisciplines.length; j++) {
                        if (disciplineReq[i].id == studentDisciplines[j].id) {
                            cont++;
                            break;
                        }
                    }
                }
                if(cont==sizeDiscipline) {
                    return true;
                }
                else {
                    return false;
                }
            }
            var mat = false;
            if(studentDepartament == disciplineDepartament  && disciplineOffered) {
                if(studentType == graduation && (studentCourse==disciplineCourse || disciplineType != graduation)) {
                    if(disciplineType != graduation && studentCreditsMandatory+studentCreditsElective >= minCredit) {
                        $scope.log = "Matriculado com sucesso!";
                        mat = true;
                    }
                    else if (disciplineType == graduation && studentCreditsMandatory >= disciplineCredits && checkDisciplines()) {
                        $scope.log = "Matriculado com sucesso!";
                        mat = true;
                    }
                    else {
                        $scope.log = "Cumpra os créditos obrigatórios ou as disciplinas de pré requisito";
                    }
                }
                else if(studentType != graduation && studentCourse==disciplineCourse && disciplineType != graduation){
                    if (studentCreditsMandatory >= disciplineCredits && checkDisciplines()) {
                        $scope.log = "Matriculado com sucesso!";
                        mat = true;
                    }
                    else
                    {
                        $scope.log = "Cumpra os créditos obrigatórios ou as disciplinas de pré requisito";
                    }
                }
                else {
                    $scope.log = "Disciplina ofertada para alunos da graduação ao qual não pertence ao seu curso";
                }

            }
            else {
                $scope.log = "Disciplina não pertence ao seu curso ou ainda não está sendo ofertada";
            }
        }
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