# Data Model: Module 2: The Digital Twin (Gazebo & Unity)

This data model describes the conceptual structure of the educational content for Module 2, ensuring consistency and clarity in its organization. It largely follows the structure established in Module 1, adapting `KeyConcept` to reflect simulation-specific entities.

## Entities

### 1. Module (`digital-twin-gazebo-unity`)

Represents a single learning module within the textbook.

-   **`title` (String)**: The official title of the module (e.g., "The Digital Twin (Gazebo & Unity)").
-   **`description` (String)**: A brief overview or summary of the module's content and objectives.
-   **`target_audience` (String)**: Specifies the intended learners (e.g., "Undergraduate/early graduate AI & robotics students").
-   **`word_count_range` (String)**: The expected length of the module in words (e.g., "2500–4000 words").
-   **`timeline` (String)**: The estimated time for content development and review (e.g., "2-week").
-   **`chapters` (List of Chapter objects)**: A collection of Chapter entities that constitute the module.

### 2. Chapter

Represents an individual chapter within a module, a primary organizational unit for learning content.

-   **`chapter_number` (Integer)**: A numerical identifier indicating the chapter's order within the module.
-   **`title` (String)**: The title of the chapter (e.g., "Gazebo Physics: Gravity, collisions").
-   **`objectives` (List of Strings)**: A list of specific learning objectives that students should achieve upon completing the chapter.
-   **`concepts_covered` (List of KeyConcept objects)**: A collection of distinct technical or theoretical ideas explained in the chapter.
-   **`examples` (List of Strings)**: Descriptions or references to simulation setups, code snippets, diagrams, or practical exercises included in the chapter.
-   **`summary` (String)**: A brief recap of the chapter's main points.
-   **`references` (List of Citation objects)**: A collection of sources cited within the chapter.

### 3. KeyConcept

Represents a fundamental technical or theoretical concept presented in the module, specifically tailored to digital twin and simulation topics.

-   **`name` (String)**: The official name of the concept (e.g., "Gazebo Physics Engine", "LiDAR Sensor").
-   **`definition` (String)**: A concise explanation of what the concept is.
-   **`key_attributes` (List of Strings)**: Important properties or characteristics of the concept.
-   **`usage_context` (String)**: Describes when and how the concept is typically applied in digital twin scenarios.

### 4. Citation

Represents a reference to an external source used to verify technical claims or provide further reading.

-   **`full_citation_text` (String)**: The complete academic citation of the source (e.g., "Author, A. A. (Year). Title of work. Publisher.") adhering to a Markdown-compatible APA style.
-   **`markdown_format` (String)**: How the citation appears within the Markdown text (e.g., "[1]" or "(Author, Year)").
-   **`source_type` (String)**: Categorization of the source (e.g., "peer-reviewed paper", "official documentation", "textbook").

## Relationships

-   **Module has Chapters**: A one-to-many relationship, where one Module contains multiple Chapters.
-   **Chapter covers KeyConcepts**: A many-to-many relationship, where a Chapter can explain multiple KeyConcepts, and a KeyConcept can be discussed across multiple Chapters (though primarily defined in one).
-   **Chapter has Citations**: A one-to-many relationship, where a Chapter can cite multiple sources.

## Validation Rules

-   All `title` fields MUST be non-empty.
-   `chapter_number` MUST be unique within a Module and sequential.
-   All `references` MUST adhere to the defined Markdown-compatible APA citation style.
-   `word_count_range` and `timeline` MUST be respected for the Module.