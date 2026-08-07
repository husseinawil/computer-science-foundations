# System Architecture & Network Flow

This diagram outlines how data moves from a local machine through the network stack during a web request.

```text
[ User / Terminal ] 
        │ (cURL / Ping)
        ▼
[ Operating System (Kernel / Network Stack) ]
        │ (TCP/IP Packets)
        ▼
[ Network Interface Card (NIC) / Hardware Router ]
        │ (DNS Resolution to IP)
        ▼
[ Internet / Remote Server ]
find ~ -name "computer-science-foundations" -type d
