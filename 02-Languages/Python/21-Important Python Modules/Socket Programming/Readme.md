## Introduction

- Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC).

  - A socket is one endpoint of a two-way communication link between two programs running on the network.
  - Sockets allow communication between two different processes on the same or different machines.
  - It's a way to talk to other computers using standard Unix file descriptors.

- The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks.

  - Eg. Internet, which you connect to via your ISP.

- Sockets have a long history. Their use originated with ARPANET in 1971 and later became an API in the Berkeley Software Distribution (BSD) operating system released in 1983 called Berkeley sockets.

- The most common type of socket applications are client-server applications, where one side acts as the server and waits for connections from clients.

  - Most of the application-level protocols like FTP, SMTP, and POP3 make use of sockets to establish connection between client and server and then for exchanging data.
  - The socket API for Internet sockets is called Berkeley or BSD sockets.
  - There are also Unix domain sockets, which can only be used to communicate between processes on the same host.

- Although the underlying protocols used by the socket API have evolved over the years, and new ones have developed, the low-level API has remained the same.

- There are four types of sockets available to the users.

  - **Stream Sockets**

    - These sockets use TCP (Transmission Control Protocol) for data transmission.
    - Delivery in a networked environment is guaranteed. If you send through the stream socket three items "A, B, C", they will arrive in the same order − "A, B, C".
    - If delivery is impossible, the sender receives an error indicator.
    - Data records do not have any boundaries.

  - **Datagram Sockets**

    - They use UDP (User Datagram Protocol).
    - Delivery in a networked environment is not guaranteed.
    - They're connectionless because you don't need to have an open connection as in Stream Sockets − you build a packet with the destination information and send it out.

  - **Raw Sockets**

    - These provide users access to the underlying communication protocols, which support socket abstractions.
    - These sockets are normally datagram oriented, though their exact characteristics are dependent on the interface provided by the protocol.
    - Raw sockets are not intended for the general user; they have been provided mainly for those interested in developing new communication protocols, or for gaining access to some of the more cryptic facilities of an existing protocol.

  - **Sequenced Packet Sockets**
    - They are similar to a stream socket, with the exception that record boundaries are preserved.
    - This interface is provided only as a part of the Network Systems (NS) socket abstraction, and is very important in most serious NS applications.
    - Sequenced-packet sockets allow the user to manipulate the Sequence Packet Protocol (SPP) or Internet Datagram Protocol (IDP) headers on a packet or a group of packets, either by writing a prototype header along with whatever data is to be sent, or by specifying a default header to be used with all outgoing data, and allows the user to receive the headers on incoming packets.

## Socket Programming

- Socket programming is a way of connecting two nodes on a network to communicate with each other.

- Sockets are commonly used for client and server interaction. Typical system configuration places the server on one machine, with the clients on other machines. The clients connect to the server, exchange information, and then disconnect.

- One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection.
  - Server forms the listener socket while client reaches out to the server.

## Socket Programming in Python

- Python’s socket module provides an interface to the Berkeley sockets API.
  - It provides a convenient and consistent API that maps directly to system calls, their C counterparts.
- There are also many modules available that implement higher-level Internet protocols like HTTP and SMTP also modules like socketserver, a framework for network servers.
- We can use both TCP and UDP protocol for socket.
  - The Transmission Control Protocol (TCP)
    - Is reliable i.e. Packets dropped in the network are detected and retransmitted by the sender.
    - Has in-order data delivery: Data is read by your application in the order it was written by the sender.
    - Sequence of socket API calls and data flow for TCP:
      ![Socket TCP Flow](../img/sockets-tcp-flow.webp "Socket TCP Flow")
  - User Datagram Protocol (UDP) sockets aren’t reliable, and data read by the receiver can be out-of-order from the sender’s writes.
