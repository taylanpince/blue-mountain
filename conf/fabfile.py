from fabric.api import *
from fabric.contrib.console import confirm


env.staging_path = "blue-mountain"
env.production_path = "blue-mountain-production"
env.root_dir = "/home/bluemountainteam/sites"
env.project_dir = "src/blue-mountain"
env.user = "bluemountainteam"
env.hosts = [
    "184.106.172.234",
]

def deploy_staging():
    """
    Deploy staging site
    """
    deploy(env.staging_path)

def deploy_production():
    """
    Deploy production site
    """
    deploy(env.production_path)

def deploy(path):
    """
    Deploy the latest version
    """
    update(path)
    update_pip(path)
    syncdb(path)
    restart(path)

def update(path):
    """
    Updates project source
    """
    run('cd %s/%s/%s; git pull' % (env.root_dir, path, env.project_dir))

def version(path):
    """
    Show last commit to repo on server
    """
    run('cd %s/%s/%s; git log -1' % (env.root_dir, path, env.project_dir))

def restart(path):
    """
    Restart Apache process gracefully
    """
    run('touch %s/%s/%s/conf/bluemountain.wsgi' % env.root_dir, path, env.project_dir)

def update_pip():
    """
    Update pip requirements
    """
    virtualenv_run('pip install -E %s/%s -r %s/%s/%s/conf/requirements.pip' % (env.root_dir, path, env.root_dir, path, env.project_dir), path)

def syncdb():
    """
    Run syncdb and apply south migrations
    """
    virtualenv_run('manage.py syncdb', path)
    virtualenv_run('manage.py migrate', path)

def virtualenv_run(cmd, path):
    """
    Runs a command using the virtualenv environment
    """
    require('root_dir')

    return run('source %s/%s/bin/activate; %s' % (env.root_dir, path, cmd))
