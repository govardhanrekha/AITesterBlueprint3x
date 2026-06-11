AI-Powered Test Plan Generator using Ollama
📌 Project Overview

This project demonstrates how a Local Large Language Model (LLM) running through Ollama can be used to automatically generate a comprehensive Software Test Plan from a Product Requirements Document (PRD).

Traditionally, QA Engineers spend significant time analyzing requirements and preparing Test Plans manually. This project showcases how AI can assist the QA process by generating structured Test Plan documents based on application requirements.

The project uses a PRD of the RESTful Booker API as input and generates a detailed Test Plan covering testing scope, objectives, strategy, risks, assumptions, entry/exit criteria, and deliverables.

🎯 Objectives
Automate Test Plan creation using AI.
Reduce manual documentation effort.
Demonstrate AI-assisted QA activities.
Explore local LLM capabilities using Ollama.
Showcase Prompt Engineering for software testing.
🛠️ Technologies Used
Technology	Purpose
Ollama	Local LLM Runtime
Llama 3 / Mistral	AI Model
VS Code	Development Environment
Microsoft Word	Test Plan Documentation
Git & GitHub	Version Control
RESTful Booker API PRD	Input Requirement Document
📂 Project_1_TestPlan_Generator_Ollama
│
│
├── README.md
│
├── PRD
│   └── RestfulBooker_PRD.docx
│
├── Prompts
│   └── RICE-POT-TestPlan-Prompt.txt
│
├── Generated_Output
│   └── Test_Plan_for_RESTful_Booker_API.docx
│
└── Screenshots
    └── Ollama_Snapshot_1.png
    Ollama_Snapshot_2.png
    Ollama_Snapshot_3.png

🔄 Workflow
PRD Document
      ↓
Prompt Engineering
      ↓
Ollama Local LLM
      ↓
Requirement Analysis
      ↓
Test Plan Generation
      ↓
Review & Validation
      ↓
Final Test Plan Document
📋 Input

The system accepts:

Product Requirement Document (PRD)
Functional Requirements
Business Rules
API Specifications
User Stories (optional)

Example Input:

RESTful Booker API PRD
📄 Generated Output

The AI-generated Test Plan includes:

1. Test Plan Identifier
Project Name
Version
Author
2. Test Objectives
Testing goals
Quality objectives
3. Scope
Features to be tested
Features not to be tested
4. Test Strategy
Functional Testing
API Testing
Integration Testing
Regression Testing
5. Test Environment
6. Entry Criteria
7. Exit Criteria
8. Risks and Mitigation
9. Assumptions
10. Deliverables
11. Resource Requirements
12. Test Schedule
🚀 How to Run
Step 1: Install Ollama

Download and install Ollama from:

https://ollama.com

Step 2: Pull an LLM Model
ollama pull llama3

or

ollama pull mistral
Step 3: Open Ollama

Start the Ollama server.

Step 4: Load the PRD

Copy the PRD content into the prompt.

Step 5: Execute Prompt

Use the prepared prompt file:

RICE-POT-TestPlan-Prompt.txt
Step 6: Generate Test Plan

The LLM analyzes the requirements and generates a structured Test Plan.

Step 7: Review Output

Validate the generated Test Plan and save it as a Word or PDF document.

💡 Key QA Concepts Demonstrated
Requirement Analysis
Test Planning
Risk Assessment
Test Strategy Design
AI-assisted Testing
Prompt Engineering
Documentation Automation
📸 Sample Output

The repository contains:

Input PRD
Prompt Template
Generated Test Plan
Output Screenshots
🔍 Benefits
Faster Test Plan creation
Consistent documentation
Reduced manual effort
Improved productivity
Demonstrates practical AI adoption in QA
⚠️ Limitations
Generated content requires QA review.
Output quality depends on prompt quality.
Complex business rules may require manual refinement.
AI-generated plans should not replace tester judgment.
🔮 Future Enhancements
Test Case Generation from PRD
Test Scenario Generation
Export to Excel
Streamlit User Interface
Retrieval-Augmented Generation (RAG)
Multi-Model Support (Llama, Mistral, Gemma)
Jira Integration
Automated Traceability Matrix Generation
👩‍💻 Author

Rekha Govardhan
Senior QA Engineer | Manual Testing | API Testing | AI-Assisted Testing