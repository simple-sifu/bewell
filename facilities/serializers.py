from rest_framework import serializers
from .models import HealthFacilities, Location, Description


class DescriptionSerializer(serializers.Serializer):

    shortDescription = serializers.CharField(max_length=15)
    description = serializers.CharField(max_length=50)


class LocationSerializer(serializers.Serializer):

    address1 = serializers.CharField(max_length=40)
    address2 = serializers.CharField(max_length=30, allow_blank=True)
    city = serializers.CharField(max_length=40)
    state = serializers.CharField(max_length=40)
    zipCode = serializers.CharField(max_length=40)
    phoneNumber = serializers.CharField(max_length=40)
    faxNumber = serializers.CharField(max_length=40,  allow_blank=True)
    website = serializers.CharField(max_length=40, allow_blank=True)
    countyCode = serializers.CharField(max_length=40)
    county = serializers.CharField(max_length=40)
    latitude = serializers.CharField(max_length=40)
    longitude = serializers.CharField(max_length=40)
    location = serializers.CharField(max_length=40)


class HealthFacilitiesSerializer(serializers.Serializer):

    facility = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    openDate = serializers.CharField(max_length=50)

    desc = DescriptionSerializer(many=True)
    loc = LocationSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new Facilities instance, given the validated data.
        """
        # print("validated_data -", validated_data)
        HF = HealthFacilities.objects.create(
            facility=validated_data.get('facility'),
            name=validated_data.get('name'),
            openDate=validated_data.get('openDate'),
        )
        HF.save()

        # Remember Desc is a nested object which is an OrderedDict
        validDesc = dict(validated_data.get('desc')[0])
        DESC = Description.objects.create(
            facility=HF,
            shortDescription=validDesc.get('shortDescription'),
            description=validDesc.get('description'),
        )
        DESC.save()

        # Remember loc is a nested object which is an OrderedDict
        validLoc = dict(validated_data.get('loc')[0])
        LOC = Location.objects.create(
            facility=HF,
            address1=validLoc.get('address1'),
            address2=validLoc.get('address2'), 
            city=validLoc.get('city'),
            state=validLoc.get('state'),
            zipCode=validLoc.get('zipCode'),
            phoneNumber=validLoc.get('phoneNumber'),
            faxNumber=validLoc.get('faxNumber'),
            website=validLoc.get('website'),
            countyCode=validLoc.get('countyCode'),
            county=validLoc.get('county'),
            latitude=validLoc.get('latitude'),
            longitude=validLoc.get('longitude'),
            location=validLoc.get('location')
        )
        LOC.save()
        return HF

    def update(self, instance, validated_data):

        # print("validated_data -", validated_data)

        # HF = HealthFacilities.objects.prefetch_related('loc', 'desc').get(facility=validated_data.get('facility'))
        # prefetch doesnt allow me to save DESC or LOC...will need to fetch directly.
        HF = HealthFacilities.objects.get(facility=validated_data.get('facility'))
        HF.facility = validated_data.get('facility')
        HF.name = validated_data.get('name')
        HF.openDate = validated_data.get('openDate')
        HF.save()

        # Remember Desc is a nested object which is an OrderedDict
        validDesc = dict(validated_data.get('desc')[0])
        DESC = Description.objects.get(facility=HF.facility)
        DESC.shortDescription = validDesc.get('shortDescription')  
        DESC.description = validDesc.get('description')
        DESC.save()

        # Remember Loc is a nested object which is an OrderedDict
        validLoc = dict(validated_data.get('loc')[0])
        LOC = Location.objects.get(facility=HF.facility)
        LOC.address1 = validLoc.get('address1')
        LOC.address2 = validLoc.get('address2') 
        LOC.city = validLoc.get('city')
        LOC.state = validLoc.get('state')
        LOC.zipCode = validLoc.get('zipCode')
        LOC.phoneNumber = validLoc.get('phoneNumber')
        LOC.faxNumber = validLoc.get('faxNumber')
        LOC.website = validLoc.get('website')
        LOC.countyCode = validLoc.get('countyCode')
        LOC.county = validLoc.get('county')
        LOC.latitude = validLoc.get('latitude')
        LOC.longitude = validLoc.get('longitude')
        LOC.location = validLoc.get('location')
        LOC.save()

        return HF


        # Remember Desc is a nested object which is an OrderedDict
        # validDesc = validated_data.get('desc')
        # validShortDescription = list(validDesc[0].items())[0][1]
        # validDescription = list(validDesc[0].items())[1][1]