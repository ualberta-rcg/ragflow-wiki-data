---
title: "NCCL"
tags:
  []

keywords:
  []
---

= What is NCCL =
Please see the [NVIDIA webpage](https://developer.nvidia.com/nccl).

= Troubleshooting =
To activate NCCL debug outputs, set the following variable before running NCCL:
 NCCL_DEBUG=info

To fix `Caught error during NCCL init [...] connect() timed out` errors, set the following variable before running NCCL:
 export NCCL_BLOCKING_WAIT=1