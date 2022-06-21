from django.db import models
from django.db.models import Q

class ListCampaignsManager(models.Manager):
    """" listar campañas"""

    def list_campaigns(self, kword):
        result = self.filter(
            Q(nombre_campania__icontains = kword) | Q(id_campania__icontains = kword)
        )
        return result


class CreateCampaignsManager(models.Manager):
    """" managers crear campañas"""

    def list_campaigns(self):
        
        return self.all()
