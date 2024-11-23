This work examines the impact that the finalists of the post-quantum cryptography competition organized by NIST have on a critical security protocol for the Internet, the TLS protocol. The analysis is supported by an extensible framework that enables the implementation of a baseline scenario, allowing for a fair comparison of different post-quantum primitives under identical conditions. 

The project currently has two folders:

* **IdealScenario**: This folder contains the data from the work called *Towards the Quantum-Safe Web:Benchmarking Post-Quantum TLS*.

* **RealScenarios**: Support for delay and packet loss has been added to the framework to simulate a real-world working scenario.

Each folder has three subfolders:

* **Docker**: The files needed to create the Docker image, as well as the scripts used to create a TLS client and server.
* **Experiment**: It contains: 
 - **Logs**: The logs obtained in the execution.
 - **process_scripts**: The python scripts used to process the logs and obtain the plots.
 -  **Output**:
   		- The csv obtained when processing the logs.
		- The images of the plots obtained.
	-  **docker_dcripts**: The scripts used to launch the TLS clients and servers with the various traditional and post-quantum algorithms.