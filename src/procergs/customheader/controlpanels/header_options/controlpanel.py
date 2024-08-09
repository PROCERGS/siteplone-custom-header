# -*- coding: utf-8 -*-
from procergs.customheader import _
from procergs.customheader.interfaces import IProcergsCustomheaderLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope.component import adapter
from zope.interface import Interface
from zope import schema

from zope.interface import Invalid
from zope.interface import invariant

class IHeaderOptions(Interface):
    header_type = schema.Choice(
        title=_(
            "Header Type",
        ),
        description=_(
            "",
        ),
        vocabulary="procergs.customheader.HeaderOptions",
        default="default",
        required=True,
        readonly=False,
    )

    subtitle = schema.TextLine(
        title=_(
            "Subtitle",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )

    @invariant
    def validate_start_end(data):
        if data.header_type == "subsecretaria" and data.subtitle is None:
            raise Invalid('Subtitle is required for this Header Type')


class HeaderOptions(RegistryEditForm):
    schema = IHeaderOptions
    schema_prefix = "procergs.customheader.header_options"
    label = _("Header Options")


HeaderOptionsView = layout.wrap_form(
    HeaderOptions, ControlPanelFormWrapper
)



@adapter(Interface, IProcergsCustomheaderLayer)
class HeaderOptionsConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IHeaderOptions
    configlet_id = "header_options-controlpanel"
    configlet_category_id = "Products"
    title = _("Header Options")
    group = ""
    schema_prefix = "procergs.customheader.header_options"
