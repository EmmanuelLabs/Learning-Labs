# Huawei VRP (Versatile Routing Platform) – Complete Study Notes

---

# 1. Overview of VRP

## Definition

Huawei VRP is the operating system used on Huawei networking devices such as routers, switches, and firewalls.

## Core Functions

* Controls hardware operations
* Runs network protocols (routing, switching)
* Manages configurations
* Provides CLI interface for user interaction

## Key Idea

VRP = Operating System → Controls device behavior and traffic forwarding

---

# 2. VRP Architecture

## Control Plane

* Runs on CPU
* Responsible for:

  * Routing protocols (OSPF, BGP)
  * Routing table generation
  * ARP/MAC learning
  * Processing CLI commands

## Data Plane

* Runs on ASIC (hardware chips)
* Responsible for:

  * High-speed packet forwarding
  * Applying ACLs, VLANs, QoS

## Tables

* Routing Table (Control Plane)
* Forwarding Table / FIB (Data Plane)

## Key Flow

Control Plane → Builds routes → Programs Data Plane → Packets forwarded

---

# 3. CLI Command Structure

## Views (Modes)

### User View

```
<Huawei>
```

* Monitoring only
* No configuration allowed

### System View

```
[Huawei]
```

Command:

```
system-view
```

* Global configuration

### Feature Views (Sub-views)

Example:

```
[Huawei-GigabitEthernet0/0/1]
```

Command:

```
interface GigabitEthernet 0/0/1
```

---

## Navigation Commands

```
system-view   → Enter system view
quit          → Go one level up
return        → Return to user view
```

---

## Command Structure

```
keyword + parameters
```

Example:

```
ip address 192.168.1.1 255.255.255.0
```

---

# 4. Navigation & Help System

## Help Commands

```
?                → List available commands
display ?        → Show next-level options
display ip ?     → Show deeper options
```

## Command Completion

```
TAB → Auto-complete command
```

## Command Abbreviation

```
display ip routing-table
dis ip rou
```

## Common Errors

* Unrecognized command → Wrong command/view
* Incomplete command → Missing parameters
* Wrong parameter → Invalid argument

---

# 5. Configuration Management

## Types of Configuration

### Current Configuration

* Stored in RAM
* Active immediately

### Startup Configuration

* Stored in Flash
* Loaded on reboot

---

## Save Configuration

```
save
```

## View Current Configuration

```
display current-configuration
```

---

## Key Concept

Current Config → (save) → Startup Config

---

# 6. File System & Storage

## Storage Types

| Type   | Purpose                        |
| ------ | ------------------------------ |
| SDRAM  | Running config, temporary data |
| Flash  | OS file, startup config        |
| NVRAM  | Boot settings                  |
| USB/SD | External storage               |

---

## File System

```
flash:/
```

---

## File Commands

```
dir                 → List files
cd flash:/          → Change directory
more filename.cfg   → View file
delete filename.cfg → Delete file
```

---

## Important Files

* VRP system file: `vrp.cc`
* Configuration file: `vrpcfg.cfg`

---

# 7. Boot Process

## Steps

1. Power ON
2. BootROM runs
3. Hardware check
4. Load VRP from flash
5. Load startup config
6. System ready

---

## Key Components

* BootROM → Loads OS
* Flash → Stores OS & config
* NVRAM → Stores boot instructions

---

# 8. File Transfer (Concept)

## Methods

* FTP
* TFTP
* USB

## Use Cases

* Backup configuration
* Restore configuration
* Upgrade VRP
* Troubleshooting (log export)

---

# 9. System Management

## Device Identity

```
sysname Core-Switch
```

---

## System Time

```
clock datetime HH:MM:SS YYYY-MM-DD
```

---

## AAA (Authentication, Authorization, Accounting)

### Create User

```
aaa
local-user admin password cipher Huawei@123
local-user admin privilege level 15
```

### Definitions

* Authentication → Who are you?
* Authorization → What can you do?
* Accounting → What did you do?

---

## Remote Access

### VTY Lines

```
user-interface vty 0 4
```

### Access Types

* Telnet (insecure)
* SSH (secure)

---

## Access Methods

* Console → Physical access
* VTY → Remote access

---

# 10. Access Control Lists (ACLs)

## Function

Filters traffic based on rules

## Rule Processing

* Top-down
* First match wins
* Implicit deny at end

---

## Types

* Basic ACL → Source IP only
* Advanced ACL → Source, destination, protocol, port

---

## Application

* Applied to interfaces
* Direction:

  * Inbound
  * Outbound

---

# 11. Software & Versioning

## VRP Versions

* Different OS releases (V5, V8, etc.)
* Include updates, fixes, features

---

## System File

```
flash:/vrp.cc
```

---

## Boot File Selection

* Defined in boot settings (NVRAM)

---

## Upgrade Process

1. Obtain new VRP file
2. Transfer to device
3. Set as boot file
4. Reboot

---

## Key Concepts

* Flash stores OS
* BootROM loads OS
* Backup before upgrade
* Compatibility is critical

---

## Dual Image

* Primary OS
* Backup OS
* Ensures reliability

---

# FINAL CORE MODEL

* BootROM → Starts system
* VRP → Operating system
* Config file → Device behavior
* Flash → Permanent storage
* RAM → Active processes
* AAA → User control
* ACL → Traffic control

---

# QUICK REVISION CHECKLIST

* VRP = OS
* Control vs Data Plane
* CLI hierarchy (User → System → Interface)
* Help system (?, TAB)
* Current vs Startup config
* Flash vs RAM
* Boot process sequence
* AAA & VTY
* ACL logic (top-down, implicit deny)
* Upgrade process

---
