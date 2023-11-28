# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

def test_add_group(app):
    app.group.create(Group("1", "2", "3"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

