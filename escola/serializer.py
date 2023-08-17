from rest_framework import serializers
from escola.models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        exclude = []

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class CursoDisciplinaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    materia = serializers.ReadOnlyField(source='disciplina.materia')
    class Meta:
        model = CursoDisciplina
        exclude = []



class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self,obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    rg = serializers.ReadOnlyField(source='aluno.rg')
    class Meta:
        model = Matricula
        fields = ['aluno_nome','rg']

class ListaDisciplinasCursoSerialiizer(serializers.ModelSerializer):
    materia = serializers.ReadOnlyField(source='disciplina.materia')
    id_materia = serializers.ReadOnlyField(source='disciplina.id')
    class Meta:
        model = CursoDisciplina
        fields = ['id_materia','materia']
