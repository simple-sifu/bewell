from django.test import TestCase
from django.urls import reverse, resolve
from .models import HealthFacilities, Description, Location
from rest_framework import status

# Create your tests here.
class FacilitiesTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        hf = HealthFacilities.objects.create(facility=99999, 
                                             name="Elmhurst Hospital", 
                                             openDate='04/05/20')

        Description.objects.create(facility=hf, 
                                   shortDescription="veryshort", 
                                   description='desc')

        Location.objects.create(facility=hf, 
                                address1 = "address",
                                address2 = "address2",
                                city = "city",
                                state = "state",
                                zipCode = "zip",
                                phoneNumber = "ph",
                                faxNumber = "fax",
                                website = "web",
                                countyCode = "cc",
                                county = "cou",
                                latitude ="lat",
                                longitude = "long",
                                location = "loc")

    def test_facilties_content(self):

        hf = HealthFacilities.objects.get(facility=99999) 

        self.assertEquals(hf.name, 'Elmhurst Hospital')  
        self.assertEquals(hf.openDate, '04/05/20')  

    def test_description_content(self):

        desc = Description.objects.get(facility=99999)

        self.assertEquals(desc.shortDescription, 'veryshort')
        self.assertEquals(desc.description, 'desc')

    def test_location_content(self):

        loc = Location.objects.get(facility=99999)

        self.assertEquals(loc.address1, "address")
        self.assertEquals(loc.address2, "address2")
        self.assertEquals(loc.city, "city")
        self.assertEquals(loc.state, "state")
        self.assertEquals(loc.zipCode, "zip")
        self.assertEquals(loc.phoneNumber, "ph")
        self.assertEquals(loc.faxNumber, "fax")
        self.assertEquals(loc.website, "web")
        self.assertEquals(loc.countyCode, "cc")
        self.assertEquals(loc.county, "cou")
        self.assertEquals(loc.latitude, "lat")
        self.assertEquals(loc.longitude, "long")
        self.assertEquals(loc.location, "loc")

    def test_facilities_list_api(self):
        url = reverse('facility-list')

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        facilityDict = dict(dict(self.response.data).get('results')[0])
        self.assertEqual(facilityDict.get('facility'), 99999)
        self.assertEqual(facilityDict.get('name'), 'Elmhurst Hospital')
        descDict = dict(facilityDict.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(facilityDict.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_facilities_detail_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data.get('facility'), 99999)
        self.assertEqual(self.response.data.get('name'), 'Elmhurst Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_missing_facilities_detail_api(self):
        url = reverse('facility-detail', kwargs={"pk":"1"})

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_facilities_list_different_queryParams_api(self):
        url = reverse('facility-list')+'?shortDesc=No'
        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(self.response.data.get('facility'), 99999)

    def test_facilities_list_matching_queryParams_api(self):
        url = reverse('facility-list')+'?shortDesc=veryshort'

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        facilityDict = dict(dict(self.response.data).get('results')[0])
        self.assertEqual(facilityDict.get('facility'), 99999)

    def test_facilities_good_delete_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})

        self.response = self.client.delete(url)

        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_facilities_missing_rec_delete_api(self):
        url = reverse('facility-detail', kwargs={"pk":"1"})

        self.response = self.client.delete('/api/v1/facilities/1/')

        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_facilities_update_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})
        self.response = self.client.get(url)
        newNameObject = self.response.data
        newNameObject.update({"name": 'Jackson Hospital'})
 
        self.response = self.client.put(url, newNameObject, "application/json")

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)        
        self.assertEqual(self.response.data.get('facility'), 99999)
        self.assertEqual(self.response.data.get('name'), 'Jackson Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_facilities_insert_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})
        self.response = self.client.get(url)
        newFacilityObject = self.response.data
        newFacilityObject.update({"facility": 4})
        url = reverse('facility-list')
 
        self.response = self.client.post(url, newFacilityObject, "application/json")

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data.get('facility'), 4)
        self.assertEqual(self.response.data.get('name'), 'Elmhurst Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')
