from django import forms

class AddTodoForm(forms.Form):
    title=forms.CharField(required=True,max_length=150,help_text='Todo list title')
    information=forms.CharField(required=False,widget=forms.Textarea)