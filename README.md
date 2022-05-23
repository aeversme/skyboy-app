# Skyboy App

_An application for visualizing FPV quadcopter telemetry data logged by OpenTx/EdgeTx._

![Development screenshot](app/src/images/skyboyapp-feb212022.jpg)

**Roadmap**

* :heavy_check_mark: [Deploy](https://skyboy.app) proof-of-concept with load-balancing and a domain
* :heavy_check_mark: Configure and implement Terraform for AWS infrastructure
* :heavy_check_mark: Add an application Demo mode
* :heavy_check_mark: Add Datadog monitoring of ECS Fargate deployment
* :construction: Modify transformations for logs from other receiver/radio/flight controller combinations
* :dart: Add authentication and personal S3 buckets or directories
* :dart: Add S3 upload functionality
* :dart: Add S3 read/retrieve functionality
* :dart: more interesting/better 3D map?
* :dart: Sanity checks/error handling
* :dart: Testing

_Development updates May 2022:_
* Configured auto-scaling policies and container health checks
* Deployed Datadog Agent container to monitor service metrics
* Added a Demo button to allow users to preview the application

_Development updates April 2022:_
* Deployed infrastructure as code with branch-dependent Actions workflow
* Added ability for user to demo the app using a sample telemetry log

_Development update March 2022:_
* Created modular Terraform code for defining infrastructure
* Refactored Action to be reusable, which can be triggered from multiple branches
* Created and tested GitHub Action for automatically building and pushing images 
* Deployed Proof-Of-Concept with custom domain name (skyboy.app) on AWS

_Development updates February 2022:_
* Created Dockerfile and built application Docker image
* Added uploader utility (local memory storage only)
* Added content to initial application view (prior to uploading data)
* Added Mapbox map and basic flight path layer
* Added Python module for transforming data
* Added Python module for extracting/calculating metrics from dataset
* Added flight metrics
* Added checkboxes in sidebar to toggle content
* Added charts using plotly