# Windows Dual Boot Setup (Windows 11 + Windows 10)
## Overview
This document describes the complete setup of a dual-boot environment on a Dell Latitude 7400, enabling both Windows 11 and Windows 10 to coexist on the same system.

This setup was required to support legacy networking tools such as Huawei eNSP, which depend on older virtualization environments incompatible with modern systems.
## Objective
- Maintain a stable modern environment (Windows 11)
- Create a separate legacy-compatible environment (Windows 10)
- Avoid conflicts between software dependencies (e.g., VirtualBox versions)
- Enable structured networking lab development
## System Specifications
- Device: Dell Latitude 7400
- RAM: 16 GB (10.6 GB usable)
- Storage: 237 GB total (~153 GB free before setup)
- CPU: 4 cores / 8 logical processors
- Boot Mode: UEFI
- Secure Boot: Enabled
## Key Design Decision
#### Problem
Huawei eNSP requires:
- Older Oracle VM VirtualBox (5.x)
While the system already uses:
- Modern VirtualBox (7.x) for Fedora VM
#### Solution
Instead of:
- downgrading VirtualBox
- running nested virtual machines (VM inside VM inside VM)
A dual-boot strategy was selected:
```Plain text
Windows 11 → Modern tools (Fedora VM, Python, etc.)
Windows 10 → Legacy tools (eNSP environment)
```
## Disk Preparation
### Step 1 — Open Disk Management
Accessed via:
```Plain text
Windows + X → Disk Management
```
### Step 2 — Shrink Existing Partition
- Target: C: (Windows 11 partition)
- Action: Shrink Volume
### Step 3 — Allocate Space
- Shrunk: ~85 GB
- Result:
```Plain text
Unallocated Space (85 GB)
```
#### Important Constraint
- No formatting
- No partition creation
- Space left as unallocated for Windows installer
## Bootable USB Creation
#### Tools Used
- Rufus
- Windows 10 ISO (official Microsoft source)
#### USB Specifications
- Size: 128 GB
- Status: Empty
#### Rufus Configuration
---
| Setting | Value | Reason
| ------- | ------- | -------
| Image Option | Standard Windows installation | Reqired for OS install
| Partition Scheme | GPT | Required for UEFI systems
| Target system | UEFI (non-CSM) | Modern boot mode
| File system | NTFS | Supports files > 4GB
| Volume label | Default (ESD-ISO) | Not critical
| Cluster size | Default | Automatically optimized
---

#### Secure Boot Adjustment
Rufus detected a revoked UEFI bootloader.

Action:
```Plain text
Applied Rufus bootloader fix
```
---
### Additional Installation Customizations
---
#### Enabled:
✔ Create local account

✔ Set regional settings automatically

✔ Disable data collection

✔ Disable BitLocker auto encryption
## Boot Process
### Step 1 — Enter Boot Menu
On restart:
```Plain text
F12 (Dell Boot Menu)
```
### Step 2 — Select USB
Due to naming convention, USB appeared as:
```Plain text
UEFI: VendorCoproductCode 2.00, Partition 1
```
Selected:
```Plain text
Partition 1 (bootable)
```
## Windows Installation
### Step 1 — Initial Setup
- Language: English (UK)
- Time/Region: UK
- Keyboard: UK
### Step 2 — Installation Type
Selected:
```Plain text
Custom: Install Windows only (advanced)
```
#### Reason:
- Prevents overwriting Windows 11
- Allows manual partition selection
### Step 3 — Partition Selection
Selected:
```Plain text
Drive 0 Unallocated Space (85 GB)
```
#### Critical Constraint
Did NOT:
- delete any partitions
- format existing drives
- modify EFI or recovery partitions
### Step 4 — Installation Execution
Windows automatically:
- created required partitions
- installed OS in allocated space
### Step 5 — USB Removal Timing
USB removed:
```Plain text
after system restart (black screen)
```
## Outcome
- Windows 10 successfully installed
- Windows 11 preserved
- Dual boot environment operational
## Resulting System Architecture
System Boot Menu:
- Windows 10 (legacy environment)
- Windows 11 (primary environment)
## Validation
Successful setup confirmed by:
- Boot menu displays both OS options
- Both systems boot independently
- No data loss on Windows 11
- Stable operation in Windows 10
## Role in Networking Workflow
This dual boot setup serves as the foundation for:
- Legacy virtualization environments
- Installation of eNSP ecosystem
- Controlled experimentation without affecting primary OS
## Next Steps
- Install legacy Oracle VM VirtualBox (5.x) on Windows 10
- Install supporting tools (WinPcap, Wireshark)
- Install and configure Huawei eNSP
