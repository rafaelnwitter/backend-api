#### Escopo do projeto

- A aplicação serve para gerenciar uma faculdade, onde é possivel cadastrar, remover e alterar alunos, cursos e gerar a matricula de alunos em cursos.

- As rotas são 
	- http://localhost:8000 --> Para swagger API
    - http://localhost:8000/students/
    - http://localhost:8000/courses/
    - http://localhost:8000/enrollments/

- Os verbos HTTP utilizados nas rotas são 
	- GET --> http://localhost:8000/students/ e http://localhost:8000/students/id
	- POST --> http://localhost:8000/students/
	- DELETE -->  http://localhost:8000/students/id
	- PUT -->  http://localhost:8000/students/id


- Os filtos disponiveis são
	- http://127.0.0.1:8000/enrollments/? --> status, date_close, date_enroll, student, course
	- http://127.0.0.1:8000/enrollments/?status=Reprovado
	- Sendo Reprovado para alunos reprovados, Aprovado para alunos aprovados e Andamento para cursos em andamento

- [Testes via Postman](https://www.getpostman.com/collections/0eb463ddcd7a45613d74)
