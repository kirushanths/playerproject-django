from django import forms
from django.utils import html

class DropzoneAreaWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return html.format_html(
            '<div class="dz-message dz-clickable"><span>' +
            '<span class="btn btn-primary">Upload files</span>&nbsp;&nbsp;&nbsp;or drop files here to upload' +
            '</span></div><div class="dropzone-previews"></div>')


class DropzoneField(forms.Field):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        kwargs["widget"] = DropzoneAreaWidget

        super(DropzoneField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return value