# Minor_Project_TechMates
MINI PTOJECT
TECHMATES

Title
Performance Analysis of Auto-Scaling Policies in Cloud Computing

1. Introduction
With the growing adoption of cloud computing, modern applications are expected to handle highly dynamic and unpredictable workloads while maintaining consistent performance and reasonable operational cost. Cloud platforms provide auto-scaling mechanisms that automatically adjust computing resources based on workload demand.
However, different auto-scaling strategies behave differently under real-world traffic patterns. Some prioritize cost efficiency, while others focus on performance stability. Understanding these trade-offs is essential for designing reliable and scalable cloud-based systems.
This mini project focuses on experimentally analyzing and comparing different auto-scaling policies by deploying a controlled web application in a cloud environment and observing its behavior under varying workloads.
________________________________________
2. Problem Statement
Although cloud providers offer multiple auto-scaling policies, developers often lack clear insights into:
•	How quickly each policy reacts to workload changes
•	How scaling decisions impact response time and resource utilization
•	The cost implications of aggressive vs conservative scaling
This project aims to study these aspects by running controlled experiments and comparing auto-scaling strategies using measurable performance metrics.
________________________________________
3. Objective of the Project
The primary objectives of this project are:
•	To design a minimal cloud-based application suitable for performance measurement
•	To implement and evaluate different auto-scaling policies
•	To analyze system behavior under low, moderate, and burst workloads
•	To study the trade-off between performance, stability, and cost
•	To derive practical insights that can guide real-world cloud deployment decisions
________________________________________
4. Proposed Solution Approach
The proposed solution follows a step-by-step experimental methodology:
1.	Develop a minimal web application with predictable and repeatable CPU behavior
2.	Deploy the application on a cloud virtual machine
3.	Configure an auto-scaling group using identical system settings
4.	Apply different auto-scaling policies one at a time
5.	Generate controlled workloads using a load testing tool
6.	Monitor system metrics using cloud-native monitoring services
7.	Collect and analyze performance data
8.	Compare results across policies to identify strengths and limitations
Only one variable (scaling policy) will be changed at a time to ensure a fair and valid comparison.
________________________________________
5. Auto-Scaling Policies Under Study
The project will analyze the following auto-scaling strategies:
•	Manual Scaling: Instances are added or removed manually based on observed load
•	Threshold-Based Scaling: Scaling decisions are triggered when predefined CPU utilization thresholds are crossed
•	Predictive Scaling: Scaling decisions are made using historical workload patterns to anticipate future demand
________________________________________
6. Performance Metrics
The system will be evaluated using the following metrics:
•	Average response time
•	Tail latency (P95 response time)
•	CPU utilization
•	Number of scaling events
•	Average number of active instances
•	Estimated operational cost
These metrics provide a balanced view of user experience, system stability, and cost efficiency.
________________________________________
7. Scope and Constraints
Scope:
•	Focused on compute-layer auto-scaling
•	Single-region cloud deployment
•	Stateless web application
Constraints:
•	No database or persistent storage
•	Limited instance count for cost control
•	Fixed workload patterns for repeatability
________________________________________
8. Expected Outcome
The expected outcome of this project is a comparative performance analysis that clearly demonstrates how different auto-scaling policies behave under identical workload conditions. The results will help identify which policies are better suited for:
•	Cost-sensitive applications
•	Performance-critical applications
•	Predictable vs unpredictable workloads
________________________________________
9. Conclusion
This project is designed as a controlled, practical study of cloud auto-scaling behavior rather than a feature demonstration. By keeping the application simple and the experiment well-defined, the focus remains on understanding system behavior and making informed engineering trade-offs.


