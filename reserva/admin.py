from django.contrib import admin
from reserva.models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display = ['nomeDoPet', 'nomeDoDono', 'dia', 'turno']
  search_fields = ['nomeDoPet', 'nomeDoDono']
  list_filter = ['dia', 'turno', 'tamanho']