---
title: "Accessing object storage with s3cmd/en"
slug: "accessing_object_storage_with_s3cmd"
lang: "en"

source_wiki_title: "Accessing object storage with s3cmd/en"
source_hash: "957a4dd3fa2987bb2b59af9ee4ec4cd0"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:49:59.502867+00:00"

tags:
  - cloud

keywords:
  - "s3cmd"
  - "bucket name"
  - "buckets"
  - "delete files"
  - "configuration"
  - "upload files"
  - "--guess-mime-type"
  - "MIME type"
  - "bucket policies"
  - "Arbutus object storage"
  - "Access control lists (ACLs)"
  - "put command"

questions:
  - "How do you install and configure the s3cmd tool to connect to Arbutus object storage?"
  - "What are the naming rules and specific commands required to create and check the status of a new bucket?"
  - "How do you upload a file to a bucket and automatically determine its MIME type using s3cmd?"
  - "How do you delete a specific file from a bucket using the s3cmd command?"
  - "What commands are used to modify a bucket's Access Control List (ACL) to make its contents either publicly accessible or restricted to the owner?"
  - "How can a user view the current configuration of a bucket and where can they find more advanced instructions on managing bucket policies?"
  - "What is the correct syntax for using the s3cmd put command to upload a file to a specific bucket?"
  - "How does the --guess-mime-type parameter determine the appropriate file type during an upload?"
  - "What is the default MIME type assigned to a file if the system cannot determine its specific type?"
  - "How do you delete a specific file from a bucket using the s3cmd command?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

This page contains instructions on how to set up and access [Arbutus object storage](arbutus-object-storage.md) with s3cmd, one of the [object storage clients](arbutus-object-storage-clients.md) available for this storage type.

## Installing s3cmd
Depending on your Linux distribution, the `s3cmd` command can be installed using the appropriate `yum` (RHEL, CentOS) or `apt` (Debian, Ubuntu) command:

```bash
sudo yum install s3cmd
```

```bash
sudo apt install s3cmd
```

## Configuring s3cmd

To configure the `s3cmd` tool, use the command:
```bash
s3cmd --configure
```

And make the following configurations with the keys provided or created with the `openstack ec2 credentials create` command:

```
Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.

Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key []: <20_DIGIT_ACCESS_KEY>
Secret Key []: <40_DIGIT_SECRET_KEY>
Default Region [US]: 

Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint []: object-arbutus.alliancecan.ca

Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used
if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket []: object-arbutus.alliancecan.ca

Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password []:
Path to GPG program [/usr/bin/gpg]: 

When using secure HTTPS protocol all communication with Amazon S3
servers is protected from 3rd party eavesdropping. This method is
slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol []: Yes

On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name:
```

This should produce a s3cmd configuration file as in the example below. You are also free to explore additional s3cmd configuration options to fit your use case. Note that in the example the keys are redacted and you will need to replace them with your provided key values:

```ini
[default]
access_key = <REDACTED>
check_ssl_certificate = True
check_ssl_hostname = True
host_base = object-arbutus.alliancecan.ca
host_bucket = object-arbutus.alliancecan.ca
secret_key = <REDACTED>
use_https = True
```

## Create buckets
The next task is to make a bucket. Buckets contain files. Bucket names must be unique across the Arbutus object storage solution. Therefore, you will need to create a uniquely named bucket which will not conflict with other users. For example, buckets `s3://test/` and `s3://data/` are likely already taken. Consider creating buckets reflective of your project, for example `s3://def-test-bucket1` or `s3://atlas_project_bucket`. Valid bucket names may only use the upper case characters, lower case characters, digits, period, hyphen, and underscore (i.e. A-Z, a-z, 0-9, ., -, and _ ).

To create a bucket, use the tool's `mb` (make bucket) command:

```bash
s3cmd mb s3://<BUCKET_NAME>/
```

To see the status of a bucket, use the `info` command:

```bash
s3cmd info s3://<BUCKET_NAME>/
```

The output will look something like this:

```
s3://<BUCKET_NAME>/ (bucket):
   Location:  default
   Payer:     BucketOwner
   Expiration Rule: none
   Policy:    none
   CORS:      none
   ACL:       *anon*: READ
   ACL:       USER: FULL_CONTROL
   URL:       http://object-arbutus.alliancecan.ca/<BUCKET_NAME>/
```

## Upload files
To upload a file to the bucket, use the `put` command similar to this:

```bash
s3cmd put --guess-mime-type <FILE_NAME.dat> s3://<BUCKET_NAME>/<FILE_NAME.dat>
```

where the bucket name and the file name are specified. Multipurpose Internet Mail Extensions (MIME) is a mechanism for handling files based on their type. The `--guess-mime-type` command parameter will guess the MIME type based on the file extension. The default MIME type is `binary/octet-stream`.

## Delete files
To delete a file from the bucket, use the `rm` command similar to this:
```bash
s3cmd rm s3://<BUCKET_NAME>/<FILE_NAME.dat>
```

## Access control lists (ACLs) and policies
Buckets can have ACLs and policies which govern who can access what resources in the object store. These features are quite sophisticated. Here are two simple examples of using ACLs using the tool's `setacl` command.

```bash
s3cmd setacl --acl-public -r s3://<BUCKET_NAME>/
```

The result of this command is that the public can access the bucket and recursively (-r) every file in the bucket. Files can be accessed via URLs such as
`https://object-arbutus.alliancecan.ca/<PROJECT_ID>:<BUCKET_NAME>/<FILE_NAME.dat>`

The second ACL example limits access to the bucket to only the owner:

```bash
s3cmd setacl --acl-private s3://<BUCKET_NAME>/
```

The current configuration of a bucket can be viewed via the command:

```bash
s3cmd info s3://<BUCKET_NAME>
```

Other more sophisticated examples can be found in the s3cmd [help site](https://www.s3express.com/help/help.html) or s3cmd(1) man page.

Instructions on [managing bucket policies](arbutus-object-storage.md#managing-data-container-bucket-policies-for-your-arbutus-object-store) for your object store, including examples using s3cmd are available on the main [object storage](arbutus-object-storage.md) page.