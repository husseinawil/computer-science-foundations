# Hardware Architecture & System Bus Flow

This diagram illustrates how data flows between primary hardware components during execution.

```mermaid
graph TD
    subgraph Storage [Non-Volatile Storage]
        SSD[SSD / Flash Memory]
    end

    subgraph Memory [Primary Memory]
        RAM[RAM - Volatile Memory]
    end

    subgraph Processing Unit [CPU]
        ALU[Arithmetic Logic Unit]
        CU[Control Unit]
        REG[Registers]
    end

    SSD -- "1. Load Program/Data" --> RAM
    RAM -- "2. Fetch Instruction" --> CU
    CU -- "3. Execute Operation" --> ALU
    ALU -- "4. Store Temporary State" --> REG
    REG -- "5. Write Back Data" --> RAM
    RAM -- "6. Save File Changes" --> SSD

---

### Step 2: Push the diagram file to GitHub

Run this command block to commit and push:

```bash
git add -A
git commit -m "Add Mermaid architecture diagram to diagrams directory"
git push origin maincat << 'EOF' > digital-foundations/01-computer-fundamentals/diagrams/hardware-architecture.md
# Hardware Architecture & System Bus Flow

This diagram illustrates how data flows between primary hardware components during execution.

```mermaid
graph TD
    subgraph Storage [Non-Volatile Storage]
        SSD[SSD / Flash Memory]
    end

    subgraph Memory [Primary Memory]
        RAM[RAM - Volatile Memory]
    end

    subgraph Processing Unit [CPU]
        ALU[Arithmetic Logic Unit]
        CU[Control Unit]
        REG[Registers]
    end

    SSD -- "1. Load Program/Data" --> RAM
    RAM -- "2. Fetch Instruction" --> CU
    CU -- "3. Execute Operation" --> ALU
    ALU -- "4. Store Temporary State" --> REG
    REG -- "5. Write Back Data" --> RAM
    RAM -- "6. Save File Changes" --> SSD
