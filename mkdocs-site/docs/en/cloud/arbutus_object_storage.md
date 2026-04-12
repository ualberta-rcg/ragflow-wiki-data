---
title: "Arbutus object storage/en"
slug: "arbutus_object_storage"
lang: "en"

source_wiki_title: "Arbutus object storage/en"
source_hash: "a02440a0beac92bf09580243bb986710"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:28:37.660119+00:00"

tags:
  - cloud

keywords:
  - "Buckets"
  - "Arbutus OpenStack Dashboard"
  - "Cloud"
  - "Public Access Block"
  - "bucket policies"
  - "ReplicationConfiguration"
  - "Arbutus Object Store"
  - "JSON policy files"
  - "Object Lock"
  - "ObjectTagging"
  - "LifecycleConfiguration"
  - "s3"
  - "Data containers"
  - "Swift"
  - "Bucket"
  - "data containers"
  - "S3-compatible clients"
  - "OpenStack"
  - "Arbutus Object Storage"
  - "Bucket Encryption"
  - "s3cmd"
  - "Object storage"

questions:
  - "What are the primary characteristics and recommended use cases for object storage compared to traditional file storage?"
  - "How is storage capacity allocated to Arbutus projects, and what processes must be followed to request additional space?"
  - "What protocols and client tools can be used to access, manage, and set policies for the Arbutus Object Store?"
  - "How do you make a data container publicly accessible and what URL format is used to read its contents?"
  - "How can users create and apply JSON policy files to manage access controls, such as restricting access by IP address?"
  - "What specific subset of AWS policy actions does Arbutus Object Storage currently support?"
  - "Where can users access the object storage interface within the Arbutus OpenStack Dashboard?"
  - "What alternative term is commonly used in other object storage systems to refer to data containers?"
  - "What specific actions can be performed using the dashboard, and what alternative method exists for creating data containers?"
  - "What specific AWS S3 features and configurations are managed by this list of IAM permissions?"
  - "How do these permissions differentiate between bucket-level management and object-level or version-level tagging?"
  - "What are the security and operational implications of granting the \"Put\" and \"Delete\" actions included in this text?"
  - "What specific S3 permissions are required to manage object lock configurations, legal holds, and retention policies?"
  - "Which API actions are listed for configuring, retrieving, and deleting public access blocks at both the account and bucket levels?"
  - "What are the designated permissions for managing bucket encryption within this cloud category?"
  - "What specific S3 permissions are required to manage object lock configurations, legal holds, and retention policies?"
  - "Which API actions are listed for configuring, retrieving, and deleting public access blocks at both the account and bucket levels?"
  - "What are the designated permissions for managing bucket encryption within this cloud category?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Object storage is a service that manages data as objects. This is different from other storage architectures where data is managed in a file hierarchy. Objects can be created, replaced, or deleted, but unlike traditional storage, they cannot be edited in place. Object storage has become popular due to its ability to handle large files and large numbers of files, and due to the prevalence of compatible tools.

Unlike other storage types, a unit of data or *object* is managed as a whole, and the information within it cannot be modified in place. Objects are stored in containers in the object store. The containers are stored in a way that makes them easier and often faster to access than in a traditional filesystem.

The best use of object storage is to store and export items which do not need hierarchical naming; are accessed mostly as a whole and mostly read-only; and have simplified access-control rules. We recommend using it with software or platforms that are designed to work with data living in an object store.

All Arbutus projects are allocated a default 1TB of object storage. If more is required, you can either request an additional 9TB available through our [Rapid Access Service](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service). More than 10TB must be requested and allocated under the annual [Resource Allocation Competition](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition).

Unlike a cluster computing environment, management of a project's object storage containers is self-service. This includes operations such as [backups](backing_up_your_vm.md) because the object store itself is not backed up. For more information about differences between object storage and other cloud storage types, see [Cloud storage options](cloud_storage_options.md).

We offer access to the OpenStack Object Store via two different protocols: Swift or Amazon Simple Storage Service (S3).

These protocols are very similar and in most situations you can use whichever you like. You don't have to commit to one, as object storage containers and objects created with Swift or S3 can be accessed using both protocols. There are a few key differences in the context of the Arbutus Object Store.

Swift is the default and is simpler since you do not have to manage credentials yourself. Access is governed using your Arbutus account. However, Swift does not replicate all the functionalities of S3. The main use case here is that when you want to manage your object storage containers using access policies, you must use S3, as Swift does not support access policies. You can also create and manage your own keys using S3, which could be useful if you for example want to create a read-only user account for a specific application. See [the OpenStack S3/Swift compatibility list](https://docs.openstack.org/swift/latest/s3_compat.html) for more details.

## Establishing access to your Arbutus Object Store

In order to manage your Arbutus Object Store, you will need your own storage access ID and secret key. To generate these, use the [OpenStack command line client](openstack_command_line_clients.md):

```bash
openstack ec2 credentials create
```

### Accessing your Arbutus Object Store

Setting access policies cannot be done via a web browser but must be done with a [SWIFT or S3-compatible client](arbutus_object_storage_clients.md). There are several ways to access your data containers:

1.  You can use an [S3-compatible client](arbutus_object_storage_clients.md) (e.g. `s3cmd`).
2.  You can use [Globus](../getting-started/globus.md#object-storage-on-arbutus).
3.  If your object storage policies are set to public (not default), you can use a browser via an HTTPS endpoint:

```
https://object-arbutus.alliancecan.ca/PROJECT_ID:DATA_CONTAINER/FILENAME
```

## Managing your Arbutus Object Store

The recommended way to manage buckets and objects in the Arbutus Object Store is by using the `s3cmd` tool, which is available in Linux.
Our documentation provides specific instructions on [configuring and managing access](accessing_object_storage_with_s3cmd.md) with the `s3cmd` client.
We can also use other [S3-compatible clients](arbutus_object_storage_clients.md) that are also compatible with Arbutus Object Store.

In addition, we can perform certain management tasks for our object storage using the [Containers](https://arbutus.cloud.computecanada.ca/project/containers) section under the **Object Store** tab in the [Arbutus OpenStack Dashboard](https://arbutus.cloud.computecanada.ca).

This interface refers to *data containers*, which are also known as *buckets* in other object storage systems.

Using the dashboard, we can create new data containers, upload files, and create directories. Alternatively, we can also create data containers using [S3-compatible clients](arbutus_object_storage_clients.md).

> Please note that data containers are owned by the user who creates them and cannot be manipulated by others.
> Therefore, you are responsible for managing your data containers and their contents within your cloud project.

If you create a new container as **Public**, anyone on the internet can read its contents by simply navigating to

```
https://object-arbutus.alliancecan.ca/<OPENSTACK PROJECT ID>:<YOUR CONTAINER NAME HERE>/<YOUR OBJECT NAME HERE>
```

with your container and object names inserted in place.

To make a data container accessible to the public, we can change its policy to allow public access. This can come in handy if we need to share files to a wider audience. We can manage container policies using JSON files, allowing us to specify various access controls for our containers and objects.

### Managing data container (bucket) policies for your Arbutus Object Store

!!! warning "Attention"
    Be careful with policies because an ill-conceived policy can lock you out of your data container.

Currently, Arbutus Object Storage only supports a [subset](arbutus_object_storage.md#policy-subset) of the AWS specification for [data container policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-iam-policies.html). The following example shows how to create, apply, and view a policy. The first step is to create a policy JSON file:

```json
{
    "Version": "2012-10-17",
    "Id": "S3PolicyId1",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::testbucket",
                "arn:aws:s3:::testbucket/*"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "206.12.0.0/16",
                    "aws:SourceIp": "142.104.0.0/16"
                }
            }
        }
    ]
}
```

This example denies access except from the specified source IP address ranges in Classless Inter-Domain Routing (CIDR) notation. In this example the s3://testbucket is limited to the public IP address range (206.12.0.0/16) used by the Arbutus cloud and the public IP address range (142.104.0.0/16) used by the University of Victoria.

Once you have your policy file, you can implement that policy on the data container:

```bash
s3cmd setpolicy testbucket.policy s3://testbucket
```

To view the policy you can use the following command:

```bash
s3cmd info s3://testbucket
```

### Policy subset

Currently, we support only the following actions:

*   s3:GetObject
*   s3:GetObjectVersion
*   s3:PutObject
*   s3:GetObjectAcl
*   s3:GetObjectVersionAcl
*   s3:PutObjectAcl
*   s3:PutObjectVersionAcl
*   s3:DeleteObject
*   s3:DeleteObjectVersion
*   s3:ListMultipartUploadParts
*   s3:AbortMultipartUpload
*   s3:GetObjectTorrent
*   s3:GetObjectVersionTorrent
*   s3:RestoreObject
*   s3:CreateBucket
*   s3:DeleteBucket
*   s3:ListBucket
*   s3:ListBucketVersions
*   s3:ListAllMyBuckets
*   s3:ListBucketMultipartUploads
*   s3:GetAccelerateConfiguration
*   s3:PutAccelerateConfiguration
*   s3:GetBucketAcl
*   s3:PutBucketAcl
*   s3:GetBucketCORS
*   s3:PutBucketCORS
*   s3:GetBucketVersioning
*   s3:PutBucketVersioning
*   s3:GetBucketRequestPayment
*   s3:PutBucketRequestPayment
*   s3:GetBucketLocation
*   s3:GetBucketPolicy
*   s3:DeleteBucketPolicy
*   s3:PutBucketPolicy
*   s3:GetBucketNotification
*   s3:PutBucketNotification
*   s3:GetBucketLogging
*   s3:PutBucketLogging
*   s3:GetBucketTagging
*   s3:PutBucketTagging
*   s3:GetBucketWebsite
*   s3:PutBucketWebsite
*   s3:DeleteBucketWebsite
*   s3:GetLifecycleConfiguration
*   s3:PutLifecycleConfiguration
*   s3:PutReplicationConfiguration
*   s3:GetReplicationConfiguration
*   s3:DeleteReplicationConfiguration
*   s3:GetObjectTagging
*   s3:PutObjectTagging
*   s3:DeleteObjectTagging
*   s3:GetObjectVersionTagging
*   s3:PutObjectVersionTagging
*   s3:DeleteObjectVersionTagging
*   s3:PutBucketObjectLockConfiguration
*   s3:GetBucketObjectLockConfiguration
*   s3:PutObjectRetention
*   s3:GetObjectRetention
*   s3:PutObjectLegalHold
*   s3:GetObjectLegalHold
*   s3:BypassGovernanceRetention
*   s3:GetBucketPolicyStatus
*   s3:PutPublicAccessBlock
*   s3:GetPublicAccessBlock
*   s3:DeletePublicAccessBlock
*   s3:GetBucketPublicAccessBlock
*   s3:PutBucketPublicAccessBlock
*   s3:DeleteBucketPublicAccessBlock
*   s3:GetBucketEncryption
*   s3:PutBucketEncryption