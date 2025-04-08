# System Design Task: Automated Investment System

## Problem Statement

Design a system that allows users to deposit funds into an account, which are then automatically invested into appropriate financial assets based on predefined criteria or user preferences.

## Requirements

### Functional Requirements

1.  **User Onboarding:** Allow new users to create an account.
2.  **Deposit Funds:** Users must be able to deposit money into their account through various methods (e.g., bank transfer, card payment).
3.  **Investment Strategy:** The system needs a mechanism to determine the correct assets for investment. This could be based on user risk profiles, pre-defined portfolios, or other criteria.
4.  **Automated Investment:** Once funds are deposited, the system should automatically execute trades to invest the money according to the determined strategy.
5.  **Account Viewing:** Users should be able to view their account balance, holdings, and transaction history.

### Non-Functional Requirements

1.  **Reliability:** The system must reliably process deposits and execute investments. Financial transactions must be accurate and atomic.
2.  **Scalability:** The system should handle a growing number of users and transactions.
3.  **Security:** Protect user data, financial information, and prevent unauthorized access. Ensure secure handling of transactions.
4.  **Performance:** Deposits and investment executions should occur within a reasonable timeframe. Users should experience low latency when viewing their account information.
5.  **Compliance:** The system must adhere to relevant financial regulations and reporting requirements.

## Task

1.  Describe the high-level architecture of the system.
2.  Detail the key components and their responsibilities.
3.  Explain the data models required.
4.  Discuss the technologies you would choose and justify your choices.
5.  Outline how you would address the non-functional requirements, particularly security, reliability, and scalability.
6.  Consider potential failure points and how the system would handle them.
