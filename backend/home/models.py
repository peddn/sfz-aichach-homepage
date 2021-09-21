from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):

    show_welcome = models.BooleanField(default=True)
    welcome      = models.CharField(blank=True, max_length=256)
    body         = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('show_welcome', classname="full", heading="Willkommensmeldung anzeigen"),
        FieldPanel('welcome', classname="full", heading="Willkommensmeldung"),
        FieldPanel('body', classname="full", heading="Inhalt")
    ]
