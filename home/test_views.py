from django.test import TestCase 

class TestViews(TestCase):
    def test_get_home(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/home.html")
        
    def test_get_contact(self):
        page = self.client.get("/home/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/contact.html")
        
    def test_get_about_us(self):
        page = self.client.get("/home/about-us/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/about-us.html")
        