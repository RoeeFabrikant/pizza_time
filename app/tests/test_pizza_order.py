import pytest
import requests
import time

# make a a request and check the response code and message
def http_request(url, request_type, body = None):
  max_retries=3
  retry_delay=5

  for i in range(max_retries):
    try:
      if request_type == 'get':
        response = requests.get(url)
      elif request_type == 'post':
        response = requests.post(url, data = body)
      return response
    except requests.exceptions.RequestException as e:
      if i < max_retries - 1:
        time.sleep(retry_delay)
  return response

@pytest.fixture
def run_docker():
    import docker
    client = docker.from_env()

    try:
      client.images.build(tag='roeef/pizza_time_test', path='/Users/i563495/Development/pizza_time')
      client.containers.run(image='roeef/pizza_time_test',
                            name='pytest_tests',
                            detach=True,
                            stdout=True,
                            ports={'8080': 8080})
      yield
    except Exception as e:
      raise AssertionError(e)

    for container in client.containers.list():
      if 'pytest_tests' in container.name:
        print('Cleaning', container.name, '...')
        container.kill()

    client.containers.prune()

@pytest.mark.usefixtures('run_docker')
class TestLiveServer:

  def test_application_health(self):
    response = http_request("http://localhost:8080/health", 'get')
    response_message = response.json()
    assert response.status_code == 200
    assert 'App is healthy' in response_message['message']

  def test_application_ping(self):
    response = http_request("http://localhost:8080/ping", 'get')
    response_message = response.json()
    assert response.status_code == 200
    assert 'Pong!' in response_message['message']

  def test_pizza_order(self):
    request_data = {'pizza_type': 'napolitana', 'size': 'fammily', 'amount': 3}
    response = http_request("http://localhost:8080/order", 'post', request_data)
    response_message = response.json()
    assert response.status_code == 200
    assert 'Order placed successfully!' in response_message['message']

  def test_wrong_way_pizza_order(self):
    request_data = {'pizza_type': 'napolitana', 'size': 'large', 'amount': 3}
    response = http_request("http://localhost:8080/order", 'post', request_data)
    response_message = response.json()
    assert response.status_code == 400
    assert 'The pizza size does not exist' in response_message['message']