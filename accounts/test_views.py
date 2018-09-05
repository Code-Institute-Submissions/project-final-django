from django.test import TestCase 

class TestViews(TestCase):
    def test_get_register(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/register.html")
        
