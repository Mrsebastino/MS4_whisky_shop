from django.test import TestCase
from .forms import OrderForm
# Create your tests here.


class TestOrderForm(TestCase):

    def test_item_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
