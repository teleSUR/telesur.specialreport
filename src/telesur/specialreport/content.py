from five import grok
from zope import schema
from plone.directives import dexterity, form
from plone.namedfile.field import NamedFile, NamedBlobImage
from telesur.specialreport import _


class ISpecialReport(form.Schema):
    """
    A session than contains questions
    """

    file = NamedFile(
        title=_(u'Flash file'),
        required=True,
    )

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u'Image for the special'),
        required=True,
    )

    width = schema.Int(
        title=_(u'Width'),
        default=640,
    )

    height = schema.Int(
        title=_(u'Height'),
        default=480,
    )