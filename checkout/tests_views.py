from django.test import TestCase


class TestViewsCheckout(TestCase):
    def test_get_checkout_page(self):
        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
