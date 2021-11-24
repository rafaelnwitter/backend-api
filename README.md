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


- Para filtrar é utilizado a seguinte rota
	- http://127.0.0.1:8000/enrollments/?status=Rp
	- Sendo Rp para alunos reprovados, Ap para alunos aprovados e Ad para cursos em andamento

- [Testes via Postman](https://go.postman.co/workspace/My-Workspace~bdd094bb-68b6-4bdf-8d09-99e05e7bb8cc/collection/18510677-f88f7e34-e2be-439b-bf97-fbc4841dfcc5)