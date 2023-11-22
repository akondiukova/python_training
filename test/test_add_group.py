# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.auth("admin", "secret")
    app.group.create(Group("1", "2", "3"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.auth("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()

