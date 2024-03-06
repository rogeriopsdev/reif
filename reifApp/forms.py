from django import forms
from datetime import datetime

from reifApp.models import Discente, Curso, Campus, Evento, Prato, Acesso, Entrada, Acao


class Discente_Form(forms.ModelForm):
    class Meta:
        model = Discente
        fields = ['nome_discente', 'mat_discente', 'email_discente', 'id_campus','cpf_discente','desc_curso_discente', 'id_curso',
                  'edital_discente','ref_cafe','ref_almoco','ref_janta', 'foto_discente', 'qr_discente']
    nome_discente = forms.CharField(label="Nome:")
    mat_discente = forms.CharField(label="Matrícula:")
    email_discente = forms.EmailField(label="e-mail:")
    # id_campus =forms.CharField(label="Campus:")
    #desc_curso_discente = forms.CharField(label="Nome do Curso:")
    # id_curso =forms.CharField(label="Id do Curso:")
    cpf_discente =forms.CharField(label="CPF:")
    edital_discente = forms.CharField(label="Nº do edital:")
    ref_cafe = forms.BooleanField(label="Café", required=False)
    ref_almoco = forms.BooleanField(label="Almoço", required=False)
    ref_janta = forms.BooleanField(label="Janta", required=False)
    #qr_discente = forms.CharField(label="Nº do Valor:")

    def __init__(self, *args, **kwargs):
        super(Discente_Form, self).__init__(*args, **kwargs)
        # Set the initial value for qr_discente based on mat_discente
        self.fields['qr_discente'].initial = self['mat_discente'].value()
    #foto_discente = forms.ImageField(label="Foto:")




class Curso_Form(forms.ModelForm):
    TURNO_CHOICES = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
        ('Integral', 'Integral'),
        ('Outro', 'Outro'),

    ]

    class Meta:
        model = Curso
        fields = ['cod_curso', 'nome_curso', 'turno_curso', 'foto_curso']

    cod_curso = forms.CharField(label='Código:')
    nome_curso = forms.CharField(label='Nome do Curso:')
    turno_curso = forms.ChoiceField(
        label='Turno:',
        choices=TURNO_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='Diurno'
    )
    foto_curso = forms.ImageField(label='Logotipo:')


class Campus_Form(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome_campus', 'foto_campus']

    nome_campus = forms.CharField(label='Nome:')
    foto_campus = forms.ImageField(label='Foto:')


class Campus_Form(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome_campus', 'foto_campus']

    nome_campus = forms.CharField(label='Nome:')
    foto_campus = forms.ImageField(label='Foto:')




class Evento_Form(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Evento
        fields = ['nome_evento', 'data_inicio', 'data_fim', 'abre']

    nome_evento = forms.ModelChoiceField(
        label='Turno:',
        queryset=Acao.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-select'}),
        initial='Diurno'
    )
    data_inicio = forms.DateTimeField(label='Início',
                                      widget=forms.DateTimeInput(
                                          format='%Y-%m-%dT%H:%M',
                                          attrs={
                                              'type': 'datetime-local',
                                          }
                                      ),
                                      input_formats=('%Y-%m-%dT%H:%M',),
                                      )
    data_fim = forms.DateTimeField(
        label='Término',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type': 'datetime-local',
            }
        ),
        input_formats=('%Y-%m-%dT%H:%M',),
    )
    abre = forms.BooleanField(label="Status", required=False)
    #fecha = forms.BooleanField(label="Aberto", required=False)


class Acao_Form(forms.ModelForm):
    class Meta:
        model= Acao
        fields= ['nome_acao']

    nome_acao = forms.CharField(label='Nome')


class Prato_Form(forms.ModelForm):
    class Meta:
        model= Prato
        fields= ['nome_prato','foto_prato']

    nome_prato = forms.CharField(label='Nome')
    foto_prato = forms.ImageField(label="Foto:")


class Acesso_Form(forms.ModelForm):
    class Meta:
        model = Acesso
        fields =['id_discente', 'nome_disc_acesso','id_evento','id_prato','nome_evento_acesso']
    #id_discente = forms.CharField(label='Discente')
   # id_evento = forms.CharField(label='Evento')
    #id_prato = forms.CharField(label='Prato')


class Entrada_Form(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['id_discente', 'nome_disc_entrada', 'id_evento', 'nome_evento_entrada', 'entrada']

    id_discente = forms.ModelChoiceField(
        label='Discente',
        queryset=Discente.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-select'}),
    )

    nome_disc_entrada = forms.CharField(label='Nome')
    id_evento = forms.CharField(label='Evento')
    nome_evento_entrada = forms.CharField(label='Nome')

    entrada = forms.DateTimeField(
        label='Fecha',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type': 'datetime-local',
            }
        ),
        input_formats=('%Y-%m-%dT%H:%M',),
    )