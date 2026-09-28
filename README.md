# TCP Client-Server Chat with Wireshark Traffic Analysis

A simple TCP server and client written in Python using the `socket` module. Both programs run on the same machine (localhost) and exchange messages. The traffic is captured with Wireshark to verify that it is plain, direct TCP with no tunnel or extra encapsulation.

This project was made for a Cyber Security course assignment.

## Objectives

1. Write a server-side network program.
2. Write a client-side network program.
3. Capture the messages exchanged between them using a packet capture tool (Wireshark).
4. Verify that the connection is direct and that no tunnel is being created.

## Project Structure

```
.
├── server.py     # TCP server (listens on port 5000)
├── client.py     # TCP client (connects to 127.0.0.1:5000)
└── README.md
```

## Requirements

- Python 3.x
- Wireshark with Npcap (Windows) for loopback capture

No extra Python libraries are needed.

## How to Run

1. Open two terminals in the project folder.

2. Start the server in the first terminal:

   ```bash
   python server.py
   ```

   Output: `Waiting...`

3. Start the client in the second terminal:

   ```bash
   python client.py
   ```

4. Type a message at the `You:` prompt and press Enter. The server replies with `Server got: <message>`.

5. Type `exit` to close the client. The server stops automatically when the connection closes.

> If `python` is not recognized on Windows, use `py server.py` and `py client.py`.

## How It Works

**Server (`server.py`)**
- Creates a TCP socket and binds it to `0.0.0.0:5000`.
- Listens and accepts one client connection.
- Receives messages in a loop, prints them, and sends back an acknowledgement.
- Closes when the client disconnects.

**Client (`client.py`)**
- Creates a TCP socket and connects to `127.0.0.1:5000`.
- Reads user input, sends it to the server, and prints the reply.
- Stops when the user types `exit`.

## Traffic Capture with Wireshark

1. Open Wireshark and select **Adapter for loopback traffic capture**.
2. Apply the display filter:

   ```
   tcp.port == 5000
   ```

3. Start the server and client, then send a few messages.
4. Stop the capture and inspect the packets.

### What the capture shows

- **TCP three-way handshake:** `SYN`, `SYN-ACK`, `ACK`
- **Message packets:** `PSH, ACK` (client to server and server to client)
- **Connection close:** `FIN, ACK`
- Right-click a data packet and choose **Follow > TCP Stream** to see the messages in plain text.

## Tunnel Verification

A tunnel wraps the original packet inside another protocol (GRE, IP-in-IP, IPsec/ESP, SSH, VPN). To check for this, open a data packet and look at its layers:

```
Frame > Null/Loopback > Internet Protocol (127.0.0.1 -> 127.0.0.1) > TCP (port 5000) > Data
```

Result: there is no extra outer header, the source and destination IPs are the real endpoints, and the data is visible as plain text.

**Conclusion:** the traffic is direct TCP with no encapsulation, so the server is not creating a tunnel.

## Notes

- Messages are sent in plain text (no encryption), which is why they are readable in Wireshark.
- The server handles a single client at a time.

## Author

Syed Najmuddin
