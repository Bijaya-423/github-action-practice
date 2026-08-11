on: -> Defines when the GitHub Actions workflow should run.

In your workflow:

on:
  push:

means the workflow runs whenever code is pushed to the repository.

jobs:

Defines the jobs that GitHub Actions needs to execute.

Example:

jobs:
  greet:

Here, the workflow has one job called greet.

runs-on: -> Specifies the operating system/runner environment where the job will execute.

runs-on: ubuntu-latest

means the greet job runs on the latest available Ubuntu GitHub-hosted runner.

steps: -> Defines the individual tasks performed inside a job.

steps:
  - name: Checkout code
    ...
  - name: Print greeting
    ...

Your greet job has two steps.

uses: -> Uses an existing GitHub Action instead of writing the functionality yourself.

uses: actions/checkout@v4

This uses the official actions/checkout action to check out your repository's code.

run: -> Executes a shell command on the GitHub Actions runner.

run: echo "Hello from GitHub Actions!"

This executes the echo command and prints:

Hello from GitHub Actions!
name: on a step

Gives a step a human-readable name.

For example:

- name: Checkout code

and:

- name: Print greeting

These names appear in the Actions tab and job logs, making it easy to understand what each step is doing.

Quick Notes
Key	Purpose
on:	When the workflow runs
jobs:	What jobs the workflow contains
runs-on:	Where the job runs
steps:	Tasks performed by the job
uses:	Use an existing GitHub Action
run:	Execute a shell command
name:	Give a workflow/job/step a readable name
Easy way to remember
on       → WHEN?
jobs     → WHAT JOB?
runs-on  → WHERE?
steps    → WHAT TASKS?
uses     → USE WHICH ACTION?
run      → RUN WHICH COMMAND?
name     → WHAT SHOULD IT BE CALLED?
