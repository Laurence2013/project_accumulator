from django.test import TestCase, RequestFactory
from accumulator.views import IndexPageGamesView

class AllRequestsShould(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_TheIndexPage(self):
        request = self.factory.get('/index/$')
        response = IndexPageGamesView.as_view()(request)
        self.assertEqual(response.status_code, 200)
