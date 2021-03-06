from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Search anything...",
                "id": "custom_search_id",
            }
        ),
        required=False,
    )
