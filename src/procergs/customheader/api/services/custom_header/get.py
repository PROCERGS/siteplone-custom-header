# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.services import Service
from zope.publisher.interfaces import IPublishTraverse
from zope.interface import implementer
#import procergs.customheader.controlpanels.header_options.controlpanel.IHeaderOptions


@implementer(IPublishTraverse)
class CustomHeaderGet(Service):
    def __init__(self, context, request):
        super(CustomHeaderGet, self).__init__(context, request)

    def reply(self):
        url = (
            api.portal.get_registry_record(
                "procergs.customheader.header_options.url",
                #interface=IMyFeaturedControlPanel,
                default="",
            )
            or ""  # noqa
        )
        subtitle = (
            api.portal.get_registry_record(
                "procergs.customheader.header_options.subtitle",
                #interface=IMyFeaturedControlPanel,
                default="",
            )
            or ""  # noqa
        )

        return {
            "url": url,
            "subtitle": subtitle
        }

