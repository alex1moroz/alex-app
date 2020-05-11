from django.test import TestCase

from applications.mainpage.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/",
            expected_view_name="mainpage:index",
            expected_view=IndexView,
            expected_template="mainpage/index.html",
        )
