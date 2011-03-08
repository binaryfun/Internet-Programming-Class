from django.db import models

class siteID(models.Model):
    websiteName = models.CharField(max_length=100)
    date_added = models.DateTimeField('Time Now')
    def __unicode__(self):
        return self.websiteName

class workLog(models.Model):
    websiteName = models.ForeignKey(siteID)
    notes  = models.CharField(max_length=500)
    date_added = models.DateTimeField('Time Now')
    def __unicode__(self):
        return self.websiteName.websiteName
