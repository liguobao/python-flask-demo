# manage.py

import sys
from flask.cli import FlaskGroup
import subprocess
import traceback
import click
import sys
from loguru import logger
from src import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(['flake8', 'src'])


@cli.command()
@click.option('--job_name')
@click.option('--job_body')
def start_job(job_name="", job_body="{}"):
    """start job """
    try:
        logger.info(f"job_name:{job_name},job_body:{job_body}")
        #job_obj = find_job_object(job_name)
        #job_obj.run(job_body)
    except Exception as err:
        logger.error(f"start_job fail,err:{str(err)}")
        traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    cli()
