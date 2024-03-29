from django.db import models

# Create your models here.
class Reserva(models.Model):
  TAMANHO_OPCOES = (
    (0, 'Pequeno'),
    (1, 'Médio'),
    (2, 'Grande')
  )
  TURNO_OPCOES = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde')
  )
  nomeDoPet = models.CharField(max_length=50, verbose_name="Nome do PET", )
  nomeDoDono = models.CharField(max_length=50, verbose_name="Nome do Dono")
  telefone = models.CharField(max_length=15)
  dia = models.DateField(verbose_name="Dia da Reserva")
  observacoes = models.TextField(verbose_name="Observações")
  tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
  turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=5)