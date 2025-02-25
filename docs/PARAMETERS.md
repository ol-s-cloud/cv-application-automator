# Configuration Parameters

This document outlines all configurable parameters and options for the CV Application Automator.

## CV Templates

Templates should be in DOCX format and placed in the `templates/` directory.

### Placeholder Variables

The following placeholders can be used in your CV templates:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[JOB_TITLE]` | Will be replaced with the job title | "Senior D365 Consultant" |
| `[COMPANY]` | Will be replaced with the company name | "Microsoft" |
| `[DATE]` | Will be replaced with the current date | "February 25, 2025" |

### Keyword Highlighting

For skills and qualifications sections, the system will automatically identify matches between the job description keywords and your CV content. To optimize this matching:

1. Create distinct sections for Skills, Technical Competencies, and Professional Experience
2. Include multiple variations of key skills (e.g., "Microsoft Dynamics 365", "D365", "Dynamics CRM")
3. Group related skills to increase matching probability

## Job Portal Credentials

The application securely stores credentials for job portals locally in `credentials.json`. Currently supported portals:

- LinkedIn
- Indeed
- Glassdoor

For each portal, provide:
- Username (typically email)
- Password

## Job Description Parameters

When entering a job description, the following aspects are analyzed:

| Parameter | Description |
|-----------|-------------|
| Required Skills | Technical skills and competencies explicitly mentioned as required |
| Preferred Skills | Technical skills mentioned as preferred or desired |
| Experience Level | Years of experience and seniority level |
| Industry Keywords | Industry-specific terminology and buzzwords |

## Additional Keywords

You can manually add keywords that might not be in the job description but are relevant to your application. These are entered as comma-separated values in the "Additional Keywords" field.

## Application Customization Options

| Option | Description | Default |
|--------|-------------|---------|
| `Customize CV only` | Generate a custom CV without submitting the application | Unchecked |
| `Highlight matched skills` | Visually highlight skills that match job requirements | Checked |
| `Include cover letter` | Generate a matching cover letter (future feature) | Unchecked |

## Template Specializations

The application comes with specialized templates for different roles:

1. **D365 Functional Consultant**
   - Emphasizes business process knowledge
   - Highlights module-specific expertise (Finance, Supply Chain, etc.)
   - Focuses on implementation experience

2. **D365 Technical Consultant**
   - Emphasizes development skills and customizations
   - Highlights integrations and extensions
   - Focuses on technical architecture

3. **Data and Systems Architect**
   - Emphasizes system design and enterprise architecture
   - Highlights data modeling and integration patterns
   - Focuses on large-scale implementations

4. **Data Analytics and Reporting**
   - Emphasizes data analysis skills
   - Highlights reporting tools and visualization expertise
   - Focuses on business intelligence implementations

5. **ML Research and Developer**
   - Emphasizes machine learning algorithms and models
   - Highlights research experience and publications
   - Focuses on model development and deployment
