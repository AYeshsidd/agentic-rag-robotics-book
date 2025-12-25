# Research for Module 1: The Robotic Nervous System (ROS 2)

## 1. ROS 2 Scope (Core Middleware vs. Extended Tools)

**Decision**: Focus on the core middleware concepts (Nodes, Topics, Services, Actions) and `rclpy` as the primary Python interface. Extended tools (e.g., RViz, Gazebo integration beyond basic URDF visualization) will be mentioned conceptually but not covered in depth within this module.

**Rationale**: For an undergraduate/early graduate target audience, a strong foundation in core ROS 2 communication patterns and Python integration is paramount. Diving into the vast ecosystem of extended tools prematurely can overwhelm learners and dilute the focus on fundamental principles. These extended tools will be covered in subsequent modules (e.g., Module 2 for Gazebo).

**Alternatives Considered**:
-   Covering a broader range of ROS 2 tools: Rejected due to potential for information overload and scope creep within a single module.
-   Limiting to only conceptual overview: Rejected as practical `rclpy` examples are crucial for skill development.

## 2. Best Practices for `rclpy` in Educational Content

**Decision**: Provide clear, concise, and runnable `rclpy` examples for each core ROS 2 concept (Nodes, Topics, Services, Actions). Examples will be self-contained where possible, well-commented, and focus on illustrating a single concept effectively. Use a consistent Python version (e.g., Python 3.8+ compatible with the chosen ROS 2 distro).

**Rationale**: Hands-on examples are vital for teaching programming concepts. Clarity and simplicity are prioritized to ensure students can easily adapt and extend the provided code. Consistency in language version avoids unnecessary compatibility issues.

**Alternatives Considered**:
-   More complex, real-world examples: Rejected for foundational learning to avoid distracting from core concepts with application-specific details.
-   Minimalist, abstract examples: Rejected as concrete, runnable code is more engaging and effective for practical understanding.

## 3. Level of Humanoid Detail in URDF Examples

**Decision**: Present simplified humanoid URDF examples focusing on fundamental elements (links, joints, inertia, visual, collision). Examples will illustrate a basic kinematic chain (e.g., a single arm or leg) before conceptually expanding to a full humanoid structure. Visualizations (e.g., using `urdf_to_graphiz` or RViz screenshots) will be heavily utilized.

**Rationale**: Full humanoid URDF can be highly intricate. Starting with simplified examples allows students to grasp the structure and syntax without being overwhelmed, gradually building towards complexity. Visual aids are crucial for understanding spatial relationships.

**Alternatives Considered**:
-   Presenting a full, complex humanoid URDF from the outset: Rejected due to the high learning curve and potential for demotivation.
-   Only conceptual discussion without examples: Rejected as practical syntax and structure are essential for understanding URDF.

## 4. Recommended ROS 2 Distribution and Version

**Decision**: Specify ROS 2 Humble Hawksbill as the primary distribution for all examples. All code examples will be tested and verified against this version. A note will be included to advise students on potential differences with newer distributions (e.g., Iron Irwini) and how to consult official documentation for updates.

**Rationale**: Humble Hawksbill is a Long Term Support (LTS) release, ensuring stability and long-term relevance for a textbook. This reduces the likelihood of examples quickly becoming outdated. Providing a single, consistent version simplifies the learning environment for students.

**Alternatives Considered**:
-   Using the absolute latest ROS 2 distribution: Rejected due to potential for rapid deprecations and breaking changes, which is undesirable for a textbook.
-   Providing examples for multiple ROS 2 distributions: Rejected due to increased complexity in content creation and maintenance, and potential for student confusion.

## 5. Markdown-compatible APA Citation Style Examples for Docusaurus

**Decision**: Implement a Markdown-compatible version of APA 7th edition citation style. This will involve using inline citations with author-date format and a numbered bibliography section at the end of each chapter, referencing a central `.bib` or `.yaml` file for sources. Markdown links will be used for direct access to online sources.

**Rationale**: APA 7th edition is a widely recognized academic citation standard. Markdown compatibility ensures proper rendering within Docusaurus. A consistent, centralized reference management approach simplifies content creation and maintenance, while direct links enhance accessibility.

**Alternatives Considered**:
-   Using plain text citations without specific formatting: Rejected as it deviates from academic standards.
-   Implementing complex citation plugins for Docusaurus: Rejected to maintain simplicity and avoid dependency on potentially brittle third-party tools, especially if they are not Markdown-native. The goal is to provide Markdown-compatible examples, not a full citation management system.
