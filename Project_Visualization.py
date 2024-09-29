import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set_theme(style="whitegrid")


def load_and_clean_csv(file_path):
    df = pd.read_csv(file_path)
    df_cleaned = df.rename(columns={
        'Unnamed: 0': 'Student Name',
        'Unnamed: 1': 'Project Categories',
        'Unnamed: 3': 'Project Name',
        'Unnamed: 4': 'Group Project',
        'Unnamed: 5': 'Clone Project',
        'Unnamed: 6': 'Technologies Used'
    }).drop([0, 1, 2], axis=0)
    df_cleaned = df_cleaned.reset_index(drop=True)
    return df_cleaned


def plot_project_categories(df_cleaned):
    category_counts = df_cleaned['Project Categories'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
    plt.title('Project Count by Category', fontsize=20, fontweight='bold', color='#333')
    plt.xlabel('Project Categories', fontsize=14)
    plt.ylabel('Number of Projects', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt.gcf())

def plot_clone_projects(df_cleaned):
    clone_counts = df_cleaned['Clone Project'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=clone_counts.index, y=clone_counts.values, palette='coolwarm')
    plt.title('Clone Projects vs. Unique Projects', fontsize=20, fontweight='bold', color='#333')
    plt.xlabel('Clone Project', fontsize=14)
    plt.ylabel('Number of Projects', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt.gcf())


def plot_group_projects(df_cleaned):
    group_counts = df_cleaned['Group Project'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=group_counts.index, y=group_counts.values, palette='Set2')
    plt.title('Group Projects vs. Individual Projects', fontsize=20, fontweight='bold', color='#333')
    plt.xlabel('Group Project', fontsize=14)
    plt.ylabel('Number of Projects', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt.gcf())


def plot_technologies_used(df_cleaned):
    technologies = df_cleaned['Technologies Used'].dropna().str.split(',').explode()
    tech_counts = technologies.value_counts()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=tech_counts.index, y=tech_counts.values, palette='magma')
    plt.title('Technologies Used in Projects', fontsize=20, fontweight='bold', color='#333')
    plt.xlabel('Technologies', fontsize=14)
    plt.ylabel('Number of Projects', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt.gcf())


st.title("Project Data Analysis")


file_path = "sample.csv"


df_cleaned = load_and_clean_csv(file_path)


st.subheader("Raw Data")
st.dataframe(df_cleaned)


st.subheader("Project Count by Category")
plot_project_categories(df_cleaned)

st.subheader("Clone Projects vs. Unique Projects")
plot_clone_projects(df_cleaned)

st.subheader("Group Projects vs. Individual Projects")
plot_group_projects(df_cleaned)

st.subheader("Technologies Used in Projects")
plot_technologies_used(df_cleaned)
