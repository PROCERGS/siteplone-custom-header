# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import procergs.customheader


class ProcergsCustomheaderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=procergs.customheader)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'procergs.customheader:default')


PROCERGS_CUSTOMHEADER_FIXTURE = ProcergsCustomheaderLayer()


PROCERGS_CUSTOMHEADER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PROCERGS_CUSTOMHEADER_FIXTURE,),
    name='ProcergsCustomheaderLayer:IntegrationTesting',
)


PROCERGS_CUSTOMHEADER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PROCERGS_CUSTOMHEADER_FIXTURE,),
    name='ProcergsCustomheaderLayer:FunctionalTesting',
)


PROCERGS_CUSTOMHEADER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PROCERGS_CUSTOMHEADER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ProcergsCustomheaderLayer:AcceptanceTesting',
)
