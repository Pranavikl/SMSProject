from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

from django import forms
from .models import AddCourse
class AddCourseForm(forms.ModelForm):
    class Meta:
        model=AddCourse
        fields=['student','course','section']

from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']