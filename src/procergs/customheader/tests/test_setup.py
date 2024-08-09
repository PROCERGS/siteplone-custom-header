# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from procergs.customheader.testing import (  # noqa: E501
    PROCERGS_CUSTOMHEADER_INTEGRATION_TESTING,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that procergs.customheader is properly installed."""

    layer = PROCERGS_CUSTOMHEADER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if procergs.customheader is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'procergs.customheader'))

    def test_browserlayer(self):
        """Test that IProcergsCustomheaderLayer is registered."""
        from plone.browserlayer import utils
        from procergs.customheader.interfaces import IProcergsCustomheaderLayer
        self.assertIn(
            IProcergsCustomheaderLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PROCERGS_CUSTOMHEADER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('procergs.customheader')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if procergs.customheader is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'procergs.customheader'))

    def test_browserlayer_removed(self):
        """Test that IProcergsCustomheaderLayer is removed."""
        from plone.browserlayer import utils
        from procergs.customheader.interfaces import IProcergsCustomheaderLayer
        self.assertNotIn(IProcergsCustomheaderLayer, utils.registered_layers())
