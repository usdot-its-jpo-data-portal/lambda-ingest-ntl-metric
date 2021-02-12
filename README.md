# Summary

This repository contains a lambda function for ingesting usage metrics relating to ITS DataHub's assets on National Transportation Library. The metrics are ingested into ITS DataHub's Elasticsearch database for display on ITS DataHub.

# README Outline:
* Project Description
* Prerequisites
* Usage
	* Building
	* Testing
* Version History and Retention
* License
* Contributions
* Contact Information
* Acknowledgements

# Project Description

This repository contains a lambda function for ingesting usage metrics relating to ITS DataHub's assets on National Transportation Library. The metrics CSVs are deposited into an S3 bucket and these CSVs are then ingested into ITS DataHub's Elasticsearch database for display on ITS DataHub.

# Prerequisites

Requires:
- Python 3.6+
- Elasticsearch (optional if you choose to write metrics to CSV)
- AWS S3

# Usage

## Building
 
Option 1: Build package locally and deploy to lambda manually through AWS console.
```
sh package.sh
```

## Testing
Run
```
python src/lambda_function.py
```

# Version History and Retention

**Status:** This project is in the prototype phase.

**Release Frequency:** This project is currently in development and updated weekly.

**Release History: See [CHANGELOG.md](CHANGELOG.md)**

**Retention:** This project will remain publicly accessible for a minimum of five years (until at least 06/15/2025).

# License

This project is licensed under the Creative Commons 1.0 Universal (CC0 1.0) License - see the [LICENSE](https://github.com/usdot-jpo-codehub/codehub-readme-template/blob/master/LICENSE) for more details. 

# Contributions
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our Code of Conduct, the process for submitting pull requests to us, and how contributions will be released.

# Contact Information

Contact Name: ITS JPO
Contact Information: data.itsjpo@dot.gov

# Acknowledgements

## Citing this code

When you copy or adapt from this code, please include the original URL you copied the source code from and date of retrieval as a comment in your code. Additional information on how to cite can be found in the [ITS CodeHub FAQ](https://its.dot.gov/code/#/faqs).

## Contributors
Shout out to [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) for their README template.
