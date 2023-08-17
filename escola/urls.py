from django.urls import path,include
from escola.views import *
from rest_framework import routers


router = routers.DefaultRouter('')
router.register('alunos',AlunosViewSet, basename='Alunos')
router.register('cursos',CursosViewSet, basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')
router.register('disciplinas', DisciplinasViewSet, basename='Disciplinas')
router.register('curso-disciplinas',CursoDisciplinaViewSet,basename='CursoDisciplina')


urlpatterns = [
    path('',include(router.get_urls())),
    path('aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas', ListaAlunosMatriculados.as_view()),
    path('curso/<int:pk>/disciplinas', ListaDisciplinasCurso.as_view())

]
# urlpatterns = router.urls