---
title: "Access to files of users leaving a project"
slug: "access_to_files_of_users_leaving_a_project"
lang: "base"

source_wiki_title: "Access to files of users leaving a project"
source_hash: "83ff569eb08ac09330a4622085d23e40"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:35:30.721500+00:00"

tags:
  []

keywords:
  - "storage access policy"
  - "data transfer"
  - "account deactivation"
  - "Principal Investigators"
  - "sponsored users"

questions:
  - "Why might a Principal Investigator lose access to a departing sponsored user's files upon account deactivation?"
  - "What is the simplest method to prevent data access issues before a group member leaves?"
  - "What specific data management actions should be taken while a departing user's account is still active?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is primarily directed at Principal Investigators who have sponsored users.

!!! warning "Account Deactivation and File Access"
    During annual renewals, you may indicate that some of your sponsored users will **not be continuing** as a part of your research team. **This may lead to the deactivation of their accounts**, which may in turn restrict your ability to access their files. Because intellectual property rules vary depending on the situation, we do not automatically assume that you the sponsor are allowed to access files owned or produced by group members, even in contexts where you may exercise control over a filesystem quota.

Just as group members who quit are expected to return their office keys after having cleaned out their office, it’s logical to expect similar behaviour concerning data stored in their account on a cluster. These data should be transferred to another member of the research group so that they can be sorted and either deleted (freeing up valuable space) or kept for later use.

!!! tip "Preventing Data Access Issues"
    It is therefore important to make arrangements with a group member *before* their account is deactivated, to mitigate the risk of them becoming incommunicado in subsequent months.

    The easiest way to avoid any problem is that your group members **agree** to the **storage access policy** in their [CCDB](https://ccdb.alliancecan.ca) account under My Account/Agreements tab.

!!! tip "Actions to Take While an Account is Active"
    Here are some actions you should take while the departing user's account is still active:

    *   If they own many files, ask the user to compress them first with `tar, zip`, or some other such tool. For help with archiving data, see [Handling large collections of files](handling-large-collections-of-files.md). For directory access permissions, see the [Sharing data](sharing-data.md) wiki page and its parent page [Storage and file management](storage-and-file-management.md). For further assistance, contact [technical support](technical-support.md).
    *   Ask the user to identify any data that should be archived and copy them to a portable USB drive, an external hard drive you may have in your lab, or to your own account on an Alliance system. Lots of copies keep stuff safe!
    *   On the other hand, storage is limited and can be expensive, so once any important data have been secured, ask the user to delete everything that can reasonably be deleted.
    *   If there is anything you have good reason to keep on Alliance storage systems, move it from the user's account to your own before this person leaves. If the person becomes incommunicado, intellectual property rules may delay or even forbid us from moving data from this account to your own. IP rules vary from institution to institution, so it would be wise to familiarize yourself with those rules for your own sake.

The [Alliance policy](https://alliancecan.ca/en/services/advanced-research-computing/account-management/policies) regarding Terms of Use states that files associated with expired accounts may be removed after one year. [Contact us](technical-support.md) to know if these data have been migrated to tape.