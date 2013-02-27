# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.flash_specials.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.flash_specials into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.flash_specials is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.flash_specials'))

    def test_uninstall(self):
        """Test if collective.flash_specials is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.flash_specials'])
        self.assertFalse(self.installer.isProductInstalled('collective.flash_specials'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveFlash_specialsLayer is registered."""
        from collective.flash_specials.interfaces import ICollectiveFlash_specialsLayer
        from plone.browserlayer import utils
        self.failUnless(ICollectiveFlash_specialsLayer in utils.registered_layers())
