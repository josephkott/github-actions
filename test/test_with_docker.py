import os
import pytest
import docker


@pytest.fixture
def client():
    client = docker.from_env()
    return client


@pytest.fixture
def image(client):
    """
    Build Docker image to evaluate tests.
    """

    client.images.build(path=os.getcwd(), tag='test:latest', rm=True,
                        container_limits={'memory': 512 * 1024 * 1024})
    yield client.images.get('test:latest')


def test_image(client, image):
    """
    Show help message from the dockerized tool.
    """
    response = client.containers.run(image.id, '/usr/bin/eagle -h')
    print('\n' + response.decode('utf-8'))
