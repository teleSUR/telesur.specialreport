# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory
from five import grok
from plone.dexterity.interfaces import IDexterityContainer

_ = MessageFactory('telesur.specialreport')


class TelesurSpecialreportView(grok.View):
    grok.context(IDexterityContainer)
    grok.require('zope2.View')


class TelesurSpecialreportFolderView(grok.View):
    grok.context(IDexterityContainer)
    grok.require('zope2.View')
