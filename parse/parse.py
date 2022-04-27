"""
Module responsible for the main menu
"""


import click
from execution import execution
from config import config


@click.group()
def main():
    """
    Main app to check/export the JIRA information
    """
    # print("here")


@main.command()
def list_project():
    """
    List all the projects available in JIRA
    """
    execution.list_all_projects()


@main.group()
def export():
    """
    Export a JIRA project information
    """


@export.command()
def by_project():
    """
    You can select the project to export the information
    """
    execution.export_by_project()

# @export.group()
# def everything():
#     """
#     You can export the whole information of all projects
#     """
#     pass


@main.group()
def setup():
    """
    Setup and/or show the basic configuration
    """


@setup.command()
def set_token():
    """
    Set the TOKEN
    """
    config.set_token()


@setup.command()
def show_token():
    """
    Show the TOKEN
    """
    config.show_token()
