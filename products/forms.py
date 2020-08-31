from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Special


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        specials = Special.objects.all()
        friendly_special_names = [
            (s.id, s.get_friendly_name()) for s in specials]

        self.fields['category'].choices = friendly_names
        self.fields['special'].choices = friendly_special_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
