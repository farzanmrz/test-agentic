## 🧱 PHASE 1 — SYSTEM FOUNDATIONS (Week 1-2)

### ✅ 1. **FastAPI Backend Setup**

* Create a Conda environment - Done 
* Install FastAPI + Uvicorn
* Create a `main.py` app with a `/ping` route to confirm backend is working

---

### ✅ 2. **Excel Upload & Preview Endpoint**

* Create a `/upload-excel` endpoint in FastAPI
* Accept `.xlsx` file from frontend
* Use `pandas` to read it
* Return a small preview of the DataFrame (`.head()`) as JSON

---

### ✅ 3. **Frontend Setup with React**

* Create React app using Vite
* Build a basic UI with:

  * File input
  * Header row index input
  * `drop_na_rows` and `drop_na_cols` checkboxes
  * Submit button

---

### ✅ 4. **Connect Frontend ↔ Backend**

* Send uploaded Excel + config as `FormData` from React to FastAPI
* Receive and display the JSON DataFrame preview in the UI
* Display raw table using HTML or a table component

---

## 🧱 PHASE 2 — TEMPLATE & WORKFLOW STRUCTURE (Week 3)

### ✅ 5. **Template Naming**

* Input box for `template_name`
* On change, check backend for duplicates via `/template/check-name`
* Save selected name in frontend state

---

### ✅ 6. **Save Excel Reader Config Locally**

* Combine:

  * `template_name`
  * Excel reader config: `header_index`, drop NAs
  * File (base64 or file object)
* Save in a structured `templateState` object (e.g., `ExcelReaderConfig`)

---

## 🧱 PHASE 3 — INTRODUCE VISUAL WORKFLOW (Week 4)

### ✅ 7. **React Flow Integration**

* Install and initialize React Flow
* Add a canvas and create the first node: `ExcelReader`
* Use internal state (from Step 6) to populate node config
* Add placeholder `RowFilter` and `EmailSender` nodes

---

### ✅ 8. **Graph JSON & Submission**

* On “Run Flow”, serialize `nodes` + `edges` into JSON
* Send JSON to `/execute-flow` endpoint in FastAPI
* Backend logs or returns mocked execution result

---

## 🧱 PHASE 4 — MOCKED EXECUTION & CLEANUP (Week 5+)

### ✅ 9. **Backend: Parse & Mock Flow**

* Parse received graph in `/execute-flow`
* Log node execution order
* Return success/failure JSON

---

### ✅ 10. **Display Results in Frontend**

* Show backend result (mocked “email sent”)
* Show debug log or notification
* Prepare to save entire template/workflow (localStorage or file)

---

## 🚧 Future Enhancements (Beyond MVP)

| Future Feature                           | Description |
| ---------------------------------------- | ----------- |
| Real Excel parsing & row filtering logic |             |
| Real email sending with SMTP             |             |
| Save template/workflow in DB             |             |
| Login & auth (e.g., Clerk or Supabase)   |             |
| Cloud deploy (e.g., Render/GCP)          |             |
| Full CrewAI integration                  |             |

---

## ✅ Final Output of MVP

* User can define a `template_name`
* Upload and configure an Excel file
* View parsed preview
* See a basic flow diagram in React Flow
* Submit the flow and receive confirmation

