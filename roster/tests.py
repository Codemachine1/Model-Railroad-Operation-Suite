from django.test import TestCase
from django.core.urlresolvers import reverse
from views import *
# Create your tests here.
class testRoster(TestCase):
    def test_add(self):
        numberOfCarsBefore=Cars.objects.count()
        response=self.client.post('/roster/addCar',data={"username":"test","password":"test"})
        numberOfCarsAfter=Cars.objects.count()
        self.assertEqual(response.status_code,200)
        self.assertGreater(numberOfCarsAfter,numberOfCarsBefore)
    def test_list(self):
        response=self.client.get('/roster/listCars')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,)
    def test_delete(self):
        numberOfCarsBefore=Cars.objects.count()
        response=self.client.post('/roster/deleteCar',data={"id":"test"})
        numberOfCarsAfter=Cars.objects.count()
        self.assertEqual(response.status_code,200)
        self.assertLess(numberOfCarsAfter,numberOfCarsBefore)