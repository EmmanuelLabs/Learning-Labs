# Huawei eNSP Setup (Windows 10 Dual-Boot Environment)
## Overview
This document provides a complete, step-by-step procedure for installing and configuring Huawei eNSP on a Windows 10 dual-boot system.

The setup includes all required dependencies such as `Oracle VM VirtualBox`, `Wireshark`, and `WinPcap` to ensure full compatibility with Huawei simulation environments.
## System Requirements
Minimum requirements for stable operation:
| Component | Requirement
| --------- | ---------
| RAM | ≥ 8 GB
| Storage | ≥ 40 GB free space
| CPU | Virtualization enabled
| OS | Windows 10 (64-bit)
-----------
## Installation Strategy
To ensure compatibility:
- Use specific legacy versions required by eNSP
- Follow strict installation order
- Avoid mixing incompatible modern software versions
## Required Software and Files
#### Core Dependencies
| Software | Version
| -------- | --------
| VirtualBox | 5.2.44
| Wireshark | 3.2.5
| WinPcap | 4.1.3
| eNSP | V100R003C00SPC100
---
#### Optional Device Images
Used for advanced simulations:
- CE (Cloud Engine switches)
- CX series
- NE40E, NE5000E, NE9000 (core routers)
- USG6000V (firewall)

Click [Here](https://mega.nz/folder/WtFwWIZB#swLFgAQA156pSBNLYQNk2g) to obtain the files, i.e,  `core dependencies + optional device images`

## Storage Planning
Due to large file sizes:
- Moved ZIP archives to external USB storage
- Kept only active installations on system drive

## Installation Procedure
### Step 1: VirtualBox Installation
---
Install:
- Oracle VM VirtualBox (v5.2.44)

Steps:
- Run installer as Administrator
- Accept network interface installation
- Ignore temporary network disconnection warnings

Configuration:
- Leave default VM folder as it is
- Ensure Host-Only Network exists
- Install matching Extension Pack
---
### Step 2: Wireshark Installation
---
Install:
- Wireshark (v3.2.5)

Steps:
- Run installer as Administrator
- Install required components (Wireshark, TShark)
- Allow installation of packet capture drivers
---
### Step 3: WinPcap Installation
---
Install:
- WinPcap (v4.1.3)

Purpose:
- Required for eNSP installer detection
- Ensures compatibility with legacy software checks
---
### Step 4: eNSP Installation
---
Install:
- Huawei eNSP

Steps:
- Extract installation files
- Run setup as Administrator
- Ensure all dependencies are detected
- Complete installation
## First Launch Configuration
### Launch eNSP
Verify:
- Application opens without errors
- Workspace and device panel visible
### Register Devices
Navigate:
```
Menu → Tools → Register Device
```
Register:
- AR routers
- Switches (S5700, S3700)
- AC (Access Controller)
- AP devices


## Verification Checklist
| Component | Status
| --- | ---
| VirtualBox installed | ✔
| Wireshark working |✔
| WinPcap detected | ✔
| eNSP launches | ✔
---
## Key Observations
- eNSP requires strict version compatibility
- Legacy dependencies are mandatory
- Storage management is critical for stability
- Installation order directly affects success
## Conclusion
The Huawei eNSP environment has been successfully installed and configured with all required dependencies. 
## Next Steps
- Import additional device images as needed
- Build structured lab exercises
- Begin networking practice aligned with Huawei certification paths
