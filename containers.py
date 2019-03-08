import docker
from flask import make_response, abort, jsonify

client = docker.from_env()


def listContainers():
    all_containers = []
    for c in client.containers.list(all=True):
        all_containers.append([c.short_id, c.status, c.name])
    return all_containers


def getContainer(name):
    try:
        c = client.containers.get(f"{name}")
    except docker.errors.DockerException as error:
        abort(
            404, str(error)
        )
    container_params = [c.short_id, c.status, c.name]
    return container_params


def pullImage(name):
    client.images.pull(f'{name}:latest')
    return print(f"Successfully pulled {name} image.")


def createContainer(name):
    client.containers.run(f'{name}:latest', name={name}, detach=True)
    return print(f"Container {name} is running.")


def removeContainer(name):
    container = client.containers.get(f"{name}")
    if container.status == "running":
        container.stop()
        container.remove()
    else:
        container.remove()

    return print(f"Successfully removed {name} container.")
