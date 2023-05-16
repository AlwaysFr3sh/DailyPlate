from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from homeapp.models import UserSettings


###overwriting form to include email
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    height = forms.DecimalField(
        required=True,
        label='Height (cm)', 
        max_digits=5,
        decimal_places=2,
        max_value=300,
        min_value=0
    )
    weight = forms.DecimalField(
        required=True,
        label='Weight (kg)',
        max_digits=5,
        decimal_places=2,
        max_value=300,
        min_value=0
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        height=self.cleaned_data["height"]
        weight=self.cleaned_data["weight"]
        usersettings = UserSettings(user=user, height=height, weight=weight)

        if commit:
            user.save()
            usersettings.save()
        return user


def signup(request):
    if request.method == 'POST':
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationFormWithEmail()
    return render(request, 'registration/signup.html', {'form': form})

