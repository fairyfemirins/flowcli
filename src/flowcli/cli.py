#!/usr/bin/env python3
"""
flowcli: Build AI workflows in your terminal.
Local-first, code-driven, and self-hostable.
"""

import click
import yaml
from rich.console import Console
from rich.progress import Progress

console = Console()

@click.group()
def cli():
    """Build and run AI workflows from your terminal."""
    pass

@cli.command()
def init():
    """Initialize a new AI workflow project."""
    console.print("[bold green]Creating new workflow project...[/bold green]")
    workflow = {
        "name": "my_workflow",
        "steps": [
            {
                "name": "prompt",
                "type": "llm",
                "model": "llama3",
                "prompt": "Summarize this document: {{input}}"
            }
        ]
    }
    with open("workflow.yaml", "w") as f:
        yaml.dump(workflow, f)
    console.print("[bold green]Created workflow.yaml[/bold green]")

@cli.command()
@click.argument("workflow_file", type=click.Path(exists=True))
def run(workflow_file):
    """Run an AI workflow from a YAML file."""
    console.print(f"[bold blue]Running workflow: {workflow_file}[/bold blue]")
    with open(workflow_file, "r") as f:
        workflow = yaml.safe_load(f)
    console.print(f"[bold]Workflow: {workflow['name']}[/bold]")
    for step in workflow["steps"]:
        console.print(f"[cyan]Step: {step['name']} (Type: {step['type']})[/cyan]")

if __name__ == "__main__":
    cli()