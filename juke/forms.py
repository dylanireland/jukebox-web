from django import forms

class AddSongForm(forms.Form):
    url = forms.CharField(label = "Song URL", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song URL'}))
    coverUrl = forms.CharField(label = "Cover URL", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Cover URL'}))
    title = forms.CharField(label = "Song Title", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song Title'}))
    artist = forms.CharField(label = "Song Artist", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Song Artist'}))
    duration = forms.IntegerField(label = "Duration", widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder': 'Duration (Blocks)', 'oninput': 'durationChanged(this.value);'}))