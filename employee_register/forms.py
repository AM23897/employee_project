from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('empFullName','mobile','emp_code','position')
        labels = {
            'empFullName':'Employee Full Name',
            'mobile':'Employee Mobile No',
            'emp_code':'Employee Code',
            'position':'Employee Designation'
        }
    def __init__(self, *args, **kwards):
        super(EmployeeForm,self).__init__(*args, **kwards)
        self.fields['position'].empty_label = 'Select Designation'
        self.fields['emp_code'].required = False
