This work examines the impact that the finalists of the post-quantum cryptography competition organized by NIST have on a critical security protocol for the Internet, the TLS protocol. The analysis is supported by an extensible framework that enables the implementation of a baseline scenario, allowing for a fair comparison of different post-quantum primitives under identical conditions. 

The project currently has three folders:

* **Original**: This folder contains the original work called *Towards the Quantum-Safe Web*.

* **Standards**: This is a modification of the original work to substitute Kyber for ML-KEM and Dilithium for ML-DSA.

* **TC**: A delay and packet loss support has been added to the framework to simulate a real working scenario.

Each folder has three subfolders:

* **Docker**: The files needed to create the Docker image, as well as the scripts used to create a TLS client and server.
* **Data**: It contains the information necessary to create the graphs: 
	- The logs obtained in the execution.
	- The csv obtained when processing the logs.
	- The images of the graphs obtained.
	- The python scripts used to process the logs and make the graphs.
* **Execution_Scripts**: The scripts used to launch the TLS clients and servers with the various traditional and post-quantum algorithms.