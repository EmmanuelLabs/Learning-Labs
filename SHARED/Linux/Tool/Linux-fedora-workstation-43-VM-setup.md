# VIRTUALBOX + FEDORA 43 SETUP
## Tool Name
- Oracle VM Virtualbox
- Fedora Workstation 43
## Overview
This setup documents the process of installing Fedora 43 on virtualbox under windows 11, including multiple failed attempts and the final working configuration.

The objective was to create a stable Linux virtual environment for learning and development. The process exposed critical conflicts between virtualbox and windows virtualization layers, requiring deep system-level intervention.
## System Requirements
- Host OS: Windows 11
- CPU: Intel (VT-x supported)
- RAM: 16GB (8GB allocated to VM)
- Storage: ≥ 40GB free
- BIOS/UEFI: Virtualization (VT-x/VT-d) enabled
## Installation
### Software
- Virtualbox (final working version: 7.2.6)
- Virtualbox Extension Pack (must be of same version)
- Fedora Workstation 43 ISO
### Initial Setup
- VM created in Expert Mode
- Base directory: `C:\Dev\VMs`
- Disk: 40GB dynamically allocated VDI
## Configuration (Final stable settings)
### System
- RAM: 8192 MB
- CPUs: 4 cores
- PAE/NX: Enabled
- Chipset: ICH9
- EFI: Disabled (final stable config used BIOS mode)
### Display
- Graphics controller: VMSVGA
- Video Memory: 128 MB
- 3D Acceleration: Disabled (critical for stability)
### Storage
- Controller: SATA
- Fedora ISO attached to SATA (not IDE)
- VDI attached to SATA
### Network
- NAT (Default)
## Step-by-Step Setup Process
### Attempt Phase
- Initial installs failed with: `systemd[1]: Freezing execution` and `failed to start display manager`
- Misleading indicator: `supported iso: no` (non-fatal)
### Configuration Fixes
Switched:
- PIIX3 → ICH9
- BIOS → UEFI (temporarily, later reverted)

Moved ISO from IDE to SATA

Enabled proper CPU + RAM allocation

RESULT: GRUB loaded, but system still failed.
## Critical Issue: Virtualization Conflict ("Green Turtle")
### Symptoms
- Green turtle icon in Virtualbox status bar
- Extremely slow performance
- Fedora boot failures (systemd freeze, graphics failure)
### Root Cause
- Windows **Virtualization-Based Security (VBS)** was still active, forcing VirtualBox into a fallback mode:
```text
Windows → Hyper-V → VirtualBox → Fedora
```
Instead of direct hardware access.
### Failed Fix Attempts
These did NOT solve the issue (but they should've):
```powershell
bcdedit /set hypervisorlaunchtype off
bcdedit /set vsmlaunchtype off

dism /online /disable-feature /featurename:Microsoft-Hyper-V-All
dism /online /disable-feature /featurename:VirtualMachinePlatform
dism /online /disable-feature /featurename:WindowsHypervisorPlatform
```
Also did:
- Disable Hyper-V via windows features
- Disable memory integrity via core isolation
- Editing registry keys (`regedit` in `win + R`), specifically deviceguard and lsa to 0

RESULT: Green turtle persisted
## Breakthrough: Device Guard Removal
### Tool used
- Microsoft Device Guard Readiness Tool (`DG_Readiness_Tool_v3.6.ps1`) download from Microsoft.
### Steps Followed
The DG Readiness tool downloads as a zip file, so the first step was to extract the ile contents. Then moved it to a new directory since it is not just another file but a powershell script. The new directory became:
```plaintext
C:\Windows\System32
```
Then opened powershell as **administrator**, and navigated to the path:
```plaintext
C:\Windows\System32\dgreadiness_tool_v3.6.ps1
```
Then typed in the specific "nuke" command:
```
powershell

.\DG_Readiness_Tool.ps1 -Disable
```
and enter.
After that, performed the mandatory restart and followed all the booting instructions, by clicking the windows key first, followed by any key next, then windows key again and lastly any key.
### What it Did
- Disabled; `Device Guard`, `Credential Guard`, and `VBS` at boot level
- Modified **registry + UEFI** boot policies
### Result
- VirtualBox switched to direct hardware virtualization
- Indicator changed from green turtle to blue "V" (VT-x active)
- New architecture:
```plaintext
Windows → Virtualbox → Fedora
```
## Additional Issues Encountered
### VirtualBox version conflicts
- Version 7.1.16 → Nested paging issues
- Version 7.0.22 → Driver error:
```plaintext
VERR_SUP_VP_UNEXPECTED_VALID_PATH_COUNT
``` 
Due to windows security features.

**Final stable version: 7.2.6**
### Installation Freeze ("Finalization Loop")
#### Problem:
- Fedora installer stuck for hours during finalization
#### Solution (TTY Rescue):
Access terminal:
```plaintext
Left Ctrl + Left Alt + F3
```
Commands executed:
```plaintext
liveuser
```
```bash
sudo useradd -m intuitive_dialect  #intuitive_dialect is my username
sudo passwd intuitive_dialect    #this is not your password yet
```
```plaintext
New passwd: type in your real password (you will not see what you are typing)
confirm passwd: confirm your password
```
Then, give yourself administrative priviledge:
```bash
sudo usermod -aG wheel intuitive_dialect
sudo reboot
```
during reboot, remove the **ISO** from the optical drive by selecting machine on the top left bar of virtualbox, see optical drive options, select remove then force unmount.
### Boot Loop (EROFS Error)
#### Cause:
- ISO still attached after installation
- System kept booting into live environment
#### Fix:
- power off VM
- remove ISO from virtual drive manually in settings
#### Result:
- system booted fro VDI
- GRUB loaded correctly
## Verification
Successful setup confirmed by:
- Fedora boots without freeze
- No systemd freeze
- GNOME desktop loads normally
- Blue "V" visible in VirtualBox
- User account created with sudo access
- Internet working via NAT
## Lessons Learned
- The green turtle icon is not cosmetic, it is a critical diagnostic tool
- Disabling Hyper-V is not enough on modern Windows systems
- VBS (Device Guard / Credential Guard) operates below normal configuration layers
- Virtualization problems must be solved at the host level first, not inside the VM
- IDE controllers are effectively obsolete under modern firmware (UEFI)
- 3D acceleration in VirtualBox is unstable for many Linux guests
## Notes
- Always use SATA for modern OS installations
- Avoid unnecessary feature toggles unless you understand their impact
- Treat virtualization as a stack problem, not a single tool issue
- Once hardware virtualization is properly exposed, most “mysterious” errors disappear