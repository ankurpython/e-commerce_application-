from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
COLOR_CHOICES=[('1','Red'),('2','Blue'),('3','Black'),('4','Green')]
SIZE_CHOICES=[('1','S'),('2','M'),('3','L'),('4','X-L')]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    color =forms.TypedChoiceField(choices=COLOR_CHOICES,coerce=int)
    size =forms.TypedChoiceField(choices=SIZE_CHOICES,coerce=int)
