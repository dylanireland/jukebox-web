from django import forms

class AddSongForm(forms.Form):
    url = forms.CharField(label = "Song URL", required = False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song URL'}))
    coverUrl = forms.CharField(label = "Cover URL", required = False, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Cover URL'}))
    title = forms.CharField(label = "Song Title", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song Title'}))
    artist = forms.CharField(label = "Song Artist", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song Artist'}))
    duration = forms.IntegerField(label = "Duration", widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder': 'Duration (Blocks)', 'oninput': 'durationChanged(this.value);'}))
    value = forms.IntegerField(label = "Value")
    song = forms.FileField(allow_empty_file=True, required = False)
    covfile = forms.FileField(allow_empty_file=True, required = False)
