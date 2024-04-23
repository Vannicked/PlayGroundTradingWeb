from django.db import models

# Create your models here.
class Portfolio(models.Model):
    aal = models.IntegerField()
    aapl = models.IntegerField()
    amzn = models.IntegerField()
    bac = models.IntegerField()
    dal = models.IntegerField()
    hmc = models.IntegerField()
    jnj = models.IntegerField()
    jpm = models.IntegerField()
    lly = models.IntegerField()
    luv = models.IntegerField()
    msft = models.IntegerField()
    tm = models.IntegerField()
    tsla = models.IntegerField()
    unh = models.IntegerField()
    v = models.IntegerField()
    totalValue = models.FloatField()

    def __str__(self):
        return f"{self.aal - self.aapl - self.amzn - self.bac - self.dal - self.hmc - self.jnj - self.jpm - self.lly - self.luv - self.msft - self.tm - self.tsla - self.unh - self.v - self.totalValue}"