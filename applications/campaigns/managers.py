from django.db import models
from django.db.models import Q

class ListCampaignsManager(models.Manager):
    """" listar campañas"""

    def list_campaigns(self, kword):
        result = self.filter(
            Q(nombre_campania__icontains = kword) | Q(id_campania__icontains = kword)
        )
        return result

class SearchCampaignsManager(models.Manager):
    """" managers buscar campañas"""

    def search_campaigns(self, query):
        result = self.filter(
            Q(nombre_campania__icontains = query) | Q(id_campania__icontains = query)
        )
        return result

class CreateCampaignsManager(models.Manager):
    """" managers crear campañas"""

    def list_campaigns(self):
        
        return self.all()
