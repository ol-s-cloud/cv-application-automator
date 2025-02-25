# CV Application Automator

A dashboard for automatically customizing and submitting job applications.

## Features

- **CV Customization**: Automatically tailors your CV based on job descriptions and keywords
- **Keyword Extraction**: Uses NLP to identify important keywords from job descriptions
- **Automated Submissions**: Submits applications to popular job portals (LinkedIn, Indeed, Glassdoor)
- **Application Tracking**: Keeps a history of all applications submitted
- **Credential Management**: Securely stores your job portal credentials

## How It Works

1. **Input Job Details**: Enter job information, including title, company, and description
2. **CV Customization**: The system extracts keywords from the job description and customizes your CV
3. **Automated Submission**: Optionally submits the application directly to the job portal
4. **Application Tracking**: Records all submissions for future reference

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for automated submissions)
- ChromeDriver (for Selenium)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/ol-s-cloud/cv-application-automator.git
   cd cv-application-automator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create necessary directories:
   ```
   mkdir -p templates output
   ```

4. Add your CV templates to the `templates` directory in DOCX format.
   - Use placeholders like `[JOB_TITLE]` and `[COMPANY]` in your templates
   - Organize skills sections to easily match with job keywords

### Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Configure your job portal credentials in the sidebar
3. Select a CV template
4. Fill in the job details and description
5. Choose whether to just customize your CV or also submit the application
6. Click "Process Application"
7. Download your customized CV and/or check the submission status

## CV Templates

Create your CV templates in DOCX format with the following features:

- Use `[JOB_TITLE]` and `[COMPANY]` placeholders where you want these to be inserted
- Organize your skills and experience sections to make keyword matching effective
- Include variations of common skills to increase matching probability

## Security Considerations

- Credentials are stored locally in a `credentials.json` file
- For better security, consider encrypting this file or using environment variables
- The application runs entirely on your local machine

## Customization Options

You can extend the functionality by:

1. Adding support for more job portals in `job_submitter.py`
2. Enhancing the CV customization logic in `cv_customizer.py`
3. Adding more advanced tracking and analytics features

## Troubleshooting

- If automated submissions fail, check that the selectors in `job_submitter.py` match the current website design
- Job portal websites change frequently, so the automation scripts may need updates
- For security reasons, some sites may block automated submissions

## Limitations

- Automated job submissions might not work on all portals due to CAPTCHA or other security measures
- Some job applications require custom fields that cannot be automated
- Job portal websites change their layouts frequently, which may break the automation