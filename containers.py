import docker
from flask import make_response, abort

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
    return f"Successfully pulled {name} image."


def createContainer(name):
    try:
        client.containers.run(f'{name}:latest', name={name}, detach=True)
    except docker.errors.DockerException as error:
        abort(
            404, str(error)
        )
    return f"Container {name} is running."


def changeContainerStatus(name, status):
    if status not in ('running', 'exited'):
        abort(
            500, "Please use correct status code."
        )
    else:
        try:
            container = client.containers.get(f"{name}")
        except docker.errors.DockerException as error:
            abort(
                404, str(error)
            )
    if container.status == status:
        abort(
            500, f'Container {name} already {status}.'
        )
    else:
        if container.status == "running":
            container.stop()
        else:
            container.start()
        return f'Container {name} is {status}.'


def removeContainer(name):
    try:
        container = client.containers.get(f"{name}")
    except docker.errors.DockerException as error:
        abort(
            404, str(error)
        )
    if container.status == "running":
        container.stop()
        container.remove()
    else:
        container.remove()

    return f"Successfully removed {name} container."


def getContainerLogs(name, tail='all'):
    try:
        container = client.containers.get(f"{name}")
    except docker.errors.DockerException as error:
        abort(
            404, str(error)
        )
    return container.logs(tail=tail)
