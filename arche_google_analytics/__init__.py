# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logging import getLogger

from fanstatic import Library
from fanstatic.core import Resource

logger = getLogger(__name__)


library = Library('arche_ga', '.', ignores='*')

_ga_default_tpl = \
"""<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', '%s', 'auto');
ga('send', 'pageview');
</script>"""


class RenderGA(object):

    def __init__(self, ga_code):
        self.ga_code = ga_code
        self.ga_tpl = _ga_default_tpl

    def __call__(self, url):
        return str(self.ga_tpl % self.ga_code)


def need_subscriber(view, *args):
    """ Subscriber that expects view object that has request as an attribute.
        This could really be any kind of view object.
    """
    view.request.registry._arche_ga_res.need()

def includeme(config):
    """ Pyramid hook. Will work out of the box with Arche installed,
        otherwise create a subscriber yourself.
    """
    try:
        from arche.interfaces import IViewInitializedEvent
        from arche.interfaces import IBaseView
        arche_ga_key = config.registry.settings.get('arche_ga.key', False)
        if arche_ga_key:
            _render_ga = RenderGA(arche_ga_key)
            config.registry._arche_ga_res = Resource(library, '.', renderer = _render_ga)
            config.add_subscriber(need_subscriber, (IBaseView, IViewInitializedEvent))
            logger.debug("Including arche_google_analytics on all IBaseView views")
        else:
            logger.info("No arche_ga.key in settings, won't include subscriber")
    except ImportError:
        logger.warn("Arche not found so you have to include the subscriber yourself.")
