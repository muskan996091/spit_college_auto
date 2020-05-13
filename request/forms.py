from django.forms import ModelForm

from request.models import attendance

class attendForm(ModelForm):
    class Meta:
        model=attendance;
        fields=['student_name']
        labels={'student_name':_('Name')}
        help_texts={'student_name':('Enter a name')}