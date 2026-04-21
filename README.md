# Bennett University Management System (UMS)

An advanced, decentralized multi-role desktop application engineered to streamline university administration workflows. Built natively with **Java AWT/Swing** and an embedded **SQLite** database, this system transitions away from legacy monolithic designs and utilizes a strict MVC architecture for maximum operational efficiency and zero-configuration portability.

## 🚀 Key Features

*   **Multi-Role Access Control (RBAC):** Independent operational portals for Administrators, Teachers, and Students securely mapped via a centralized authorization node.
*   **Decentralized Registration:** A staging methodology using a `pending_students` queue. New signups must be explicitly validated by an Administrator before migrating to the permanent database.
*   **Teacher Analytics Dashboard:** Localized domain access allowing faculty to seamlessly manage attendance tracking and semester result arrays without requiring top-level database access.
*   **Razorpay Gateway Integration:** An automated local web-bridge that dynamically generates HTML files to securely process student fee structures via the Razorpay Web SDK.
*   **Glassmorphism UI Engine:** Procedurally rendered translucent UI gradients using Java 2D Graphics, providing a highly premium aesthetic that scales beautifully on modern displays.

## 🛠️ Technology Stack
*   **Frontend:** Java Swing, AWT Graphics
*   **Backend:** Java (JDK 17)
*   **Database:** SQLite (Embedded JDBC)
*   **APIs:** Razorpay Payment Gateway

## 🗂️ Project Architecture
The system strictly adheres to the **Model-View-Controller (MVC)** paradigm:
*   **Model:** Direct DBConnection class handling isolated SQL queries and SQLite execution blocks.
*   **View:** Floating UI panels and procedural backgrounds replacing standard Swing layouts.
*   **Controller:** Role-based routing protocols instantiated upon successful login validation.

## 📈 Agile Development Schedule
*   **Phase 1:** Database Architecture & Table Normalization
*   **Phase 2:** Multi-Role Swing UI Bootstrapping
*   **Phase 3:** Advanced Logic & Payment Integrations
*   **Phase 4:** QA Testing, Security Audits & Final Deployment

---
*Developed by Priyansh Sharma (S25CSEU0495) and Kushagra Singh (S25CSEU0496) for Bennett University.*
