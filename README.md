# One-Click Craft API Server

One-Click Craft is a professional resume and cover letter tailoring assistant that helps job seekers optimize their application materials for specific job postings. This repository contains the FastAPI backend server that powers the One-Click Craft browser extension.

## 🚀 Features

- **Job Posting Analysis**: Extracts and analyzes job posting details from various websites
- **Resume Tailoring**: Generates tailored suggestions to improve resumes for specific job applications
- **Cover Letter Generation**: Creates personalized cover letters based on job postings and resumes
- **Application Question Answering**: Helps craft effective answers to job application questions
- **Full Resume Generation**: Creates optimized resumes from scratch for specific job postings
- **Credit System**: Includes a user credit system with Stripe payment integration

## 🏗️ Architecture

### Tech Stack

- **FastAPI**: Modern, high-performance web framework for building APIs
- **MongoDB**: NoSQL database for storing user information and credits
- **Claude API**: Powers the AI capabilities using Anthropic's Claude models
- **Stripe**: Payment processing for the credit system
- **Firecrawl**: Web scraping service to extract job posting details
- **Pydantic**: Data validation and settings management

### Directory Structure

```
app/
├── config.py             # Application configuration using Pydantic
├── constants.py          # Application constants and credit packages
├── custom_exceptions.py  # Custom HTTP exceptions
├── db/                   # Database operations
│   └── database.py       # MongoDB connection and operations
├── main.py               # Application entry point and FastAPI setup
├── models/               # Pydantic models for request/response validation
│   ├── application_question.py
│   ├── cover_letter.py
│   ├── job_posting_eval.py
│   ├── payment.py
│   ├── resume_suggestions.py
│   ├── uploaded_doc.py
│   └── user.py
├── routes/               # API endpoints
│   ├── payments.py       # Stripe payment endpoints
│   ├── suggestion_generation.py # Main service endpoints
│   └── users.py          # User management endpoints
├── services/             # Business logic
│   ├── payments.py       # Stripe payment processing
│   └── suggestion_generation.py # Main AI service logic
└── utils/                # Utility functions and helpers
    ├── claude_handler/   # Claude API integration
    │   ├── claude_config_apis.py
    │   ├── claude_document_handler.py
    │   └── claude_prompts.py
    ├── data_parsing.py   # JSON response parsing
    └── firecrawl.py      # Web scraping integration
```

## 🔧 Setup and Installation

### Prerequisites

- Python 3.9+
- MongoDB
- API keys for:
  - Anthropic Claude
  - Stripe
  - Firecrawl
  - OpenAI

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```
# App Configuration
PROJECT_NAME=Resume Tailor Assistant API
VERSION=1.0.0
API_V1_STR=/api/v1

# API Keys
CLAUDE_API_KEY=your_claude_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
OPENAI_API_KEY=your_openai_api_key

# MongoDB Configuration
MONGO_URI=your_mongodb_connection_string
MONGO_DB_NAME=one_click_craft

# Stripe Configuration
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret

# CORS Configuration (for development)
ALLOWED_ORIGINS=["*"]
```

### Installation Steps

1. Clone the repository:

   ```
   git clone https://github.com/your-username/one-click-craft-server.git
   cd one-click-craft-server
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Start the server:

   ```
   uvicorn app.main:app --reload
   ```

5. The API will be available at `http://localhost:8000`

## 🔌 API Endpoints

### Health Check

- `GET /health`: Simple health check endpoint

### User Management

- `GET /api/v1/users/get-or-create?browser_id={browser_id}`: Get or create a user account

### Job Posting Evaluation

- `POST /api/v1/generation/job-posting/evaluate`: Analyze a job posting from URL or content

### Resume Tailoring

- `POST /api/v1/generation/resume-suggestions/generate`: Generate tailored resume suggestions
- `POST /api/v1/generation/resume/generate`: Generate a full tailored resume

### Cover Letter Generation

- `POST /api/v1/generation/cover-letter/generate`: Generate a tailored cover letter

### Application Questions

- `POST /api/v1/generation/application-question/answer`: Generate answers to application questions

### Payment Processing

- `POST /api/v1/payments/create-session`: Create a Stripe checkout session
- `POST /api/v1/payments/webhook`: Handle Stripe webhook events
- `GET /api/v1/payments/success`: Payment success page
- `GET /api/v1/payments/cancel`: Payment cancellation page

## 💰 Credit System

The application uses a credit-based system to manage usage:

- New users receive 10 free credits upon registration
- Additional credits can be purchased through Stripe integration
- Different features consume varying amounts of credits
- Credits are tied to a browser ID for persistent identification

## 🧠 AI Integration

The application uses Anthropic's Claude API to power its AI capabilities:

- `claude-3-5-haiku-20241022`: Used for most operations to balance performance and cost
- `claude-3-7-sonnet-20250219`: More powerful model for complex tasks

## 🔑 Authentication and Security

- Browser-based identification using a unique browser ID
- CORS protection for API endpoints
- Stripe webhook signatures for payment verification
- Credit validation for premium features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 🌐 Deployment

The service is currently deployed on Render at `https://one-click-craft-server-project.onrender.com/`.

## ⚠️ Notes

- For development, CORS is configured to allow all origins. In production, this should be restricted to specific frontend domains.
- The `.env` file should never be committed to the repository.
