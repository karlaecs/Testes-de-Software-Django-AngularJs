DELETE FROM dar_student;
INSERT INTO dar_student (id, name, matriculation, credit_mandatory, credit_elective, departament_id, discipline_id)
VALUES (1,'Alex Carvalho', 98124812, 130, 50, NULL, NULL);

INSERT INTO dar_student (id, name, matriculation, credit_mandatory, credit_elective, departament_id, discipline_id)
VALUES (2, 'Jurema Torres', 9924812, 100, NULL, NULL, NULL);

INSERT INTO dar_student (id, name, matriculation, credit_mandatory, credit_elective, departament_id, discipline_id)
VALUES (3, 'José Vasconcelos', 9915918, NULL, NULL, NULL, NULL);

INSERT INTO dar_student (id, name, matriculation, credit_mandatory, credit_elective, departament_id, discipline_id)
VALUES (4, 'João da Silva', 9914918, NULL, NULL, NULL, NULL);

INSERT INTO dar_student (id, name, matriculation, credit_mandatory, credit_elective, departament_id, discipline_id)
VALUES (5, 'Maria Antônia', 0012398, NULL, NULL, NULL, NULL);


DELETE FROM dar_discipline;
INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (1,'Laboratório de Programação I', 'INF 1622', 70, 1, 1, 0, 'Arndt Von Staa', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (2, 'Estruturas de Dados', 'INF 1620', 60, 1, 0, NULL, 'Marcus Poggi', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (3,'Projeto de Sistema de Software I', 'INF 1624', 40, 0, 1, NULL, 'Carlos Lucena', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (4,'Programação em ponto grande', 'INF 1628', 50, 0, 1, NULL, 'Arndt von Staa', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (5,'Introdução a Ciência da Computação', 'INF 1001', 40, 1, 1, NULL, 'Bruno Feijó', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (6,'Cálculo Numérico', 'INF 1002', 40, 1, 1, 100, 'Marcus Poggi', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (7,'Software Básico', 'INF 1600', 50, 0, 1, 40, 'Arndt Von Staa', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (8,'Hipermídia Adaptativa', 'INF 1303', 30, 0, 1, NULL, 'Daniel Schawbe', NULL, NULL, NULL);

INSERT INTO dar_discipline (id, name, code, number_credit, required, offered, required_credit, teacher, course_id, pre_discipline_id, period_offered)
VALUES (9,'Inglês I', 'LET 1501', 30, 1, 1, NULL, 'Ângela Souza', NULL, NULL, NULL);


DELETE FROM dar_course;
INSERT INTO dar_course (id, name, secretariat_id)
VALUES (1, 'Engenharia de Computação', NULL);

INSERT INTO dar_course (id, name, secretariat_id)
VALUES (2, 'Bacharelado', NULL);

INSERT INTO dar_course (id, name, secretariat_id)
VALUES (3, 'Doutorado – Informática', NULL);

INSERT INTO dar_course (id, name, secretariat_id)
VALUES (4, 'Português – Inglês', NULL);


DELETE FROM dar_secretariat;
INSERT INTO dar_secretariat (id, type, departament_id)
VALUES (1, 0, NULL);

INSERT INTO dar_secretariat (id, type, departament_id)
VALUES (2, 1, NULL);

INSERT INTO dar_secretariat (id, type, departament_id)
VALUES (3, 0, NULL);


DELETE FROM dar_departament;
INSERT INTO dar_departament (id, name)
VALUES (1, 'Departamento Informática');

INSERT INTO dar_departament (id, name)
VALUES (2, 'Departamento Letras');
