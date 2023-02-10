from dataclasses import field
from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
from .models import Camion
from .models import Markets
from .models import Livraison
from .models import chauffer
from .models import ListeLivraisonFrais
from .models import ListeLivraisonSec
from import_export.admin import ImportExportModelAdmin
admin.site.site_header="Carrefour"

class AfficheListeLivraisonFrais(ImportExportModelAdmin):
    model = ListeLivraisonFrais
   
   
    list_filter =('dateLivraison','camion')
    ordering = ['dateLivraison']
    search_fields=['dateLivraison']
    list_display =('dateLivraison','ville','destination','camion','type','nbPalet','taux','etatFinal')
    list_filter =(('dateLivraison', DateRangeFilter),'etatFinal')  
class AfficheLivraison(ImportExportModelAdmin):
    model = Livraison
   
    list_display =['dateLivraison','NumberPalates','Ville','type']
    list_filter =(('dateLivraison', DateRangeFilter),('type'),)
   
class AfficheListeLivraisonSec(ImportExportModelAdmin):
    model = ListeLivraisonSec
   
    list_display =('dateLivraison','ville','destination','camion','type','nbPalet','taux','etatFinal')
    list_filter =(('dateLivraison', DateRangeFilter),'etatFinal')

class AfficheListeCamion(ImportExportModelAdmin):
    model = Camion
   
    list_display =('N_Vehicule','Designation','Type','Marque','GrandeFamille','Famille','NombrePalette','fonctionnelle')

class AfficheMarkets(ImportExportModelAdmin):
    model = Markets
   
    list_display =('Code','Magasin','Coordinates')
class AfficheChauffer(ImportExportModelAdmin):
    model = chauffer
   
    list_display =('nom','prenom','camion')
    




admin.site.register(Camion,AfficheListeCamion)
admin.site.register(Markets,AfficheMarkets)
admin.site.register(Livraison,AfficheLivraison)
admin.site.register(chauffer,AfficheChauffer)
admin.site.register(ListeLivraisonFrais,AfficheListeLivraisonFrais)
admin.site.register(ListeLivraisonSec,AfficheListeLivraisonSec)