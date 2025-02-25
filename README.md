# CV Application Automator

A dashboard for automatically customizing and submitting job applications.

## 🚀 Features

- **CV Customization**: Automatically tailors your CV based on job descriptions and keywords
- **Keyword Extraction**: Uses NLP to identify important keywords from job descriptions
- **Specialized Templates**: Includes templates for various technology roles
- **Application Tracking**: Keeps a history of all applications submitted
- **PDF Generation**: Creates polished PDFs ready for submission

## 📋 Version 1.0 (Current)

The current version focuses on CV customization and generation, with a roadmap for future enhancements:

- ✅ CV customization based on job descriptions
- ✅ Keyword extraction and matching
- ✅ Multiple specialized templates
- ✅ User-friendly interface
- ✅ PDF generation and download

See our [complete roadmap](docs/ROADMAP.md) for future development plans.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for automated submissions in future versions)
- ChromeDriver (for Selenium in future versions)

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
   - We provide placeholder templates for 5 specialized roles
   - See [template documentation](docs/TEMPLATES.md) for details

### Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Configure your settings in the sidebar
3. Fill in the job details and description
4. Click "Process Application"
5. Download your customized CV

## 📄 Documentation

- [Parameter Configuration](docs/PARAMETERS.md) - Details on all configurable options
- [CV Templates Guide](docs/TEMPLATES.md) - Information on included templates and creating your own
- [Development Roadmap](docs/ROADMAP.md) - Future plans and features

## 🔮 Future Plans (See Roadmap)

- **Version 2.0**: Enhanced CV customization with machine learning
- **Version 3.0**: Full application automation with job portal integration
- **Version 4.0**: Complete career management suite

## 🚩 Specialized Templates

The system includes templates for these specialized roles:
1. D365 Functional Consultant
2. D365 Technical Consultant
3. Data and Systems Architect
4. Data Analytics and Reporting
5. ML Research and Developer

## 💻 Running on Streamlit

This application is built with Streamlit, which creates a local web server with a user-friendly interface. To make it accessible:

### Local Network Access

```bash
streamlit run app.py -- --server.headless=true --server.port=8501 --server.address=0.0.0.0
```

### Cloud Deployment

For public access, you can deploy to [Streamlit Cloud](https://streamlit.io/cloud).

## 🤝 Contributing

We welcome contributions to improve the CV Application Automator. Please see our roadmap for areas where help is needed.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔒 Security Note

Your credentials are stored locally in a JSON file. For better security, consider using environment variables or a secure credential manager.

## 📊 Demo

Start the application and navigate to the local Streamlit server to see a live demo of the CV customization process.
