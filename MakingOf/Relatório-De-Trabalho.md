# Relatório De Trabalho - Rafael Magalhães

Comecei a modelação a partir da identificação das entidades e dos seus respetivos atributos. De forma esquemática, organizei as entidades e os atributos que considerei relevantes para cada uma. A primeira versão obtida foi a seguinte:

![009bd68f-43f0-46be-8049-3aa64652f90c](https://github.com/user-attachments/assets/1e7a9092-9062-490e-845e-a9011dc717e4)

Estas são todas as entidades obrigatórias com a adição de uma nova entidade, Professor, que eu adicionei pois tanto a entidade TFC como a Unidade Curricular necessitavam da mesma porque os trabalhos finais de curso têm um orientador e as unidades curriculares também têm um professor. No entanto com o avançar da modelação apercebi-me da necessidade de uma outra entidade chamada Aluno pois as entidades Competencia, Formacao, Licenciatura, Projeto devem estar associadas a uma pessoa que as tem ou fez, por isso reformolei e fiz uma nova versão que é a seguinte:

![93b7a10c-605b-4bca-9e12-a1b86f582b77](https://github.com/user-attachments/assets/0af522cf-3f93-4343-83ac-8dd584b6c1bd)

Depois de alcançar a versão final das entidade e atributos comecei a pensar nas suas relações. Através desse processo cheguei á seguinte versão:

![88ddfdd5-9432-4937-886f-ddba41dc5043](https://github.com/user-attachments/assets/ee22beff-904c-4ba4-bc4e-c25d599b615f)

A correção que é possível ver na imagem deve-se ao facto de-me ter apercebido que uma unidade currícular tem mais que um professor, como por exemplo o professor da teórica não ser o professor da prática. Após esta primeira versão de relações observei que poderiam e deveriam haver mais entre as entidades e por isso obtive esta versão final:

![ff34d355-69a8-46c1-9f0f-8e9a5ebb879a](https://github.com/user-attachments/assets/4f4258e7-2fc5-4dc3-a7f4-a780809f4689)

Neste momento tinha todas as informações necessárias em termos de entidades, atributos e relações para fazer o diagrama ER:

| Entidade               | Atributos                                                                |
|------------------------|--------------------------------------------------------------------------|
| Licenciatura           | Nome, Duracao, Creditos, Informacao                                      |
| Unidade Curricular     | Nome, Professor, Descricao, Creditos, Imagem, Projetos                   |
| Professor              | Nome, Disciplina                                                         |
| TFC                    | Título, Descricao, Autor, Ano, Orientador, Tema                          |
| Projeto                | Titulo, Descricao, DataDeRealizacao, UnidadeCurricular, Tecnologias, Link|
| Tecnologia             | Nome, Tipo, Descricao, Site, Interesse                                   |
| Formacao               | Titulo, Tipo, Instituicao, DataInicio, DataConclusao, Descricao, Aluno   |
| Aluno                  | Nome, Número, Ano, Licenciatura, Formacao                                |
| Competencia            | Nome, Tipo, Nivel, Experiencia, Projetos                                 |
| MakingOF               | Tipo, Descricao, Justificacao, Solucao, UsoIA, DescricaoUsoIA            |


| Entidade 1         | Relação            | Entidade 2         | Cardinalidade        |
|--------------------|--------------------|--------------------|----------------------|
| Licenciatura       | tem                | Unidade Curricular | 1 : N                |
| Unidade Curricular | é lecionada por    | Professor          | 1 : N ou (N : N)     |
| Unidade Curricular | contém             | Projeto            | 1 : N                |
| Projeto            | Usa                | Tecnologia         | 1 : N                |
| Aluno              | frequenta          | Licenciatura       | N : N                |
| Aluno              | realiza            | TFC                | 1 : 1                |
| TFC                | orientado por      | Professor          | 1 : 1                |
| Aluno              | tem                | Formacao           | 1 : N                |
| Competencia        | demonstrada em     | Projeto            | 1 : N                |

# Diagrama ER

![ecaf503d-8645-402a-8c95-87ea0098f69b](https://github.com/user-attachments/assets/df852b08-f298-4664-8381-d00891fa375f)
