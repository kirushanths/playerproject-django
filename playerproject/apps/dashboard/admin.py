from django.contrib import admin

from .models import (
    DZTemplate,
    DZTemplateSource,
    DZSite,
    DZSiteSettings,
    DZSiteOwnership,
    DZSiteCommit
)
 
admin.site.register(DZTemplate)
admin.site.register(DZTemplateSource)
admin.site.register(DZSite)
admin.site.register(DZSiteSettings)
admin.site.register(DZSiteOwnership)
admin.site.register(DZSiteCommit)