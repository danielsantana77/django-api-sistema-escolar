from django.contrib import admin
from escola.models import Aluno,Curso,Matricula,Disciplina,CursoDisciplina

# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento','numero')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20
    exclude = ['numero']

admin.site.register(Aluno,Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)


admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id','aluno','curso','periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)


class Disciplinas(admin.ModelAdmin):
    list_display = ('id', 'materia')
    list_display_links = ('id','materia',)

admin.site.register(Disciplina,Disciplinas)


class CursoDisciplinas(admin.ModelAdmin):
    list_display = ('id','curso', 'disciplina')
    list_display_links = ('id',)

admin.site.register(CursoDisciplina,CursoDisciplinas)
