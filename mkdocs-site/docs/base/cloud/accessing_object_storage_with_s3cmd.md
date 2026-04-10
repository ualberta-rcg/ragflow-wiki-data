---
title: "Accessing object storage with s3cmd"
slug: "accessing_object_storage_with_s3cmd"
lang: "base"

source_wiki_title: "Accessing object storage with s3cmd"
source_hash: "2b57da3ce9af32a0cba32f3686d20059"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:39:46.016894+00:00"

tags:
  - cloud

keywords:
  - "Arbutus object storage"
  - "configuration"
  - "bucket status"
  - "upload files"
  - "object storage clients"
  - "ACL"
  - "info command"
  - "BUCKET_NAME"
  - "Access control lists (ACLs)"
  - "buckets"
  - "bucket"
  - "s3cmd"
  - "object storage"

questions:
  - "How do you install the s3cmd tool on various Linux distributions?"
  - "What specific endpoint and credentials need to be provided during the s3cmd configuration process?"
  - "What are the naming requirements for creating a new bucket, and which commands are used to create and inspect it?"
  - "How do you upload a file to a bucket and automatically determine its MIME type using s3cmd?"
  - "What command is used to delete a specific file from a bucket?"
  - "How can you modify the Access Control Lists (ACLs) to change a bucket's visibility to public or private?"
  - "What command line tool and specific command are used to check the status of a bucket?"
  - "What is the exact syntax required to execute the info command for a given bucket name?"
  - "What specific configuration details and access control information are included in the output of the info command?"
  - "How do you upload a file to a bucket and automatically determine its MIME type using s3cmd?"
  - "What command is used to delete a specific file from a bucket?"
  - "How can you modify the Access Control Lists (ACLs) to change a bucket's visibility to public or private?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
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
```console
Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.

Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key []: 20_DIGIT_ACCESS_KEY
Secret Key []: 40_DIGIT_SECRET_KEY
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

This should produce an s3cmd configuration file as in the example below. You are also free to explore additional s3cmd configuration options to fit your use case. Note that in the example the keys are redacted and you will need to replace them with your provided key values:

```ini
[default]
access_key = <redacted>
check_ssl_certificate = True
check_ssl_hostname = True
host_base = object-arbutus.alliancecan.ca
host_bucket = object-arbutus.alliancecan.ca
secret_key = <redacted>
use_https = True
```

## Create buckets
The next task is to make a bucket. Buckets contain files. Bucket names must be unique across the Arbutus object storage solution. Therefore, you will need to create a uniquely named bucket which will not conflict with other users. For example, buckets `s3://test/` and `s3://data/` are likely already taken. Consider creating buckets reflective of your project, for example `s3://def-test-bucket1` or `s3://atlas_project_bucket`. Valid bucket names may only use the uppercase characters, lowercase characters, digits, period, hyphen, and underscore (i.e. A-Z, a-z, 0-9, ., -, and _ ).

To create a bucket, use the tool's `mb` (make bucket) command:

```bash
s3cmd mb s3://BUCKET_NAME/
```

To see the status of a bucket, use the `info` command:

```bash
s3cmd info s3://BUCKET_NAME/
```

The output will look something like this:

```console
s3://BUCKET_NAME/ (bucket):
   Location:  default
   Payer:     BucketOwner
   Expiration Rule: none
   Policy:    none
   CORS:      none
   ACL:       *anon*: READ
   ACL:       USER: FULL_CONTROL
   URL:       http://object-arbutus.alliancecan.ca/BUCKET_NAME/
```

## Upload files
To upload a file to the bucket, use the `put` command similar to this:

```bash
s3cmd put --guess-mime-type FILE_NAME.dat s3://BUCKET_NAME/FILE_NAME.dat
```

where the bucket name and the file name are specified. Multipurpose Internet Mail Extensions (MIME) is a mechanism for handling files based on their type. The `--guess-mime-type` command parameter will guess the MIME type based on the file extension. The default MIME type is `binary/octet-stream`.

## Delete files
To delete a file from the bucket, use the `rm` command similar to this:
```bash
s3cmd rm s3://BUCKET_NAME/FILE_NAME.dat
```

## Access Control Lists (ACLs) and Policies
Buckets can have ACLs and policies which govern who can access what resources in the object store. These features are quite sophisticated. Here are two simple examples of using ACLs using the tool's `setacl` command.

```bash
s3cmd setacl --acl-public -r s3://BUCKET_NAME/
```

The result of this command is that the public can access the bucket and recursively (-r) every file in the bucket. Files can be accessed via URLs such as
`https://object-arbutus.alliancecan.ca/PROJECT_ID:BUCKET_NAME/FILE_NAME.dat`

The second ACL example limits access to the bucket to only the owner:

```bash
s3cmd setacl --acl-private s3://BUCKET_NAME/
```

The current configuration of a bucket can be viewed via the command:

```bash
s3cmd info s3://testbucket
```

Other more sophisticated examples can be found in the s3cmd [help site](https://www.s3express.com/help/help.html) or s3cmd(1) man page.

Instructions on [managing bucket policies](arbutus-object-storage.md#managing-data-container-bucket-policies-for-your-arbutus-object-store) for your object store, including examples using s3cmd are available on the main [object storage](arbutus-object-storage.md) page.