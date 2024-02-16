from django import forms

class ContatoForm(forms.Form):
  nome = forms.CharField()
  email = forms.EmailField()
  mensagem = forms.CharField(widget=forms.Textarea)

class ReservaForm(forms.Form):
  nomeDoPet = forms.CharField(label="Nome do PET")
  telefone = forms.CharField()
  dia = forms.DateField(label="Dia da Reserva", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
  observacoes = forms.CharField(widget=forms.Textarea, label="Observações")