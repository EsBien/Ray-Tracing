# Ray-Tracing Project -3D Drops Simulation
This project simulates drops falling into pipes using ray-tracing techniques. <br/>
It is implemented in Python and is based on the pvtrace project, which has been reverse-engineered <br/>
and customized to meet the requirements of this simulation. <br/>

# System Requirements
Python: The project is implemented in Python programming language. <br/>
External Configuration File: Parameters can be accessed from an external configuration file, <br/>
making it easy to modify and access the simulation parameters. <br/>

# Functional Requirements
The system provides the following functionality: <br/>

Parameter Customization: Users can change the simulation parameters to create different scenes. <br/>
CSV Output: The output of the project is a CSV file containing data that can be used to train neural models. <br/>
Visualization: The project provides a visually appealing representation of the simulated scene based on the user-defined parameters. <br/>

# User Requirements
The system is designed to support the following user requirements: <br/>
Simulate rays on the full spectrum. <br/>
Modify parameters such as wavelengths, drop radius, lens positions, etc.,to customize the scene according to specific requirements. <br/>

# Technologies Used
The following technologies have been utilized in this project:<br/>

meshcat: Used to create a D3 simulation. <br/>
numpy: A Python library for array manipulation, linear algebra, Fourier transformation, and matrices. <br/>
pandas: An open-source data analysis and manipulation tool for Python. <br/>
Pvtrace: A full spectrum ray-tracing library. <br/>
anytree, trimesh[easy] <br/>

# Architecture
The project follows the following architecture: <br/>
![image](https://github.com/EsBien/Ray-Tracing/assets/96113739/ad70bbb7-e363-466b-8218-3741f0d135c9) <br/>

**User Input** : 
The user provides input parameters for the simulation. <br/>
Program Execution: The program runs based on the user-entered data, executing the scene simulation. <br/>
Ray Simulation: Drops start to flow in space, and light rays of varying wavelengths are transmitted every second. <br/>
Lens Sensors: Lens sensors detect the light rays that manage to reach the receivers through the drops. <br/>
Data Recording: Simulation data, including collision history and vulnerability of different wavelengths in the lenses, is recorded. <br/>
**CSV Output**:
The recorded data is stored in a CSV file at the end of each simulation run. <br/>
# Data Flow
The scene consists of light rays, liquid drops, and lenses. The collisions between rays and drops are recorded in a tracking history.<br/>
Additionally, data regarding the vulnerability of different wavelengths in the lenses is recorded in a CSV file.<br/>

# Usage
To use the project, follow these steps: <br/>

Set up the Python environment with the required dependencies (meshcat, numpy, pandas, and pvtrace,anytree, trimesh[easy]).<br/>
Customize the parameters in the configuration file to define the desired scene.<br/>
Run the program and observe the visual simulation generated based on the user-defined parameters.<br/>
At the end of each simulation run, the recorded data will be saved in a CSV file. <br/>
