# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.auth("admin", "secret")
    app.add_group(Group("1","2","3"))
    app.logout()

def test_add_empty_group(app):
    app.auth("admin", "secret")
    app.add_group(Group("", "", ""))
    app.logout()

