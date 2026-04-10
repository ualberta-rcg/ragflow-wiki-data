---
title: "Accessing the Arbutus object storage with AWS CLI"
tags:
  - cloud

keywords:
  - AWS Command Line Interface
  - object storage clients
  - sync command
  - Arbutus object storage
  - credentials
---

This page contains instructions on how to set up and access [Arbutus object storage](arbutus-object-storage.md) with the AWS Command Line Interface (CLI), one of the [object storage clients](arbutus_object_storage_clients.md) available for this storage type.

Compared to other object storage clients, AWS CLI has better support for large (>5GB) files and the helpful `sync` command. However, not all features have not been tested.

== Installing AWS CLI == 

<pre>
pip install awscli awscli-plugin-endpoint
</pre>

== Configuring AWS CLI == 

Generate an access key ID and secret key

<pre>
openstack ec2 credentials create
</pre>

Edit or create `~/.aws/credentials` and add the credentials generated above

<pre>
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
</pre>

Edit `~/.aws/config` and add the following configuration

<pre>
[plugins]
endpoint = awscli_plugin_endpoint

[profile default]
s3 =
  endpoint_url = https://object-arbutus.alliancecan.ca
  signature_version = s3v4
s3api =
  endpoint_url = https://object-arbutus.alliancecan.ca
</pre>

== Using AWS CLI == 

<pre>
export AWS_PROFILE=default
aws s3 ls <container-name>
aws s3 sync local_directory s3://container-name/prefix
</pre>

More examples of using the AWS CLI can be found on [this external site. ](https://docs.ovh.com/us/en/storage/getting_started_with_the_swift_S3_API/)