from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . models import Vehicle

class VehicleForm(forms.ModelForm):
	"""Form created to edit Vehicle entity"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Submit'))

	class Meta:
		model = Vehicle
		fields = '__all__'