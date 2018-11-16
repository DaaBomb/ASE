from django import forms
from todo_app.models import work_details


class totalwork(forms.ModelForm):
    class Meta():
        model = work_details
        fields = ['work_title','work_descript','deadline']
