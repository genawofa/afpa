from django.db import models

# Create your models here.
class Equipe(models.Model):
    nom_equipe=models.CharField(max_length=30,default='')
    nom_capitaine=models.CharField(max_length=30,null=True)

    def __str__(self):
        # return (self.nom and self.prenom)
        return (self.nom_equipe)

class Participant(models.Model):
    prenom=models.CharField(max_length=30,default='')
    nom=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=100,default='')
    numero_tel=models.CharField(max_length=20,default='')
    equipe=models.ForeignKey(Equipe,on_delete=models.CASCADE,related_name='equipe')

    def __str__(self):
        # return (self.nom and self.prenom)
        return f'{self.nom} {self.prenom}'


class Match(models.Model):
    STATUS=(('--','--'),('gagné','Gagné'),('nul','Nul'),('perdu','Perdu')
            ) 
    aller_retour=(('Match aller','Match aller'),('Match retour','Match retour'))
    equipe_receveuse=models.ForeignKey(Equipe,on_delete=models.CASCADE,related_name='id_eq_rec')
    equipe_visiteuse=models.ForeignKey(Equipe, on_delete=models.CASCADE,related_name='id_eq_vis')
    lieu=models.CharField(max_length=30,default='')
    date_match=models.DateField('date du match',null=True)
    aller_ou_retour=models.CharField(max_length=50,null=True,choices=aller_retour)
    but_equipe_receveuse=models.IntegerField(default=0)
    but_equipe_visiteuse=models.IntegerField(default=0)
    résultat=models.CharField('résultat locaux',max_length=50,null=True,choices=STATUS,default=None)
    points_equipe_receveuse=models.IntegerField(default=0)
    points_equipe_visiteuse=models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.aller_ou_retour}: {self.equipe_receveuse} - {self.equipe_visiteuse} du {self.date_match}'

    def championnat(self):
        self.points_equipe_receveuse=0
        self.points_equipe_visiteuse=0  
        A=self.but_equipe_receveuse<self.but_equipe_visiteuse
        B=self.but_equipe_receveuse>self.but_equipe_visiteuse
        
        if A:
            self.points_equipe_visiteuse += 3
            return self
            
        elif B:
            self.points_equipe_receveuse += 3
            return self
        else:
            self.points_equipe_receveuse += 1
            self.points_equipe_visiteuse += 1
            return self
        save()

    
    
        

