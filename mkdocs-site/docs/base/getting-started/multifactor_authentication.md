---
title: "Multifactor authentication/"
slug: "multifactor_authentication"
lang: "base"

source_wiki_title: "Multifactor authentication/"
source_hash: "d41d8cd98f00b204e9800998ecf8427e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:35:18.816614+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

The University of Alberta Research Computing Group (RCG) provides access to the Digital Research Alliance of Canada (the Alliance) national advanced research computing (ARC) infrastructure. To protect your data and the national infrastructure, all users are required to use multifactor authentication (MFA) to log in to the clusters.

## What is multifactor authentication (MFA)?

MFA is a security system that requires more than one method of verification from independent categories of credentials to verify the user's identity for a login or other transaction. For example, if you use your bank card at an ATM, you are combining something you have (the card) with something you know (your PIN).

The Alliance ARC systems use three factors:
*   Something you know (your password).
*   Something you have (a registered authentication device).
*   Something you are (a fingerprint, face ID, etc. - often used to unlock the device you have).

## How to get started with MFA

### 1. Register for an Alliance user account

If you do not have an Alliance user account, please apply for one at the [Alliance CCDB website](https://ccdb.alliancecan.ca). You can view the Alliance guide on how to register for an account [here](https://docs.alliancecan.ca/wiki/Account_Application).

### 2. Choose and register your MFA device

!!! warning "Registering Multiple Devices"
    If you wish to use more than one MFA device, please register them at the same time. If you register a second device after you have already registered a first one, the first one will be erased.
    Contact the RCG or Alliance technical support if you need to register additional devices after your initial setup.

The Alliance supports several methods for MFA. We recommend using a U2F device such as a YubiKey. These devices are available at many electronics retailers. However, a U2F device is not required to use MFA. Other options include:

*   **Software tokens**: Authenticator applications for Android or iOS, such as FreeOTP or Google Authenticator.
*   **Hardware tokens**: U2F (YubiKey, etc.) or OATH-TOTP tokens.

You can register an MFA device using the [Alliance CCDB website](https://ccdb.alliancecan.ca). The Alliance has a detailed guide on how to set up MFA for your account [here](https://docs.alliancecan.ca/wiki/Multi-Factor_Authentication).

### 3. Log in to a cluster with MFA

After you have registered your MFA device, you can log in to a cluster.

If you are using an authenticator application or an OATH-TOTP token, you will be prompted to enter a six-digit code after you enter your password.

```bash
ssh <username>@vulcan.computecanada.ca
```

```bash
ssh <username>@vulcan.computecanada.ca
Password: <your_password>
MFA Passcode: <6_digit_code>
```

If you are using a U2F device, you will be prompted to touch the device after you enter your password.

```bash
ssh <username>@vulcan.computecanada.ca
```

```bash
ssh <username>@vulcan.computecanada.ca
Password: <your_password>
Using U2F device to verify, please touch the button on the device.
```

If you have any issues with MFA or logging in, please contact the RCG or Alliance technical support.