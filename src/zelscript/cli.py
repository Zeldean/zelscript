#!/usr/bin/env python3
import click
from pathlib import Path

from .commands.choice import choose as choose_func
from .commands.timer import timer as timer_func
from .commands.welcome import welcome as welcome_func
from .commands.rename_sequential import rename
from .commands.convert_to_png import convert_to_png

@click.group()
def script():
    """Script utilities and tools"""
    pass

@script.command()
@click.argument('options', nargs=-1, required=True)
def choose(options):
    """Make a choice from given options (runs 11 rounds + winner)"""
    choose_func(options)

@script.command()
def welcome():
    """Display welcome message with ASCII art"""
    welcome_func()

@script.command()
@click.argument('work', type=int, default=25)
@click.argument('rest', type=int, default=5)
@click.argument('cycles', type=int, default=4)
def timer(work, rest, cycles):
    """Start a Pomodoro timer"""
    timer_func(work, rest, cycles)

@script.command("rename")
@click.argument("folder", type=click.Path(exists=True, file_okay=False, path_type=Path))
def rename_sequential(folder: Path):
    """Rename files to sequential format (001, 002, 003...)"""
    rename(str(folder))

@script.command("convert-png")
@click.argument("folder", type=click.Path(exists=True, file_okay=False, path_type=Path))
def convert_png(folder: Path):
    """Convert all non-PNG images to PNG format"""
    convert_to_png(str(folder))

# Main CLI entry point
cli = script

if __name__ == '__main__':
    script()
