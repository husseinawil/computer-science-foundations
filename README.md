# Computer Science Foundations Portfolio

A structured, hands-on repository documenting technical computer science fundamentals, system operations, and low-level mechanics executed via a Linux terminal environment.

---

## 🗺️ Curriculum & Portfolio Index

| Module | Module Title | Focus Areas | Status |
| :---: | :--- | :--- | :---: |
| **01** | [**Computer Fundamentals**](./digital-foundations/01-computer-fundamentals) | Architecture, Linux CLI, Memory, Networking | **Completed** |
| **02** | [**Data Structures & Algorithms**](./digital-foundations/02-data-structures-algorithms) | Arrays, Linked Lists, Stacks/Queues, Big-O Complexity | **Completed** |
| **03** | [**Systems & Low-Level Concepts**](./digital-foundations/03-systems-low-level) | C Memory Allocation, Pointers, Compilation Pipeline | **Completed** |
| **04** | **Software Engineering Practices** | Advanced Git, CI/CD, Modular Code Architecture | *Up Next* |

---

## 📁 Repository Map

```text
computer-science-foundations/
├── assets/
│   └── hardware/                       <-- Environment photos & hardware assets
├── digital-foundations/
│   ├── 01-computer-fundamentals/      <-- Module 01 Dashboard
│   │   ├── diagrams/
│   │   │   └── hardware-architecture.md
│   │   ├── labs/
│   │   │   ├── lab-01-cli-basics.txt
│   │   │   ├── lab-02-data-representation.txt
│   │   │   └── lab-03-networking-and-os.txt
│   │   └── README.md
│   ├── 02-data-structures-algorithms/ <-- Module 02 Dashboard
│   │   ├── code/
│   │   │   ├── array_operations.py
│   │   │   ├── linked_list.py
│   │   │   ├── search_algorithms.py
│   │   │   ├── sorting_algorithms.py
│   │   │   └── stack_queue.py
│   │   ├── labs/
│   │   │   ├── lab-01-array-complexity.txt
│   │   │   ├── lab-02-linked-list.txt
│   │   │   ├── lab-03-stack-queue.txt
│   │   │   ├── lab-04-searching.txt
│   │   │   └── lab-05-sorting.txt
│   │   └── README.md
│   └── 03-systems-low-level/           <-- Module 03 Dashboard
│       ├── code/
│       │   ├── compilation_demo.c
│       │   ├── memory_pointers.c
│       │   └── struct_alignment.c
│       ├── labs/
│       │   ├── lab-01-memory-pointers.txt
│       │   ├── lab-02-compilation-pipeline.txt
│       │   └── lab-03-struct-padding.txt
│       └── README.md
└── README.md                           <-- Main Portfolio Landing Page

---

### Step 2: Initialize Module 04 Directory Structure

Run this command block to set up **`04-software-engineering`**:

```bash
mkdir -p digital-foundations/04-software-engineering/labs
mkdir -p digital-foundations/04-software-engineering/code

cat << 'EOF' > digital-foundations/04-software-engineering/README.md
# 04. Software Engineering Practices

Modular software architecture, CI/CD pipeline automation, testing, and advanced Git workflow patterns.

---

## 📁 Subdirectory Structure
* **[`code/`](./code/)** — Modular python packages, test cases, and script utilities.
* **[`labs/`](./labs/)** — CI/CD workflow configurations, Git branching logs, and unit testing outputs.

---

## 🛠️ Core Competencies Index
* **Modular Architecture:** Separation of concerns, module imports, and clean code principles.
* **Automated Testing:** Unit testing with `unittest` / `pytest` and assertion coverage.
* **CI/CD & DevOps:** GitHub Actions workflow pipelines, linting, and automated testing builds.
