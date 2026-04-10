---
title: "Accessing the Arbutus object storage with AWS CLI"
slug: "accessing_the_arbutus_object_storage_with_aws_cli"
lang: "base"

source_wiki_title: "Accessing the Arbutus object storage with AWS CLI"
source_hash: "fdcf8e011088111a084c64d7eed4942f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:50:48.292504+00:00"

tags:
  - cloud

keywords:
  - "AWS Command Line Interface"
  - "object storage clients"
  - "sync command"
  - "Arbutus object storage"
  - "credentials"

questions:
  - "What are the main advantages of using the AWS CLI for Arbutus object storage compared to other available clients?"
  - "What specific steps and file modifications are required to properly configure the AWS CLI with your access credentials and endpoint URLs?"
  - "How do you execute basic operations, such as listing container contents and syncing local directories, using the AWS CLI?"
  - "What are the main advantages of using the AWS CLI for Arbutus object storage compared to other available clients?"
  - "What specific steps and file modifications are required to properly configure the AWS CLI with your access credentials and endpoint URLs?"
  - "How do you execute basic operations, such as listing container contents and syncing local directories, using the AWS CLI?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

This page contains instructions on how to set up and access [Arbutus object storage](arbutus-object-storage.md) with the AWS Command Line Interface (CLI), one of the [object storage clients](arbutus-object-storage-clients.md) available for this storage type.

!!! note
    Compared to other object storage clients, AWS CLI has better support for large (>5GB) files and the helpful `sync` command. However, not all features have been tested.

## Installing AWS CLI

```bash
pip install awscli awscli-plugin-endpoint
```

## Configuring AWS CLI

Generate an access key ID and secret key:

```bash
openstack ec2 credentials create
```

Edit or create `~/.aws/credentials` and add the credentials generated above:

```ini title="~/.aws/credentials"
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
```

Edit `~/.aws/config` and add the following configuration:

```ini title="~/.aws/config"
[plugins]
endpoint = awscli_plugin_endpoint

[profile default]
s3 =
  endpoint_url = https://object-arbutus.alliancecan.ca
  signature_version = s3v4
s3api =
  endpoint_url = https://object-arbutus.alliancecan.ca
```

## Using AWS CLI

```bash
export AWS_PROFILE=default
aws s3 ls <container-name>
aws s3 sync local_directory s3://container-name/prefix
```

More examples of using the AWS CLI can be found on [this external site](https://docs.ovh.com/us/en/storage/getting_started_with_the_swift_S3_API/).