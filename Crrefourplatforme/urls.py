from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livraison', views.LivraisonView)
router.register('chauffeur', views.ChauffeurView)
router.register('camion', views.CamionView)
router.register('markets', views.MarketsView)
router.register('listelivraisonFrais', views.ListeLivraisonFraisView)
router.register('listelivraisonSec', views.ListeLivraisonSecView)
urlpatterns = [
path('api/', include(router.urls))    
   
]