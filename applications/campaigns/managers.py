from django.db import models

class CampaignsManager(models.Manager):
    """" managers para las campañas"""

    def list_campaigns(self):
        return self.all()

class SearchCampaignsManager(models.Manager):
    """" managers buscar campañas"""

    def search_campaigns(self, kword):
        result = self.filter(
            nombre_campania__icontains = kword
        )
        return result