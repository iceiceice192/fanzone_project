
from django import forms

class PreferencesForm(forms.Form):
    def __init__(self, *args, teams_choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if teams_choices is None:
            teams_choices = []
        self.fields['favorites'] = forms.MultipleChoiceField(
            choices=teams_choices,
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label='Выбери свою любимую команду'
        )
        self.fields['theme'] = forms.ChoiceField(
            choices=[('light','Light'), ('dark','Dark')],
            required=True,
            label='Theme'
        )
        self.fields['lang'] = forms.ChoiceField(
            choices=[('en','English'), ('ru','Русский')],
            required=True,
            label='Language'
        )
