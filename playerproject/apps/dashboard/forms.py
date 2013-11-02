from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from dazzle.libs.fields import SubmitButtonField
from dazzle.apps.dashboard.fields import DropzoneField

from dazzle.libs.utils import (
    zipreader
)

class DZTemplateUploadForm(forms.Form):
    template_name = forms.CharField(help_text='A unique name for your template', max_length=100)
    template_file  = forms.FileField(help_text='Upload a zip containing the files of your template')
    # dropzone = DropzoneField(label="Template Files") 
    submit = SubmitButtonField(label="", initial=u"Upload")

    def clean_template_file(self):
        template_zipfile = self.cleaned_data['template_file']
        template_files = []

        for result, archive, zip_file in zipreader.process(template_zipfile):
            if result.success:
                template_files.append(archive)
            else:
                raise ValidationError(_(result.message), 
                    code='invalid',)

        if not template_files:
            raise ValidationError(_('No files found in the zip file'), 
                code='invalid',)

        return template_zipfile

