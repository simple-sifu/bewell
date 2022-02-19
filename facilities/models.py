from django.db import models

# Create your models here.


class HealthFacilities(models.Model):
    facility = models.IntegerField("Facility ID", primary_key=True, db_index=True)
    name = models.CharField("Facility Name", max_length=50)
    openDate = models.TextField("Facility Open Date", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Description(models.Model):
    facility = models.ForeignKey(HealthFacilities, on_delete=models.CASCADE, db_index=True, verbose_name="the related HealthFacility", related_name='desc')
    shortDescription = models.CharField("Short Description", max_length=15)
    description = models.CharField("Description", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shortDescription


class Location(models.Model):
    facility = models.ForeignKey(HealthFacilities, on_delete=models.CASCADE, db_index=True, verbose_name="this related HealthFacility", related_name='loc')
    address1 = models.CharField("Facility Address 1", max_length=40)
    address2 = models.CharField("Facility Address 2", max_length=30, blank=True)
    city = models.CharField("Facility City", max_length=40)
    state = models.CharField("Facility State", max_length=40)
    zipCode = models.CharField("  Zip Code", max_length=40)
    phoneNumber = models.CharField("Facility Phone Number", max_length=40)
    faxNumber = models.CharField("  Fax Number", max_length=40)
    website = models.CharField("Facility Website", max_length=40)
    countyCode = models.CharField("Facility County Code", max_length=40)
    county = models.CharField("Facility County", max_length=40)
    latitude = models.CharField("Facility Latitude", max_length=40)
    longitude = models.CharField("Facility Longitude", max_length=40)
    location = models.CharField(" Facility Location", max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
