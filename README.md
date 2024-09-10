# Python Package Template

This repository provides a basic template for creating a Python package.

The repository also contains a Azure DevOps Pipeline (`azure-pipelines.yml`) that pushes this package to an Azure Artifacts-Feed (AAF). An AAF is a place to store, manage and share (python) packages.

I use `twine` to publish the package to the AAF. For this, `twine`must be provided with the feed URL, the name and the access token. Currently, these three values are provided as secret variables in the Azure DevOps Pipeline. 