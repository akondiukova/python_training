import pytest
from fixture.application import Application

def test_edit_contact(app):
    app.contact.test_delete_contact()