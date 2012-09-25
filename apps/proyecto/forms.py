# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Field
from crispy_forms.bootstrap import FormActions
from apps.proyecto.models import Project, Sprint, UserStory

class MessageForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField()
    
    
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('password', css_class='input-xlarge'),
        FormActions( Submit('Ingresar', 'Ingresar', css_class="btn-save"))
        )

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(ProjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Project
        
class SprintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(SprintForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Sprint
        fields= ('titulo','descrip')
        
class StoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(StoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserStory
        exclude = ('sprint')