from django.shortcuts import render
from django.http import HttpResponse
from .models import   Livraison
from .models import   chauffer
from .models import   Markets
from .models import   Camion
from .models import   ListeLivraisonFrais
from .models import   ListeLivraisonSec
from django.shortcuts import render
from rest_framework import viewsets
from  .serializers import LivraisonSerializer
from  .serializers import ChaufferSerializer
from  .serializers import MarketsSerializer
from  .serializers import CamionSerializer
from  .serializers import ListeLivraisonFraisSerializer
from  .serializers import ListeLivraisonSecSerializer

from rest_framework.permissions import AllowAny

class LivraisonView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = Livraison.objects.all()
      serializer_class = LivraisonSerializer
class ChauffeurView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = chauffer.objects.all()
      serializer_class = ChaufferSerializer
class MarketsView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = Markets.objects.all()
      serializer_class = MarketsSerializer
class CamionView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = Camion.objects.all()
      serializer_class = CamionSerializer
class ListeLivraisonFraisView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = ListeLivraisonFrais.objects.all()
      serializer_class = ListeLivraisonFraisSerializer
class ListeLivraisonSecView(viewsets.ModelViewSet):
      permission_classes = [AllowAny]
      queryset = ListeLivraisonSec.objects.all()
      serializer_class = ListeLivraisonSecSerializer
#def home(request):
    #event_list=Camion.objects.all()
    #return render(request,'Crrefourplatforme/home.html',{'event':event_list})
# Create your views here.
