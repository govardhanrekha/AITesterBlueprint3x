AI-Powered Test Case Generator using Ollama
📌 Project Overview

This project demonstrates how a Local Large Language Model (LLM) running through Ollama can be used to automatically generate comprehensive software test cases from a Product Requirement Document (PRD).

Traditionally, QA Engineers spend significant effort analyzing requirements and manually creating test scenarios and test cases. This project showcases how AI can accelerate the test design process by generating structured test cases with functional, negative, boundary, validation, security, and API coverage.

The project uses the RESTful Booker API PRD as input and generates a complete set of test cases covering authentication, CRUD operations, validation, security, performance, integration, and regression testing.

🎯 Objectives
Automate Test Case creation using AI
Reduce manual test design effort
Improve requirement coverage
Demonstrate AI-assisted testing practices
Explore Prompt Engineering for QA activities
Generate reusable test assets
🛠️ Technologies Used
Technology	Purpose
Ollama	Local LLM Runtime
Llama 3 / Mistral	AI Model
VS Code	Development Environment
Microsoft Excel	Test Case Documentation
Git & GitHub	Version Control
RESTful Booker API PRD	Input Requirement Document
📂 Project Structure
Project_2_AI_TestCase_Generator_Ollama
│
├── README.md
├── PRD
│   └── Restful_Booker_PRD.docx
│
├── Prompt
│   └── RICE_POT_TestCase_Generation_Prompt.txt
│
├── Generated_Output
│   └── Restful_Booker_TestCases.xlsx
│
└── Screenshots
    ├── Prompt Snapshot.png
    ├── Result Snapshot.png
    

🔄 Workflow
PRD Document
      ↓
Requirement Analysis
      ↓
RICE-POT Prompt
      ↓
Ollama Local LLM
      ↓
Test Scenario Generation
      ↓
Test Case Generation
      ↓
QA Review & Refinement
      ↓
Final Test Case Repository
📄 Input

The system accepts:

Product Requirement Document (PRD)
Functional Requirements
Business Rules
API Specifications
Validation Rules
User Stories
Example Input
RESTful Booker API PRD
📋 Generated Output

The AI-generated output includes:

Test Scenarios
Functional Test Cases
Positive Test Cases
Negative Test Cases
Boundary Value Test Cases
Validation Test Cases
Error Handling Test Cases
Security Test Cases
API Validation Test Cases
Integration Test Cases
Regression Test Cases
📊 Test Coverage Summary
Area	Test Cases
Authentication	TC_001 – TC_005
Create Booking	TC_006 – TC_015
Get Booking	TC_016 – TC_022
Update Booking	TC_023 – TC_027
Partial Update	TC_028 – TC_030
Delete Booking	TC_031 – TC_035
Data Validation	TC_036 – TC_039
Security Testing	TC_040 – TC_042
Performance & Load Testing	TC_043 – TC_045
Concurrency Testing	TC_046
Integration Testing	TC_047
Rate Limiting Testing	TC_048
Compatibility Testing	TC_049
Regression Testing	TC_050

Total Test Cases Generated: 50

💡 QA Concepts Demonstrated
Requirement Analysis
Test Scenario Design
Test Case Design
Boundary Value Analysis
Equivalence Partitioning
Negative Testing
API Testing
Security Testing
Performance Testing
Regression Testing
Prompt Engineering
AI-Assisted Testing
🚀 Benefits
Faster Test Case creation
Improved requirement coverage
Consistent documentation
Reduced manual effort
Better productivity
Reusable QA assets
Practical application of AI in testing
⚠️ Limitations
Generated test cases require QA review
Output quality depends on prompt quality
Complex business rules may require refinement
AI-generated results should supplement tester expertise
🔮 Future Enhancements
AI Test Data Generator
AI API Test Script Generator
AI Traceability Matrix Generator
Streamlit UI Integration
RAG-based Requirement Analysis
Jira Integration
Automated Test Case Prioritization
Multi-Model Support
📸 Screenshots
Ollama Prompt Execution

Add screenshots showing:

Prompt execution
Generated test cases
Excel export output
👩‍💻 Author

Rekha Govardhan

Senior QA Engineer | Manual Testing | API Testing | AI-Assisted Testing

⭐ Key Highlights
Local AI Solution (No API Cost)
AI-Driven Test Design
Prompt Engineering for QA
RESTful Booker API Use Case
50 Test Cases Generated
GitHub Portfolio Project
Demonstrates AI in Software Testing