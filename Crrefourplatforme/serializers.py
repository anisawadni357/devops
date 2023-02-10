from rest_framework import serializers
from .models import   Livraison
from .models import   chauffer
from .models import   Markets
from .models import   Camion
from .models import   ListeLivraisonFrais
from .models import   ListeLivraisonSec
class LivraisonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livraison
        fields =('id','Destination','NumberPalates','Biere','dateLivraison','Ville','type')

class ChaufferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = chauffer
        fields =('camion','nom','prenom','dateNaissance','password','matricule','nbkilometrage')
class MarketsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Markets
        fields =('Code','Magasin','Longitude','Latitude','Coordinates')
class CamionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Camion
        fields =('N_Vehicule','Designation','Type','Marque','GrandeFamille','Famille','NombrePalette','fonctionnelle')
class ListeLivraisonFraisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ListeLivraisonFrais
        fields =('idLivraison','ville','destination','camion','NumberPalates','dateLivraison','type','etat','nbPalet','taux','etatFinal')
class ListeLivraisonSecSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ListeLivraisonSec
        fields =('idLivraison','ville','destination','camion','NumberPalates','dateLivraison','type','etat','nbPalet','taux','etatFinal')