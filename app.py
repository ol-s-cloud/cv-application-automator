import streamlit as st
import os
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from cv_customizer import customize_cv
from job_submitter import submit_application

# Initialize session state
if 'applications' not in st.session_state:
    st.session_state.applications = []

# App title and description
st.title('CV Application Automator')
st.write('Streamline your job application process by customizing your CV and automating submissions.')

# Sidebar for configuration
with st.sidebar:
    st.header('Settings')
    
    # CV Templates
    st.subheader('CV Templates')
    template_dir = Path('templates')
    template_files = list(template_dir.glob('*.docx')) if template_dir.exists() else []
    template_names = [f.stem for f in template_files]
    
    if template_names:
        selected_template = st.selectbox('Select CV Template', template_names)
    else:
        st.warning('No templates found. Please add templates to the templates directory.')
        selected_template = None
    
    # Credentials
    st.subheader('Job Portal Credentials')
    
    # Load credentials
    credentials_file = Path('credentials.json')
    if credentials_file.exists():
        with open(credentials_file, 'r') as f:
            credentials = json.load(f)
    else:
        credentials = {}
    
    portal_names = list(credentials.keys())
    
    # Add new credentials
    new_portal = st.text_input('Add new job portal')
    if new_portal and new_portal not in portal_names:
        credentials[new_portal] = {'username': '', 'password': ''}
        portal_names.append(new_portal)
        with open(credentials_file, 'w') as f:
            json.dump(credentials, f)
    
    # Select and edit credentials
    if portal_names:
        selected_portal = st.selectbox('Select job portal', portal_names)
        if selected_portal:
            credentials[selected_portal]['username'] = st.text_input(
                f'Username for {selected_portal}', 
                value=credentials[selected_portal].get('username', ''),
                key=f'{selected_portal}_username'
            )
            credentials[selected_portal]['password'] = st.text_input(
                f'Password for {selected_portal}', 
                value=credentials[selected_portal].get('password', ''),
                type='password',
                key=f'{selected_portal}_password'
            )
            
            # Save updated credentials
            if st.button('Save credentials'):
                with open(credentials_file, 'w') as f:
                    json.dump(credentials, f)
                st.success('Credentials saved!')

# Main application form
st.header('New Job Application')

with st.form('job_application'):
    # Basic job details
    portal = st.selectbox('Job Portal/Website', portal_names if portal_names else [''])
    job_title = st.text_input('Job Title')
    company = st.text_input('Company')
    job_url = st.text_input('Job URL')
    location = st.text_input('Location')
    
    # Job description and keywords
    job_description = st.text_area('Job Description', height=200)
    keywords = st.text_input('Additional Keywords (comma separated)')
    
    # Submission options
    customize_only = st.checkbox('Customize CV only (no automatic submission)')
    
    submitted = st.form_submit_button('Process Application')

if submitted:
    try:
        if not job_title or not company:
            st.error('Job title and company are required.')
        elif not selected_template:
            st.error('Please select a CV template.')
        else:
            # Status message
            status = st.empty()
            status.info('Processing your application...')
            
            # Create a timestamped filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            cv_filename = f'{company}_{timestamp}.pdf'
            output_path = Path('output') / cv_filename
            
            # Ensure output directory exists
            os.makedirs('output', exist_ok=True)
            
            # Process keywords
            keyword_list = [k.strip() for k in keywords.split(',')] if keywords else []
            
            # Customize CV
            status.info('Customizing your CV...')
            cv_path = customize_cv(
                template_path=str(template_dir / f'{selected_template}.docx'),
                output_path=str(output_path),
                job_title=job_title,
                company=company,
                job_description=job_description,
                keywords=keyword_list
            )
            
            # Record the application
            app_record = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'company': company,
                'job_title': job_title,
                'portal': portal,
                'location': location,
                'cv_file': str(output_path),
                'status': 'CV Created'
            }
            
            # Submit application if requested
            if not customize_only and portal in credentials:
                status.info('Submitting application...')
                submission_status = submit_application(
                    portal=portal,
                    credentials=credentials[portal],
                    job_url=job_url,
                    cv_path=str(output_path),
                    job_title=job_title,
                    company=company
                )
                app_record['status'] = submission_status
            
            # Add to applications list
            st.session_state.applications.append(app_record)
            
            # Success message and download link
            status.success('Processing complete!')
            with open(output_path, 'rb') as file:
                st.download_button(
                    label='Download Customized CV',
                    data=file,
                    file_name=cv_filename,
                    mime='application/pdf'
                )
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

# Display application history
st.header('Application History')
if st.session_state.applications:
    df = pd.DataFrame(st.session_state.applications)
    st.dataframe(df)
else:
    st.info('No applications processed yet.')