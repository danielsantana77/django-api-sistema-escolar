from django.http import JsonResponse
from rest_framework import viewsets,generics
from escola.models import Aluno,Curso,Matricula,Disciplina
from escola.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
    '''Listando todas as matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class CursoDisciplinaViewSet(viewsets.ModelViewSet):
   '''Listando todos os cursos-disciplinas'''
   queryset = CursoDisciplina.objects.all()
   serializer_class = CursoDisciplinaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando matrículas de um aluno(a)"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos(as) matriculados em um Curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

class ListaDisciplinasCurso(generics.ListAPIView):
    """Listando Disciplinas de um curso"""
    def get_queryset(self):
        return CursoDisciplina.objects.filter(curso_id=self.kwargs['pk'])
    serializer_class = ListaDisciplinasCursoSerialiizer

class DisciplinasViewSet(viewsets.ModelViewSet):
    """Lista de Disciplinas"""
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


