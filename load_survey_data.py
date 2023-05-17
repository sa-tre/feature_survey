from datetime import datetime 
import numpy as np
import pandas as pd
# Requires openpyxl for read_excel
from pathlib import Path
import re
import sys

this = sys.modules[__name__]

this.RANKING = [
    # Lowest rank, comment out the following to treat this as NaN
    "No opinion",
    "Not important",
    "Nice to have",
    "Important",
    "Essential",
]

this.headers = {
    "Definitions": "SECTION",
    "Contact us": "SECTION",
    "About you": "SECTION",
    "1. Role": "TEXT",
    "2. Institution": "TEXT",
    "Technical features": "SECTION",
    "3. Admin control over data movement": "SECTION",
    "3.1.a. Ingress (data entering the environment)": "RANKING",
    "3.2.a. Egress (data leaving the environment)": "RANKING",
    "3.3.a. Streaming ingress (trusted sources can move data in without review for each event)": "RANKING",
    "4. User authentication": "SECTION",
    "4.1.a. Multi-factor authentication": "RANKING",
    "4.2.a. Federated authentication / single sign-on": "RANKING",
    "5. Network connectivity": "SECTION",
    "5.1.a. Configurable connectivity between workspaces": "RANKING",
    "5.2.a. Configurable connectivity between a project and resources outside the TRE": "RANKING",
    "5.a. Any other comments on network connectivity?": "TEXT",
    "6. Ability to forbid copy and paste": "SECTION",
    "6.1.a. From inside to outside": "RANKING",
    "6.2.a. From outside to inside": "RANKING",
    "7. User experience": "SECTION",
    "7.1.a. Windows desktop": "RANKING",
    "7.2.a. Linux desktop": "RANKING",
    "7.3.a. Command line": "RANKING",
    "7.4.a. Non-desktop interfaces e.g. JupyterLab, webapps": "RANKING",
    "7.a. Which non-desktop interfaces are important to you?": "TEXT",
    "8. Programming language support": "SECTION",
    "8.1.a. Support for common data science, statistics, ML programming languages (e.g. Python, R)": "RANKING",
    "8.a. Which programming languages are important to you?": "TEXT",
    "9. Enable users to install packages from selected external repositories (e.g. PyPI, CRAN, Conda, Maven)": "SECTION",
    "9.1.a. Any package": "RANKING",
    "9.2.a. A curated subset of packages": "RANKING",
    "9.a. Which repositories are important to you?": "TEXT",
    "10. Commercially licenced software": "SECTION",
    "10.1.a. Ability to use specific commercial software": "RANKING",
    "10.2.a. Further, software that connects to an external licensing server (e.g. SAS)": "RANKING",
    "10.a. Which commercially licenced software is important to you?": "TEXT",
    "11. Containerisation": "SECTION",
    "11.1.a. Support for running containers (e.g. Docker, Podman, Apptainer)": "RANKING",
    "12. Logging": "SECTION",
    "12.1.a. User actions inside the TRE": "RANKING",
    "12.2.a. Network connection attempts": "RANKING",
    "12.3.a. Infrastructure actions (e.g. adding compute, modifying network configuration)": "RANKING",
    "12.4.a. Data access": "RANKING",
    "12.5.a. Real time user and data access logs": "RANKING",
    "13. Automatic updates": "SECTION",
    "13.1.a. Software installed on workspaces": "RANKING",
    "13.2.a. User infrastructure (e.g. remote desktop portal, databases, webapps)": "RANKING",
    "13.3.a. Management infrastructure (e.g. logging, configuration management controller)": "RANKING",
    "13.4.a. Anti-virus/malware": "RANKING",
    "14. Compliance checking": "SECTION",
    "14.1.a. Vulnerability/security scanning of infrastructure": "RANKING",
    "14.2.a. Machine/resource configuration": "RANKING",
    "15. Automatic backup": "SECTION",
    "15.1.a. Input data": "RANKING",
    "15.2.a. User data (e.g. working files)": "RANKING",
    "15.3.a. Workspaces": "RANKING",
    "16. Customisable compute resources": "SECTION",
    "16.1.a. Ability to scale compute (CPU, memory)": "RANKING",
    "16.2.a. Accelerators such as GPUs": "RANKING",
    "17. Additional compute beyond workspaces": "SECTION",
    "17.1.a. HPC-like resources (i.e. performant hardware, job queue)": "RANKING",
    "17.2.a. Big data and data analytics tools (e.g. Spark, Hadoop)": "RANKING",
    "17.3.a. Integrating with cloud-native managed services (e.g. SageMaker, Athena, Azure ML, Databricks)": "RANKING",
    "18. Collaborative/shared tools": "SECTION",
    "18.1.a. Git server (e.g. GitLab/Gitea)": "RANKING",
    "18.2.a. Document writing (e.g. CodiMD)": "RANKING",
    "18.3.a. Databases (e.g. PostgreSQL, MSSQL, MongoDB)": "RANKING",
    "18.4.a. Collaborative coding, visualisation (e.g. Jupyter)": "RANKING",
    "19. Limiting direct access to data/code": "SECTION",
    "19.1.a. Users have no direct access to data, submit pipelines or batch jobs, only results are returned": "RANKING",
    "19.2.a. TRE admins don't have access to researcher’s analysis code": "RANKING",
    "20. Reproducible deployments": "SECTION",
    "20.1.a. Reproducible TRE deployments (e.g. through infrastructure as code)": "RANKING",
    "21. Additional technical features: describe other technical features we may have missed and how important they are.": "TEXT",
    "22. Additional comments: share any other thoughts and feelings on technical features.": "TEXT",
    "Policies and processes": "SECTION",
    "23. Sensitivity tiering": "SECTION",
    "23.1.a. Support data of different levels of sensitivity": "RANKING",
    "23.2.a. Preset security configurations which can be applied to multiple projects (e.g. a tiered system)": "RANKING",
    "23.a. Are there sensitivity systems that you think are important or use?": "TEXT",
    "24. Which aspects of governance would it be important or useful to standardise": "SECTION",
    "24.1.a. Terms of use": "RANKING",
    "24.2.a. Safe people training users": "RANKING",
    "24.3.a. Safe people training admins": "RANKING",
    "24.4.a. Data ingress and egress processes": "RANKING",
    "24.5.a. Roles and responsibilities": "RANKING",
    "24.a. Additional aspects of governance: Briefly describe other aspects of governance we may have missed and how important they are.": "TEXT",
    "25. Additional comments: share any other thoughts and feelings on policies and processes.": "TEXT",
    "CompletionDate": "DATE",
}

def to_ranking(c):
    return pd.Categorical(c, this.RANKING, ordered=True)

def convert_date_and_ranking(df, df_orig, headers, format=None):
    for (c, t) in headers.items():
        if t == "DATE":
            df[c] = pd.to_datetime(df_orig[c], format=format, errors='coerce')
        if t == "RANKING":
            df[c] = to_ranking(df_orig[c])
    return df

def load_data(spreadsheet, date_format):
    df_results = pd.read_excel(spreadsheet)
    df_results_mod = df_results.copy(deep=True)
    return convert_date_and_ranking(df_results_mod, df_results, this.headers, date_format)