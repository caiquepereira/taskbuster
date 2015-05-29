# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate

class TestHomePage(TestCase):

    def test_uses_index_template(self):
        """ Ensure we are using the index template on the homepage"""
        activate('en')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "taskbuster/index.html")

    def test_uses_base_template(self):
        """ Ensure the base template is used as part of the homepage"""
        activate('en')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")


