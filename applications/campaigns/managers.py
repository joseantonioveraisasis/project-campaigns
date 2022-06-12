from django.db import models
from django.db.models import Q

class CampaignsManager(models.Manager):
    """" managers para las campañas"""

    def list_campaigns(self):
        return self.all()

class SearchCampaignsManager(models.Manager):
    """" managers buscar campañas"""

    def search_campaigns(self, kword):
        result = self.filter(
            Q(nombre_campania__icontains = kword) | Q(id_campania__icontains = kword)
        )
        return result

class CreateCampaignsManager(models.Manager):
    """" managers crear campañas"""

    def list_campaigns(self):
        
        return self.all()
