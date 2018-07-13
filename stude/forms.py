from django import forms

from. import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ('name', )

    def clean_name(self):
            data = self.cleaned_data.get('name')
            if len(data) <= 5:
                raise forms.ValidationError('Message is too short!')
            return data
