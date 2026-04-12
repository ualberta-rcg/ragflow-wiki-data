---
title: "GIS/en"
slug: "gis"
lang: "en"

source_wiki_title: "GIS/en"
source_hash: "16e146b19fe840fe86ba6235f61f6759"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:20:27.826614+00:00"

tags:
  []

keywords:
  - "GIS"
  - "ArcGIS"
  - "software"
  - "geographic information system"
  - "clusters"

questions:
  - "What specific GIS software titles are currently available for use on the clusters?"
  - "How should users go about finding and installing GIS packages for programming languages like R and Python?"
  - "Why is ArcGIS not supported on the clusters, and what alternative options are recommended for users who need it?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

GIS is an acronym for a [geographic information system](https://en.wikipedia.org/wiki/Geographic_information_system).

For a brief overview of GIS software, see [here](https://datacarpentry.org/organization-geospatial/04-geo-landscape.html).
Of the titles mentioned in that overview, the following are available on our clusters:
* QGIS
* GRASS
* [GDAL](gdal.md)
* SAGA
You may find others by checking the list of [available software](available-software.md) and looking for entries with type "geo".
GIS packages for R and Python will not appear there; please see [R](r.md) and [Python](python.md) for more about finding and installing packages for those languages.

We are frequently asked about ArcGIS, which is commercial software.

!!! warning "ArcGIS Support"
    Due to the cost, licensing restrictions, and complexity of its configuration, we do not support ArcGIS on our clusters.
    We recommend you contact your institution's IT services department or the vendor [Esri](https://www.esri.com) to see what options are available for you, either on your personal computer, at your institution, or through a commercial cloud provider like [AWS](https://aws.amazon.com/?nc1=h_ls) or [Azure](https://azure.microsoft.com/en-ca/).