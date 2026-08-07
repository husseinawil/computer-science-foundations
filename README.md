# Computer Science Foundations Portfolio

A structured, hands-on repository documenting technical computer science fundamentals, system operations, and low-level mechanics executed via a Linux terminal environment.

---

## 🗺️ Curriculum & Portfolio Index

| Module | Module Title | Focus Areas | Status |
| :---: | :--- | :--- | :---: |
| **01** | [**Computer Fundamentals**](./digital-foundations/01-computer-fundamentals) | Architecture, Linux CLI, Memory, Networking | **Completed** |
| **02** | [**Data Structures & Algorithms**](./digital-foundations/02-data-structures-algorithms) | Arrays, Linked Lists, Stacks/Queues, Big-O Complexity | **Completed** |
| **03** | **Systems & Low-Level Concepts** | C Memory Allocation, Pointers, Compilation Pipeline | *Up Next* |
| **04** | **Software Engineering Practices** | Advanced Git, CI/CD, Modular Code Architecture | *Planned* |

---

## 📁 Repository Map

```text
computer-science-foundations/
├── assets/
│   └── hardware/                       <-- Environment photos & hardware assets
├── digital-foundations/
│   ├── 01-computer-fundamentals/      <-- Module 01 Dashboard
│   │   ├── diagrams/                   <-- Architecture flowcharts (Mermaid)
│   │   │   └── hardware-architecture.md
│   │   ├── labs/                       <-- Practical logs & terminal outputs
│   │   │   ├── lab-01-cli-basics.txt
│   │   │   ├── lab-02-data-representation.txt
│   │   │   └── lab-03-networking-and-os.txt
│   │   └── README.md
│   └── 02-data-structures-algorithms/ <-- Module 02 Dashboard
│       ├── code/                       <-- Algorithm & DS implementations
│       │   ├── array_operations.py
│       │   ├── linked_list.py
│       │   ├── search_algorithms.py
│       │   ├── sorting_algorithms.py
│       │   └── stack_queue.py
│       ├── labs/                       <-- Complexity & benchmark logs
│       │   ├── lab-01-array-complexity.txt
│       │   ├── lab-02-linked-list.txt
│       │   ├── lab-03-stack-queue.txt
│       │   ├── lab-04-searching.txt
│       │   └── lab-05-sorting.txt
│       └── README.md
└── README.md                           <-- Main Portfolio Landing Page

---

### Block 2: Setup Module 03 Directory
```bash
mkdir -p digital-foundations/03-systems-low-level/labs
mkdir -p digital-foundations/03-systems-low-level/code

cat << 'EOF' > digital-foundations/03-systems-low-level/README.md
# 03. Systems & Low-Level Concepts

Low-level system mechanics, memory management, C programming, and compilation pipelines.

---

## 📁 Subdirectory Structure
* **[`code/`](./code/)** — C source code files, memory allocation, and pointer manipulations.
* **[`labs/`](./labs/)** — Compilation logs, assembly outputs, and memory analysis logs.

---

## 🛠️ Core Competencies Index
* **C Programming:** Pointers, memory addresses, structs, manual memory management (`malloc`/`free`).
* **Compilation Pipeline:** Preprocessing, compilation, assembly, and linking GCC/Clang stages.
* **Memory Layout:** Stack vs. Heap allocation, pointer arithmetic, and buffer limits.
EOFgit add -A
git commit -m "Complete Module 02 root index and initialize Module 03 Systems directory"
git push origin main
cat << 'EOF' > digital-foundations/03-systems-low-level/README.md
# 03. Systems & Low-Level Concepts

Low-level system mechanics, memory management, C programming, and compilation pipelines.

---

## 📁 Subdirectory Structure
* **[`code/`](./code/)** — C source code files, memory allocation, and pointer manipulations.
* **[`labs/`](./labs/)** — Compilation logs, assembly outputs, and memory analysis logs.

---

## 🛠️ Core Competencies Index
* **C Programming:** Pointers, memory addresses, structs, manual memory management (`malloc`/`free`).
* **Compilation Pipeline:** Preprocessing, compilation, assembly, and linking GCC/Clang stages.
* **Memory Layout:** Stack vs. Heap allocation, pointer arithmetic, and buffer limits.
