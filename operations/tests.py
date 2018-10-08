from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class UsersViewTests(TestCase):
    def test_redirect_to_login(self):
        response=self.client.get(reverse('operatons:mainPage'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Login")
    def test_login_dispatcher_handler(self):
        response=self.client.post(reverse('operatons:mainPage'),data={"username":"test","password":"test"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"")
    def test_login_operator_handler(self):
        response=self.client.post(reverse('operatons:mainPage'),data={"username":"test1","password":"test1"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"")