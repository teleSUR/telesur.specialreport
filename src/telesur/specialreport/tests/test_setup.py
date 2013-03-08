# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from telesur.specialreport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of telesur.specialreport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if telesur.specialreport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('telesur.specialreport'))

    def test_uninstall(self):
        """Test if telesur.specialreport is cleanly uninstalled."""
        self.installer.uninstallProducts(['telesur.specialreport'])
        self.assertFalse(self.installer.isProductInstalled('telesur.specialreport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ITelesurSpecialreportLayer is registered."""
        from telesur.specialreport.interfaces import ITelesurSpecialreportLayer
        from plone.browserlayer import utils
        self.failUnless(ITelesurSpecialreportLayer in utils.registered_layers())
