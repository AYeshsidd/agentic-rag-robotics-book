# Quickstart Guide: Module 4: Vision-Language-Action (VLA)

## Getting Started

This guide provides a quick overview for setting up your environment and understanding the module's content structure.

### 1. Prerequisites

Before you begin, ensure you have access to or understand the following:

-   **OpenAI API Key**: Required for accessing OpenAI Whisper for speech-to-text.
-   **LLM API Key**: Required for accessing a Large Language Model (e.g., OpenAI GPT series, Google Gemini) for cognitive planning.
-   **ROS 2**: Humble Hawksbill distribution or compatible. Follow official ROS 2 documentation for installation: [https://docs.ros.org/en/humble/Installation.html](https://docs.ros.org/en/humble/Installation.html)
-   **Python**: Python 3.8+ (for interacting with APIs and ROS 2).
-   **Docusaurus**: For viewing and contributing to the textbook content. Installation instructions can be found [https://docusaurus.io/docs/installation](https://docusaurus.io/docs/installation).
-   **Git**: Version control system.

### 2. Module Content Structure

The content for this module is located in the `docs/vision-language-action-vla/` directory of the project repository. It is organized into chapters, as detailed in the `specs/004-vision-language-action-vla/data-model.md`.

```text
docs/
└── vision-language-action-vla/
    ├── chapter1.md
    ├── chapter2.md
    └── chapter3.md
```

### 3. Running Examples

Conceptual examples of VLA pipelines, including voice command processing, LLM-based planning, and ROS 2 action mapping, will be discussed. Where practical, code snippets demonstrating API interactions will be provided within the chapter content.

### 4. Contributing

Refer to the project's main `README.md` and constitution for general contribution guidelines and standards.

## Next Steps

-   **Review `specs/004-vision-language-action-vla/spec.md`**: Understand the feature requirements.
-   **Review `specs/004-vision-language-action-vla/plan.md`**: See the detailed implementation plan.
-   **Consult `specs/004-vision-language-action-vla/research.md`**: Understand key research decisions made for this module.
