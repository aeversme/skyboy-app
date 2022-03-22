# Skyboy App

_An application for visualizing FPV quadcopter telemetry data logged by OpenTx/EdgeTx._

![Development screenshot](app/src/images/skyboyapp-feb212022.jpg)

**Roadmap**

* :heavy_check_mark: [Deploy](https://skyboy.app) proof-of-concept with load-balancing and a domain
* :dart: Configure and implement Terraform for AWS infrastructure
* :dart: Add authentication and personal S3 buckets or directories
* :dart: Add S3 upload functionality
* :dart: Add S3 read/retrieve functionality
* :dart: more interesting/better 3D map?
* :dart: Sanity checks/error handling
* :dart: Modify transformations for logs from other receiver/radio combinations

_Development update Mar 18, 2022:_
* Started building Terraform
* VPC resources configured

_Development update Mar 13-14, 2022:_
* Refactored Action to be reusable, which can be triggered from multiple branches
* Created and testedGitHub Action for automatically building and pushing images 

_Development update Mar 3, 2022:_
* Deployed Proof-Of-Concept with custom domain name (skyboy.app) on AWS

_Development update Feb 16-27, 2022:_
* Created Dockerfile and built application Docker image
* Added uploader utility
* Added content to initial application view (prior to uploading data)
* Added basic flight path layer to map
* Started to add map functionality

_Development update Feb 10, 2022:_
* Refactored directory structure
* Added module for transforming data
* Added module for extracting/calculating metrics from dataset

_Development update Feb 8-9, 2022:_
* Added more charts
* Added flight metrics
* Added sidebar
* Added checkboxes to toggle content
* Added Flight Dynamics chart using plotly