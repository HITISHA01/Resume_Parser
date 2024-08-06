# Prompt

Write a python script for an tool designed to process resumes submitted in various formats, including PDF files, Word documents, Excel spreadsheets, and accessible URLs. Your primary task is to extract and organize essential information from these resumes and present it in a structured JSON format. Give actual implementation of all the parsing methods. Please follow the detailed instructions below for handling the input and formatting the output:

## Instructions

### 1. Resume Submission

**Formats Accepted:** You can process resumes provided in the following formats:

- **PDF Files:** Attach the resume as a PDF document.
- **Word Documents:** Attach the resume as a Microsoft Word (.docx) file.
- **URLs:** Provide a URL where the resume can be accessed. Ensure that the URL is publicly accessible or includes necessary credentials for access.

### 2. Processing Requirements

Upon receiving the resume in any of the specified formats, you will extract and organize the following information:

- **Personal Information:**
  - Full Name
  - Contact Details: Email Address, Phone Number
  - Address

- **Professional Summary:** A concise overview of the candidate’s professional background and career objectives.

- **Experience:** A detailed list of previous job positions, including:
  - Job Title
  - Company Name
  - Location
  - Employment Dates (Start Date - End Date)
  - Key Responsibilities and Achievements

- **Education:** Information about the candidate’s educational background, including:
  - Degree
  - Institution Name
  - Location
  - Dates Attended (Start Date - End Date)

- **Skills:** A list of relevant skills possessed by the candidate.

- **Certifications:** Details of any certifications, including:
  - Certification Title
  - Issuing Organization
  - Dates (Issue Date - Expiration Date)

- **Languages:** Information about languages spoken, including:
  - Language
  - Proficiency Level (e.g., Fluent, Conversational)

### 3. JSON Output Format

After processing the resume, provide the extracted information in the following JSON format:

```json
{
  "personal_information": {
    "name": "[Full Name]",
    "contact": {
      "email": "[Email Address]",
      "phone": "[Phone Number]"
    },
    "address": "[Address]"
  },
  "summary": "[Brief Professional Summary]",
  "experience": [
    {
      "job_title": "[Job Title]",
      "company": "[Company Name]",
      "location": "[Location]",
      "dates": "[Start Date - End Date]",
      "responsibilities": "[Responsibilities and Achievements]"
    }
    // Additional job experiences as needed
  ],
  "education": [
    {
      "degree": "[Degree]",
      "institution": "[Institution Name]",
      "location": "[Location]",
      "dates": "[Start Date - End Date]"
    }
    // Additional educational qualifications as needed
  ],
  "skills": [
    "[Skill 1]",
    "[Skill 2]",
    "[Skill 3]"
    // Additional skills as needed
  ],
  "certifications": [
    {
      "title": "[Certification Title]",
      "issuing_organization": "[Organization Name]",
      "dates": "[Issue Date - Expiration Date]"
    }
    // Additional certifications as needed
  ],
  "languages": [
    {
      "language": "[Language]",
      "proficiency": "[Proficiency Level]"
    }
    // Additional languages as needed
  ]
}




