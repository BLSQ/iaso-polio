from django.db import models

from iaso.models import OrgUnit
from iaso.utils.models.soft_deletable import SoftDeletableModel


class Campaign(SoftDeletableModel):
    EPID = models.TextField(null=True, blank=True)
    OBR_name = models.TextField()
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    initial_ou = models.ForeignKey(OrgUnit, on_delete=models.SET_NULL, null=True)

    # Base information

    onset_date = models.DateTimeField(null=True, blank=True)
    cVDPV_notification_date = models.DateTimeField(null=True, blank=True)
    three_level_call_date = models.DateTimeField(null=True, blank=True)
    PV_notification_date = models.DateTimeField(null=True, blank=True)

    virus = models.CharField(max_length=100)
    vaccine = models.CharField(max_length=100)

    # Detection information
    detection_status = models.CharField(max_length=100)
    reponsible = models.CharField(max_length=100)
    #onset date is meaningful
    cVDPV2_notification_date = models.DateTimeField(null=True, blank=True)
    PV2_notification_date = models.DateTimeField(null=True, blank=True)

    #risk assesment info

    def __str__(self):
        return "%s %d" % (self.EPID, self.OBR_name)

