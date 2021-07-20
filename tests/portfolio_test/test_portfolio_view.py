from flask.testing import FlaskClient
from ipdb import set_trace


def test_should_retrieve_a_portfolio_with_transactions(
    app_client: FlaskClient, new_user, new_transaction
):
    response = app_client.post('/api/register', json=new_user)
    token = response.get_json()['token']
    headers = {'Authorization': f'Bearer {token}'}

    app_client.post('/api/transactions/register', json=new_transaction, headers=headers)
    portfolio = app_client.get('/api/portfolio/list', headers=headers)

    assert portfolio.status_code == 200
    assert isinstance(portfolio.get_json(), list)
    # colocar outros testes, se necessários


def test_should_retrieve_a_portfolio_with_no_transactions(
    app_client: FlaskClient, new_user
):
    user = app_client.post('/api/register', json=new_user)

    token = user.get_json()['token']
    headers = {'Authorization': f'Bearer {token}'}

    portfolio = app_client.get('/api/portfolio/list', headers=headers)

    assert portfolio.get_json() == []
