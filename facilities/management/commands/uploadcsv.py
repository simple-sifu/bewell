from django.core.management.base import BaseCommand, CommandError
from facilities.models import HealthFacilities, Description, Location
from django.db import IntegrityError
from .enumConstants import HealthFacilityColumns, DescriptionColumns, LocationColumns

import csv


class Command(BaseCommand):
    help = 'Load Facilities csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str)

    def handle(self, *args, **kwargs):

        if HealthFacilities.objects.all().count() > 0:
            val = input("The tables already has records loaded !!! Are you sure you want to load CSV File ?(y/n):") 
            if val.upper() != 'Y':
                self.stdout.write("cvs upload successfully aborted !!")
                return

        csvfile = './data/' + kwargs['filename']

        row_count = 0
        with open(csvfile, 'rt') as file:
            rows = csv.reader(file, delimiter=",", quotechar='"')
            for row in rows:

                if rows.line_num == 1:
                    continue

                try:
                    healthFacility, created = HealthFacilities.objects.update_or_create(
                            facility=row[HealthFacilityColumns.FACILITY_ID],
                            name=row[HealthFacilityColumns.NAME],
                            openDate=row[HealthFacilityColumns.OPEN_DATE],
                    )

                    description, created = Description.objects.update_or_create(
                            facility=HealthFacilities.objects.get(facility=row[HealthFacilityColumns.FACILITY_ID]),
                            shortDescription=row[DescriptionColumns.SHORT_DESCRIPTION],
                            description=row[DescriptionColumns.DESCRIPTION],
                    )

                    locationx, created = Location.objects.update_or_create(
                            facility=HealthFacilities.objects.get(facility=row[HealthFacilityColumns.FACILITY_ID]),
                            address1=row[LocationColumns.FACILITY_ADDRESS_1],
                            address2=row[LocationColumns.FACILITY_ADDRESS_2],                       
                            city=row[LocationColumns.FACILITY_CITY],                       
                            state=row[LocationColumns.FACILITY_STATE],                       
                            zipCode=row[LocationColumns.FACILITY_ZIP_CODE], 
                            phoneNumber=row[LocationColumns.FACILITY_PHONE_NUMBER],  
                            faxNumber=row[LocationColumns.FACILITY_FAX_NUMBER],  
                            website=row[LocationColumns.FACILITY_WEBSITE],  
                            countyCode=row[LocationColumns.FACILITY_COUNTY_CODE],                     
                            county=row[LocationColumns.FACILITY_COUNTY],                       
                            latitude=row[LocationColumns.FACILITY_LATITUDE],                       
                            longitude=row[LocationColumns.FACILITY_LONGITUDE],                                                                
                            location=row[LocationColumns.FACILITY_LOCATION],                       
                    )

                    row_count = rows.line_num

                except IntegrityError as e:
                    self.stdout.write("ErrorMessage: "+str(e))
                    return

            self.stdout.write(" - Loaded " + str(row_count) + " rows into HealthFacilities, Description, and Location Table")
