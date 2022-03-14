# Skyboy App

An application for visualizing FPV quadcopter telemetry data logged by OpenTx/EdgeTx.

**Roadmap**

* :heavy_check_mark: [Deploy](https://skyboy.app) proof-of-concept with load-balancing and a domain
* :dart: Choose and implement Infrastructure as Code solution
* :dart: Add authentication and personal S3 buckets or directories
* :dart: Add S3 upload functionality
* :dart: Add S3 read/retrieve functionality
* :dart: more interesting/better 3D map?
* :dart: Sanity checks/error handling
* :dart: Modify transformations for logs from other receiver/radio combinations

_Development update Mar 13, 2022:_

* GitHub Action for automatically building and pushing images created and tested

_Development update Mar 3, 2022:_

* Proof-of-concept deployed with custom domain name (skyboy.app) on AWS

_Development update Feb 27, 2022:_

* Created Dockerfile and built application Docker image

_Development update Feb 21, 2022:_

* Added uploader utility
* Added content to initial application view (prior to uploading data)

![Development screenshot](app/src/images/skyboyapp-feb212022.jpg)

_Development update Feb 18, 2022:_

* Added basic flight path layer to map

_Development update Feb 16, 2022:_

* Started to add map functionality

_Development update Feb 10, 2022:_

* Refactored directory structure
* Added module for transforming data
* Added module for extracting/calculating metrics from dataset

_Development update Feb 9, 2022:_

* Added more charts
* Added flight metrics

_Development update Feb 8, 2022:_

* Added sidebar
* Added checkboxes to toggle content
* Added Flight Dynamics chart using plotly