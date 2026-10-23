# Project 7 Report: Automated Testing with Pytest

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Pytest Version & Framework:**`, `**GitHub Repository URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information
- **Name:** Kay
- **MMDT ID:** MMDT051
---

## Section 1: Test Suite Configuration
- **Pytest Version & Framework:** Pytest 8.3.3 with pytest-cov and Python 3.11 test environment
- **Total Test Cases Written:** 33 test cases across the calculator, validator, and student manager modules
- **Measured Code Coverage (%):** 96%
- **Key Fixtures Implemented:** valid_registration_data, sample_student, empty_manager, and populated_manager for reusable setup and stateful testing

---

## Section 2: Test Case Design & Boundary Analysis
- **Calculator Boundary & Edge Cases:** Tested empty lists, valid numeric averages, negative values, prime/non-prime edge cases like 0, 1, 2, 3, 5, and boundary factorial and power inputs, plus invalid type rejection and zero-to-negative-power errors.
- **Validator Exception Scenarios:** Covered missing registration fields, invalid email formats, whitespace issues, weak passwords, invalid usernames, and age limits with explicit custom exception assertions using pytest.raises.
- **Student Manager State Transitions:** Verified student creation, duplicate ID rejection, grade updates, GPA recalculation, top-performer ordering, minimum GPA filtering, and safe removal behavior with KeyError checks.

---

## Section 3: Local Verification & Feature Checklist
*Check the test modules and features you successfully implemented and verified locally by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Module 1: Calculator Unit Tests with Boundary & Type Assertions (`test_calculator.py`)
- [x] Parameterized Testing with `@pytest.mark.parametrize` for Multiple Input Scenarios
- [x] Module 2: Data Validator Tests with Custom Exception Assertions (`pytest.raises`)
- [x] Module 3: Student Management System Tests with State Mutation & CRUD Verification
- [x] Reusable Pytest Fixtures in `conftest.py` for Modular Test Setup
- [x] Mutation Testing & Bug Detection Verification (Catching Hidden Mutants)
- [x] Code Coverage Analysis with `pytest-cov` (>= 85% Coverage)

---

## Section 4: Deployed and Presentation Information
- **GitHub Repository URL:** https://github.com/gloryprospect39-blip/Test_MMDT_MLAT_Project07
- **Video Presentation Link:** https://drive.google.com/drive/folders/1uaPMZveDRk3ZznSX0SZNF4Tt3Xf-gz3t?usp=drive_link

---

## Section 5: Discussion
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **Explain why a test suite that passes 100% does not guarantee code correctness, and how mutation testing or evaluating tests against buggy code verifies test suite effectiveness.**
    A test suite can pass on the current implementation while still missing important edge cases, because it only checks the behaviors we explicitly encoded. Mutation testing improves confidence by introducing small faults such as a wrong comparison, skipped validation, or a missing exception check; if the suite still passes, it is not actually detecting the bug. This process shows whether the tests are strong enough to catch realistic regressions instead of merely confirming the original code path.
- **Compare classical unit and integration testing in software engineering with modern AI engineering evaluation (e.g., LLM benchmarks, unit testing AI agents/tool calls, and Process Reward Models / LLM-as-a-judge).**
    Classical unit and integration testing validate deterministic software behavior across modules, while modern AI engineering evaluates probabilistic systems with benchmark suites, task-specific unit checks, and agent workflows. For LLMs, we measure accuracy, reasoning quality, tool use correctness, and reliability under varied prompts, while process reward models and LLM-as-a-judge systems score intermediate decisions or rubric-based responses. Both approaches share the same principle: test the system against expected behaviors and hidden failure modes, not only the happy path.
