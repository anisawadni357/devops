from django.db import models

# Create your models here.
a=(
    ('Autonome','Autonome'),
    ('Remorque','Remorque'),
  
    
)
b=(
    ('MAT-TRANSPO','MAT-TRANSPO'),
    ('MAT-EXPLOI','MAT-EXPLOI'),
   
    
)
f=(
    ('REMORQ-SEC','REMORQ-SEC'),
    ('REMORQ-FRAIS','REMORQ-FRAIS'),
    ('CAM-POILOU-SEC','CAM-POILOU-SEC'),
    ('CAM-POILOU-FRAIS','CAM-POILOU-FRAIS'),
    ('CHARIOT-ELEV','CHARIOT-ELEV'),
    
)
sf=(
    ('REMORQ-SEC','REMORQ-SEC'),
    ('REMORQ-FRAIS','REMORQ-FRAIS'),
    ('10T FRAIS','10T FRAIS'),
    ('3T FRAIS','3T FRAIS'),
    ('10T SEC','10T SEC'),
    ('3T SEC','3T SEC'),
   
    
)
vil=(
    ('tunis','tunis'),
    ('ariana','ariana'),
    ('beja','beja'),
    ('benarous','benarous'),
    ('bizert','bizert'),
    ('gabes','gabes'),
    ('gafsa','gafsa'),
    ('gasrine','gasrine'),
    ('gbeli','gbeli'),
    ('jandouba','jandouba'),
    ('kairawen','kairawen'),
    ('kef','kef'),
    ('mahdia','mahdia'),
    ('manouba','manouba'),
    ('mednine','mednine'),
    ('monastir','monastir'),
    ('nabeul','nabeul'),
    ('seliana','seliana'),
    ('sfax','sfax'),
    ('sidi-bouzid','sidi-bouzid'),
    ('sousse','sousse'),
    ('tatawin','tatawin'),
    ('tozeur','tozeur'),
    ('zaghwen','zaghwen'),
   
    
)
fin=(
    ('0','no'),
    ('1','yes'),
  
)
typ=(
    ('frais','frais'),
    ('sec','sec'),
  
)
eta=(
    ('0','0'),
    ('1','1'),
    ('-1','-1')
  
)
eta=(
    ('0','0'),
    ('1','1'),
    ('-1','-1')
  
)
t=(
    ('terminer','terminer'),
    ('en cours','en cours'),
    ('enpanne','enpanne')
)
class Camion(models.Model):
    N_Vehicule=models.CharField(max_length=100, primary_key=True)
    Designation=models.CharField(max_length=300,null=False)
    Type=models.CharField(max_length=50, choices=a, default='Autonome')
    Marque=models.CharField(max_length=300,null=False)
    GrandeFamille=models.CharField(max_length=50, choices=b, default='MAT-TRANSPO')
    Famille=models.CharField(max_length=50, choices=f, default='REMORQ-SEC')
    fonctionnelle=models.BooleanField(default=True)
   
    NombrePalette=models.CharField(max_length=300,null=False)
    def __str__(self):
        return self.Designation+" ("+self.N_Vehicule+")"
    class Meta:
        verbose_name = 'Vehicle'
class Markets(models.Model):
    Code=models.CharField(max_length=300,primary_key=True)
    Magasin=models.CharField(max_length=300,null=False)
    Longitude=models.CharField(max_length=300,null=False)
    Latitude=models.CharField(max_length=300,null=False)
    Coordinates=models.CharField(max_length=300,null=False)
   
    def __str__(self):
        return "%s" % self.Magasin 
    class Meta:
        verbose_name = 'Market'

class Livraison(models.Model):
    Destination= models.ForeignKey(Markets, on_delete=models.CASCADE,null=True)
    NumberPalates= models.CharField(max_length=100,null=False,verbose_name = 'NombrePalette' )
    Biere= models.CharField(max_length=100,null=True)
    dateLivraison = models.DateField(null=False)
    Ville=models.CharField(max_length=300,choices=vil, default='sfax')
    type=models.CharField(max_length=300,choices=typ, default='sec')
    etat=models.CharField(max_length=300,choices=eta, default='-1')
  
   

    def __str__(self):
        return "Destination %s" % self.Destination

    class Meta:
        ordering = ['-dateLivraison']
        verbose_name = 'Deliverie' 


class chauffer(models.Model):
    camion= models.ForeignKey(Camion, on_delete=models.CASCADE,null=True)
    nom= models.CharField(max_length=100,null=False)
    prenom= models.CharField(max_length=100,null=True)
    dateNaissance = models.DateField(null=False)
    password= models.CharField(max_length=100,null=True)
    matricule= models.CharField(max_length=100,null=False,unique=True)
    nbkilometrage= models.CharField(max_length=100,null=True)

    def __str__(self):
        return "chauffer %s " % self.nom 

    class Meta:
        ordering = ['dateNaissance']
        verbose_name = 'Driver'

class ListeLivraisonFrais(models.Model):
    id= models.AutoField(primary_key=True)
    idLivraison= models.CharField(max_length=100,null=False)
    ville= models.CharField(max_length=100,null=False)
    destination=models.ForeignKey(Markets, on_delete=models.CASCADE,null=True)
    camion= models.CharField(max_length=100,null=False)
    NumberPalates= models.CharField(max_length=100,null=False)
    dateLivraison = models.DateField(null=True)
    type=models.CharField(max_length=300,choices=typ, default='frais')
    etat=models.CharField(max_length=300,choices=eta, default='-1')
    etatFinal=models.CharField(max_length=300,choices=t, default='en cours')
    taux=models.CharField(max_length=100,null=True)
    nbPalet=models.CharField(max_length=100,null=True)
    def __str__(self):
        return "Destination : "+self.ville+" camion : "+self.camion

    class Meta:
        ordering = ['-dateLivraison'] 
        verbose_name = 'Fresh Deliverie'

        
class ListeLivraisonSec(models.Model):
    idLivraison= models.CharField(max_length=100,null=False)
    ville= models.CharField(max_length=100,null=False)
    destination=models.ForeignKey(Markets, on_delete=models.CASCADE,null=True)
    camion= models.CharField(max_length=100,null=False)
    NumberPalates= models.CharField(max_length=100,null=False)
    dateLivraison = models.DateField(null=True)
    type=models.CharField(max_length=300,choices=typ, default='sec')
    etat=models.CharField(max_length=300,choices=eta, default='-1')
    etatFinal=models.CharField(max_length=300,choices=t, default='en cours')
    taux=models.CharField(max_length=100,null=True)
    nbPalet=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return "Destination : "+self.ville+" camion : "+self.camion

    class Meta:
        ordering = ['-dateLivraison']  
        verbose_name = 'Dry Deliverie' 
        

 
