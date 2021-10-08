from conda_api import info as info_api
from conda_api import create_env as create_env_api
from conda_api import find_env as find_env_api
from typing import Union, Dict, Any
from fabric.tasks import task
from conda_api import Ctx


@task
def info(ctx: Ctx) -> Dict[str, Any]:
    return info_api(ctx)


@task
def create_env(ctx: Ctx, env_file_path: str) -> Dict[str, Any]:
    create_env_api(ctx, env_file_path)
