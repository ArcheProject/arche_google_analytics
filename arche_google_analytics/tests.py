# -*- coding: utf-8 -*-
from unittest import TestCase

from fanstatic import get_needed
from fanstatic import init_needed
from pyramid import testing
from zope.component.event import objectEventNotify
from zope.interface import implementer


class IntegrationTests(TestCase):
    
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _mk_view(self, context, request):
        from arche.interfaces import IBaseView
        @implementer(IBaseView)
        class _DummyView(object):
            def __init__(self, context, request):
                self.context = context
                self.request = request
        return _DummyView(context, request)        

    def test_rendered_on_event(self):
        from arche.events import ViewInitializedEvent
        self.config.registry.settings['arche_ga.key'] = 'a_very_secret_code'
        self.config.include('arche_google_analytics')
        init_needed()
        request = testing.DummyRequest()
        view = self._mk_view(None, request)
        objectEventNotify(ViewInitializedEvent(view))
        needed = get_needed()
        self.assertTrue(needed.resources())
        self.assertIn('a_very_secret_code', needed.render())
