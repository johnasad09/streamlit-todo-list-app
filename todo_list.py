import streamlit as st
from task import Task
from jokes import get_joke

if "task_list" not in st.session_state:
    st.session_state.task_list = []
task_list = st.session_state.task_list

if "joke" not in st.session_state:
    api_key = st.secrets["jokes_api"]["api_key"]
    st.session_state.joke = get_joke(api_key)


def add_task(task_name: str):
    task_list.append(Task(task_name))

def delete_task(idx: int):
    del task_list[idx]

def mark_done(task: Task):
    task.is_done = True

def mark_not_done(task: Task):
    task.is_done = False

# task_list = []

with st.sidebar:
    task = st.text_input("Enter a task", placeholder="e.g., Buy groceries")
    if st.button("Add Task", type="primary"):
        add_task(task)

st.info(st.session_state.joke)

total_tasks = len(task_list)
completed_tasks = sum(1 for task in task_list if task.is_done)
metric_text = f"Completed {completed_tasks} / {total_tasks} tasks"
st.metric("Task Completion", metric_text, delta=None)

st.header("Today's To-Do List", divider='violet')
# st.info(f"task_list: {task_list}")

for idx, task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    label = f"~~{task.name}~~" if task.is_done else task.name
    checked = task_col.checkbox(label, task.is_done, key=f"task_{idx}")
    if checked and not task.is_done:
        mark_done(task)
        st.rerun()
    elif not checked and task.is_done:
        mark_not_done(task)
        st.rerun()

    if delete_col.button("Delete", key=f"delete_{idx}"):
        delete_task(idx)
        st.rerun()
