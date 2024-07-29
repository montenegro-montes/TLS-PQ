This work examines the obstacles associated with integrating the recently standardized post-quantum cryptographic algorithms into the protocol that serves as the foundation for protecting the Web. In particular, we investigate the overhead, in terms of computation and communication, in the Transport Layer Security (TLS) protocol.

The project has three folders:

* **Docker**: The files needed to create the Docker image, as well as the scripts used to create a TLS client and server.
* **Logs**: The logs obtained from the experiment and used to generate the graphs included in the paper: *Towards the Quantum-Safe Web*.
* **Scripts**: The scripts used to launch the TLS clients and servers with the various traditional and post-quantum algorithms. It also includes Python programs to create the graphs.
