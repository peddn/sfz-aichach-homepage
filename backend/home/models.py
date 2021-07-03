from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):

    show_actual = models.BooleanField(default=True)
    actual      = RichTextField(blank=True)
    body        = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('show_actual', classname="full"),
        FieldPanel('actual', classname="full"),
        FieldPanel('body', classname="full")
    ]
