"""Content tests for the homepage Blueprint."""

from application.app import init_app

app = init_app()

def test_main_page_content():
    """GET / should return 200 and contain the word 'Blueprint'."""
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Blueprint" in res.data

def test_about_page_content():
    """GET /about should return 200 and contain the word 'Blueprint'."""
    client = app.test_client()
    res = client.get("/about")
    assert res.status_code == 200
    assert b"Blueprint" in res.data
