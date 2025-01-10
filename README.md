#Movie Booking System


Introduction

The Movie Booking System is a web-based application designed to provide users with a seamless experience in booking movie tickets online. The system allows users to view available movies, select seats, and confirm their bookings, making the ticketing process efficient and user-friendly. By integrating data structures like graphs, queues, and heaps, this project aims to optimize seat allocation and booking management.


Problem Domain

The traditional movie ticket booking process involves manual operations, long queues, and high chances of errors in seat allocation. Additionally, VIP seat prioritization is often overlooked in traditional systems. The need for an automated, efficient, and user-friendly solution to manage bookings and seat assignments led to the development of this Movie Booking System.


Expected Outcome

•	Browse available movies.
•	Select seats based on availability.
•	Book tickets efficiently.
•	Manage bookings with VIP prioritization.

The solution includes a graphical seat selection interface, efficient data handling using priority queues for VIP bookings, and a graph-based seat allocation system.
Requirements


Data Structures:

•	Graph: Used to represent the seating arrangement and establish connections between adjacent seats.
•	Priority Queue (Heap): Manages VIP bookings based on priority levels.
•	Queue (Deque): Handles regular bookings in a first-come, first-served manner.

Software:

•	Python: Backend logic using Flask framework.
•	HTML & CSS: Frontend development for creating web pages.
•	Flask: Web framework to build the application.
•	Heapq & Collections: Python libraries for priority queues and deques.



Methodology

The methodology for developing the Movie Booking System involves the following steps:

Phase 1: Requirement Analysis: Identify the functionalities required for the system, including seat selection, booking, and VIP handling.

Phase 2: Design and Implementation

•	Graph Implementation: The graph represents the theatre’s seating layout. Each seat is a node, and edges connect adjacent seats. This helps in managing seat adjacency checks and ensuring that group bookings are handled efficiently.
•	Priority Queue for VIP Bookings: VIP bookings are added to a min-heap based on their priority level. The heapq library in Python is used to implement this priority queue efficiently.
•	Queue for Regular Bookings: A queue (deque) is utilized to handle regular bookings on a first-come, first-served basis. The collections module in Python provides an efficient deque implementation.

Phase 4: Booking Workflow

1.	User selects a movie and seat(s).
2.	System checks seat availability using the graph structure.
3.	If VIP booking, the priority queue is used to handle the request.
4.	For regular bookings, the deque processes the request in order.
5.	The user gets a popup confirming the booking.
   
Phase 5: Testing : Ensure that the system works efficiently by testing various booking scenarios.



Sample Screenshots 

Home page:

![image](https://github.com/user-attachments/assets/b9a0b0f9-46b3-4c53-8582-5d4f4745f373)

View seats page:

![image](https://github.com/user-attachments/assets/82201eaf-2873-49d4-9ee1-416d18c434ec)

Booking Tickts page:

![image](https://github.com/user-attachments/assets/099ee0e3-c8e2-495d-accc-c81c60d93ba4)


Summary:

The Movie Booking System provides a modern solution to traditional ticket booking problems. By utilizing efficient data structures like graphs and priority queues, it enhances seat management and booking processes. The application is scalable and can be extended to include more features, such as payment integration and user accounts, making it a comprehensive movie booking platform.
