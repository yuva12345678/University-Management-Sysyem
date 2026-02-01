# University Management System
import streamlit
import streamlit as st

class person:
    def __init__(self, branch: str, name: str):
        self.branch = branch
        self.name = name

    def __str__(self) -> str:
        return f"Name: {self.name} | Branch: {self.branch}"

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(branch, name)
        self.rollno = rollno

    def __str__(self) -> str:
        return f"Rollno: {self.rollno} | {super().__str__()}"

class teacher(person):
    def __init__(self, branch, name, subject):
        super().__init__(branch, name)
        self.subject = subject

    def __str__(self) -> str:
        return f"subject: {self.subject} | {super().__str__()}"
    
class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, s: student):
        self.students.append(s)

    def add_teacher(self, t: teacher):
        self.teachers.append(t)

    # Frontend code
st.set_page_config(page_title = "Univerity Management System",
                    layout = "centered")

st.title("🏫 Univerity Management System")

# Creating the Menu Bar
menu_choice = st.sidebar.radio(
    "Select Action",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display students",
        "Display Teachers",
        "Display Colleges"
    )
)

if "colleges" not in st.session_state:
    st.session_state.colleges = []

def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname == cname), None)

# Created new college
if menu_choice == "Create College":
    cname = st.text_input("Enter new college name")
    if st.button("Create"):
        if not cname:
            st.error("College name is empty, plz write some college name")
        elif find_college(cname):
            st.warning("This college already exist")
        else:
            st.session_state.colleges.append(college(cname))
            st.success(f"Created College successfully: {cname}")

elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please Create college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])

        roll = st.text_input("Roll Number")
        sname = st.text_input("Student Name")
        branch = st.text_input("Branch e.g. CSE")

        if st.button("Add Student"):
            if not(roll and sname and branch):
                st.error("All fields are mandatory")
            else:
                clg = find_college(clgname)
                clg.add_student(student(roll, sname, branch))
                st.success("Student added successfully")

elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please Create college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])

        subj = st.text_input("Subject")
        tname = st.text_input("Teacher Name")
        branch = st.text_input("Branch e.g. CSE")

        if st.button("Add Teacher"):
            if not(subj and tname and branch):
                st.error("All fields are mandatory")
            else:
                clg = find_college(clgname)
                clg.add_teacher(teacher(branch, tname, subj))
                st.success("Teacher added successfully")

elif menu_choice == "Display students":
    if not st.session_state.colleges:
        st.info("Please Create college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])

        st.subheader(f"List of Students from {clgname}")
        clg = find_college(clgname)
        if clg.students:
            for i, s in enumerate(clg.students, 1):
                st.write(f"{i} : {s}")
        else:
            st.warning("No Student admitted in this college")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please Create college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])
        st.subheader(f"List of Teachers from {clgname}")
        clg = find_college(clgname)
        if clg.teachers:
            for i, t in enumerate(clg.teachers, 1):
                st.write(f"{i} : {t}")
        else:
            st.warning("No Teacher in this college")

elif menu_choice == "Display Colleges":
    st.subheader("All colleges list")
    if not st.session_state.colleges:
        st.info("No college added")
    else:
        for i, c in enumerate(st.session_state.colleges, 1):
                st.write(f"{i} : {c.cname}")