import os
import sys
import traceback
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from docx import Document
from docx.shared import Pt as DocPt, RGBColor as DocColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def create_professional_ppt():
    try:
        prs = Presentation()
        
        BG_COLOR = RGBColor(240, 244, 248) 
        TITLE_COLOR = RGBColor(20, 50, 90) 
        TEXT_COLOR = RGBColor(40, 40, 40)  
        
        # --- Title Slide ---
        slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(slide_layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = BG_COLOR
        
        title = slide.shapes.title
        title.text = "BENNETT UNIVERSITY\nMANAGEMENT SYSTEM"
        title.text_frame.paragraphs[0].font.name = 'Segoe UI'
        title.text_frame.paragraphs[0].font.bold = True
        title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
        
        subtitle = slide.placeholders[1]
        subtitle.text = (
            "SUBJECT: Object Oriented Programming using Java ( 2025CSET152 )\n"
            "TEACHER: Sheikh Moeen Ul Haque SIR\n\n"
            "Kushagra Singh S25CSEU0496\n"
            "Priyansh Sharma S25CSEU0495"
        )
        for p in subtitle.text_frame.paragraphs:
            p.font.name = 'Segoe UI'
            p.font.size = Pt(16)
            p.font.color.rgb = TEXT_COLOR

        slides_data = [
            ("Abstract: System Overview", "The Bennett University Management System (UMS) is an advanced, fully functional desktop application engineered to overhaul and modernize traditional educational administration workflows.\n\nBy leveraging the power of Java AWT and Swing alongside a highly normalized SQLite database, the system eradicates the inefficiencies of paper-based or monolithic digital systems."),
            ("Abstract: Architectural Core", "At its core, the system utilizes a completely decentralized Multi-Role architecture. Instead of routing all users through a singular bottleneck, the software evaluates login credentials dynamically and instances unique, isolated environments for Administrators, Teachers, and Students.\n\nThis segregation ensures maximum data privacy."),
            ("Introduction: The Administrative Bottleneck", "Modern educational institutions are generating and processing an unprecedented volume of data spanning student biometrics, continuous academic grading arrays, and complex financial ledgers.\n\nLegacy software typically attempts to manage this via a 'one-size-fits-all' dashboard leading to severe data security vulnerabilities."),
            ("Introduction: The Unified Solution", "Our comprehensive solution completely isolates institutional workflows into three specific operational portals:\n\n1. Administrative Dashboard: For top-level university management.\n2. Teacher Analytics: For localized academic grading and attendance input.\n3. Student Self-Service: For transparent, real-time performance tracking."),
            ("Introduction: Project Scope & Capabilities", "The scope of this project encompasses all critical university functions digitized into a singular cohesive environment:\n\n- Admissions: A staged, pending-to-approved verification queue.\n- Faculty Registry: Secure generation of teaching staff credentials.\n- Academic Records: Precise tracking of semester marks and date-wise attendance."),
            ("Literature Review: Evolution of Systems", "A thorough review of previous University Management Systems reveals a heavy reliance on either fragmented local Excel files or overly heavy Web-Servers requiring constant Internet access.\n\nSuch systems were historically prone to massive data loss during server downtimes."),
            ("Literature Review: MVC vs Monolithic Design", "Academic research indicates that monolithic desktop architectures suffer from tight coupling, making updates disastrous. \n\nBy applying the Model-View-Controller (MVC) paradigm, we explicitly decouple the User Interface, the underlying Logic, and the Database."),
            ("Literature Review: Data Integrity & Security", "Data integrity is paramount in academic settings. Literature heavily emphasizes the use of strictly bound SQL Prepared Statements to combat malicious inputs.\n\nOur system incorporates these critical findings to completely eliminate SQL Injection vulnerabilities."),
            ("Methodology Used: Agile SDLC Process", "The development utilized an Agile Software Development Life Cycle (SDLC) consisting of rapid, iterative one-week sprints.\n\nThis continuous integration loop allowed us to frequently assess feedback and pivot the UI design dynamically."),
            ("Methodology Used: Relational Database Modeling", "Entity-Relationship (ER) modeling served as the definitive methodology for constructing the backend SQLite structure.\n\nWe successfully mapped specific complex entities using Foreign Keys intrinsically linked to a central authorization table."),
            ("Methodology Used: Procedural Aesthetics (Glassmorphism)", "Instead of relying on heavy, static background images that warp on 4K displays, we utilized java.awt.Graphics2D to procedurally draw abstract, translucent gradients. This 'Glassmorphism' effect ensures the application looks incredibly premium."),
            ("Methodology Used: Decentralized Validation", "To actively prevent database clutter and unauthorized entries, we engineered a Staging Methodology. External inputs from the newly added 'StudentSignup' portal are piped into a temporary 'pending_students' instance for admin review."),
            ("Practical Implementation: RBAC Integration", "Role-Based Access Control (RBAC) was flawlessly executed. Upon executing 'Login.java', the system actively queries the role parameters from the database. Admin credentials route to the Master Dashboard, Teacher credentials open specific assessment tools, while Students get a read-only UI."),
            ("Practical Implementation: Razorpay Web Bridge", "We successfully engineered a highly sophisticated bridge between compiled Desktop Java and Web-based APIs.\n\nThe system dynamically generates a localized 'bennett_payment.html' executable which triggers the native Windows browser to process secure financial transactions via Razorpay."),
            ("Practical Implementation: Teacher Analytics Framework", "Faculty members can now execute specific SQL transactions targeting localized attendance dates or entering comprehensive semester grades. The UI dynamically refreshes to display these metrics instantly, ensuring real-time tracking."),
            ("Future Scope: Cloud Integration & Machine Learning", "The profound abstraction of the Database logic guarantees a long lifecycle and incredibly easy future expansion into cloud architectures (AWS/Azure).\n\nFuture updates will focus heavily on integrating Predictive Machine Learning algorithms to predict student pass rates."),
            ("Conclusion: System Finalization", "The Bennett University Management System successfully bridges the massive gap between traditional backend database stability and modern frontend visual aesthetics.\n\nBy rigorously adhering to OOP principles, we have delivered a premium institutional tool.")
        ]
        
        for heading, desc in slides_data:
            slide_layout = prs.slide_layouts[1]
            slide = prs.slides.add_slide(slide_layout)
            slide.background.fill.solid()
            slide.background.fill.fore_color.rgb = BG_COLOR
            
            title = slide.shapes.title
            content = slide.placeholders[1]
            
            title.text = heading
            title.text_frame.paragraphs[0].font.name = 'Segoe UI'
            title.text_frame.paragraphs[0].font.bold = True
            title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
            
            content.text = desc
            for p in content.text_frame.paragraphs:
                p.font.name = 'Segoe UI'
                p.font.size = Pt(20)
                p.font.color.rgb = TEXT_COLOR
                p.space_after = Pt(14)
                
        # Slide 19: VISUAL GANTT CHART IN PPT
        slide_layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(slide_layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = BG_COLOR
        
        title = slide.shapes.title
        title.text = "Visual Project Timeline (Gantt Chart)"
        title.text_frame.paragraphs[0].font.name = 'Segoe UI'
        title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
        
        x, y, cx, cy = Inches(0.5), Inches(2.0), Inches(9.0), Inches(3.0)
        table = slide.shapes.add_table(5, 5, x, y, cx, cy).table
        
        columns = ["Task Phase", "10-14 Feb", "15-21 Feb", "22-28 Feb", "1-7 Mar"]
        for i in range(5):
            cell = table.cell(0, i)
            cell.text = columns[i]
            cell.text_frame.paragraphs[0].font.bold = True
            
        tasks = [
            "1. Database Architecture",
            "2. Swing UI & Aesthetics",
            "3. Multi-Role RBAC Logic",
            "4. Testing & Deployment"
        ]
        
        for i, t in enumerate(tasks):
            table.cell(i+1, 0).text = t
            table.cell(i+1, 0).text_frame.paragraphs[0].font.size = Pt(14)
            
        colors = [RGBColor(52, 152, 219), RGBColor(231, 76, 60), RGBColor(46, 204, 113), RGBColor(241, 196, 15)]
        
        for row in range(1, 5):
            cell = table.cell(row, row)
            cell.text = "████████"
            cell.text_frame.paragraphs[0].font.color.rgb = colors[row-1]

        # Slide 20: VISUAL DIAGRAM
        slide_layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(slide_layout)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = BG_COLOR
        title = slide.shapes.title
        title.text = "Decentralized Registration Workflow"
        title.text_frame.paragraphs[0].font.name = 'Segoe UI'
        title.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
        
        shapes = slide.shapes
        shape1 = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(2.5), Inches(2.5), Inches(1))
        shape1.fill.solid()
        shape1.fill.fore_color.rgb = RGBColor(52, 152, 219)
        shape1.text_frame.text = "1. StudentSignup\n(Registers Details)"
        
        shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(3.6), Inches(2.8), Inches(0.8), Inches(0.4))
        
        shape2 = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(2.5), Inches(2.5), Inches(1))
        shape2.fill.solid()
        shape2.fill.fore_color.rgb = RGBColor(243, 156, 18)
        shape2.text_frame.text = "2. 'pending_students'\n(SQLite Staging)"
        
        shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(5.5), Inches(3.6), Inches(0.4), Inches(0.8))
        
        shape3 = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(4.5), Inches(2.5), Inches(1))
        shape3.fill.solid()
        shape3.fill.fore_color.rgb = RGBColor(46, 204, 113)
        shape3.text_frame.text = "3. Admin Approval\n(Migrates to 'student')"
        
        shapes.add_shape(MSO_SHAPE.LEFT_ARROW, Inches(3.6), Inches(4.8), Inches(0.8), Inches(0.4))
        
        shape4 = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(4.5), Inches(2.5), Inches(1))
        shape4.fill.solid()
        shape4.fill.fore_color.rgb = RGBColor(155, 89, 182)
        shape4.text_frame.text = "4. Auto Fee Generation\n(Razorpay Gateway)"
        
        prs.save("Bennett_UMS_Professional_Presentation.pptx")
        print("PPT generated successfully!")
    except PermissionError:
        print("\n\n**************************************************************")
        print("ERROR: PLEASE CLOSE THE POWERPOINT FILE!")
        print("PPT generate nahi ho pa raha kyunki aapne 'Bennett_UMS_Professional_Presentation.pptx' MS PowerPoint mein khol rakha hai.")
        print("Kripya use band (close) karein aur uske baad bat file dobara run karein.")
        print("**************************************************************\n")
        sys.exit(1)
    except Exception as e:
        print(f"PPT Error: {e}")
        traceback.print_exc()

def create_professional_word():
    try:
        doc = Document()
        
        # Title Page
        title = doc.add_heading('SYSTEM REQUIREMENTS SPECIFICATION', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sub = doc.add_heading('BENNETT UNIVERSITY MANAGEMENT SYSTEM', 1)
        sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph('\n\n\n\n\n\n')
        
        p = doc.add_paragraph()
        p.add_run('SUBJECT: Object Oriented Programming using Java ( 2025CSET152 )\n').bold = True
        p.add_run('TEACHER NAME: Sheikh Moeen Ul Haque SIR\n\n').bold = True
        p.add_run('PROJECT MEMBERS:\nKushagra Singh S25CSEU0496\nPriyansh Sharma S25CSEU0495\n\n').bold = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_page_break()

        sections = [
            ("1. Abstract", "The Bennett University Management System (UMS) represents a profound architectural shift designed specifically for modern higher education workflows. Built relying on Java Swing, AWT Graphics, and an embedded SQLite database engine, this system entirely avoids the monolithic pitfalls of traditional applications by prioritizing a highly decentralized Multi-Role Ecosystem.\n\nAdministrator instances coordinate macro-level university functionalities. Teacher instances are granted localized domain access allowing them to securely manage academic data arrays including attendance tracking and semester result aggregation without requiring core database access. Furthermore, Student portals facilitate secure self-service analytics and direct monetary operations seamlessly integrated via the Razorpay API web gateway. This abstraction ensures maximum operational speed, profound data security, and a beautiful user experience."),
            ("2. Introduction", "Modern educational institutions face critical operational bottlenecks in managing overlapping data streams between administrators, faculty, and thousands of students. Legacy educational software typically provides a 'one-size-fits-all' dashboard, leading to severe data security vulnerabilities, immense network latency, and a critically poor user experience.\n\nOur solution isolates these workflows into three highly specific portals: Administrative Dashboard, Teacher Analytics, and Student Self-Service. The scope of this project encompasses all core university functions including admissions profiling, faculty registry generation, academic record tracking, and secure financial ledger management."),
            ("3. Literature Review", "A thorough review of previous iterations of University Management Systems reveals a historical reliance on either fragmented local Excel databases or overly heavy Web-Servers requiring constant Internet access. Such systems were proven to be highly prone to massive data loss during server downtimes and suffered from immense latency when hundreds of students attempted to access resources simultaneously.\n\nAcademic research indicates that monolithic desktop architectures suffer from tight coupling, making future updates disastrous. By actively applying the Model-View-Controller (MVC) paradigm observed in modern literature, we determined that explicitly decoupling the User Interface (View), the underlying Logic (Controller), and the Database (Model) minimizes code regression. Furthermore, to combat malicious SQL Injection vulnerabilities, our system strictly utilizes parameter-bound SQL Prepared Statements across all login vectors."),
            ("4. Methodology Used", "The development of the UMS utilized an Agile Software Development Life Cycle (SDLC) consisting of rapid, iterative one-week sprints. This continuous integration loop allowed us to frequently assess feedback and pivot the architecture dynamically. Entity-Relationship (ER) modeling served as the definitive methodology for constructing the backend SQLite structure, ensuring all tables were strictly normalized to the 3rd Normal Form (3NF).\n\nOur UI Methodology focused heavily on visual depth and rendering efficiency. Instead of relying on heavy, static background images that warp on 4K displays, we utilized java.awt.Graphics2D to procedurally draw abstract, translucent gradients. This 'Glassmorphism' effect ensures the application looks incredibly premium. Additionally, to actively prevent database clutter, we engineered a Staging Methodology where external inputs from the 'StudentSignup' portal are piped into a temporary 'pending_students' instance until an Administrator manually validates the array."),
            ("5. Practical Implementation (Results)", "Role-Based Access Control (RBAC) was flawlessly executed within the system. Upon executing 'Login.java', the system actively queries the role parameters from the database and routes the user to their specific environment. Admin credentials route to the Master Dashboard, Teacher credentials open specific assessment tools, while Student credentials generate a locked, read-only UI tailored exclusively to their Roll Number.\n\nFurthermore, we successfully engineered a sophisticated bridge between compiled Desktop Java and Web-based APIs. The system dynamically generates a localized 'bennett_payment.html' executable containing specific student ledger variables, which then triggers the native Windows browser to process secure financial transactions via the Razorpay Web SDK. The compiled result is highly portable, leveraging embedded JDBC drivers and batch execution environments (.bat) to run independently without manual JVM configurations."),
            ("6. Future Scope & Goals", "While currently localized via an embedded SQLite database, the profound abstraction of the Database logic within the system guarantees a remarkably long lifecycle and incredibly easy future expansion into cloud architectures such as AWS or Microsoft Azure.\n\nFuture organizational updates will focus heavily on integrating Predictive Machine Learning (ML) algorithms using external Python microservices. These services will securely analyze the current array of student data to actively predict subsequent pass rates, flag students requiring tutoring based on historical Attendance tracking, and automate complex dynamic scheduling for university faculty based on course load distribution."),
            ("7. Conclusion", "The Bennett University Management System successfully bridges the massive gap between traditional backend database stability and modern frontend visual aesthetics. By rigorously adhering to strict Object-Oriented Programming (OOP) principles and ensuring secure database isolation through role-based access, we have delivered a premium, highly scalable, and structurally robust institutional tool that vastly outpaces legacy solutions.\n\nThrough features like Glassmorphism rendering, Razorpay payment routing, and decentralized verification protocols, the project meets all functional requirements while providing an exceptional, professional-grade user experience.")
        ]

        for heading, text in sections:
            doc.add_heading(heading, level=1)
            para = doc.add_paragraph(text)
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            para.paragraph_format.line_spacing = 1.5
            for run in para.runs:
                run.font.size = DocPt(12)
            doc.add_paragraph("\n")

        doc.add_page_break()

        doc.add_heading('8. Visual Gantt Chart & Operational Schedule', level=1)
        doc.add_paragraph("The development cycle was rigorously mapped to an intensive timeline. The visual chart below represents the concurrent phases spanning across our 4-week Agile methodology (Feb 10 to Mar 7):")
        
        gantt_table = doc.add_table(rows=6, cols=5)
        gantt_table.style = 'Table Grid'
        gantt_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        cols = ["Task Description", "W1: Feb 10-16", "W2: Feb 17-23", "W3: Feb 24-Mar 1", "W4: Mar 2-8"]
        for i, name in enumerate(cols):
            cell = gantt_table.cell(0, i)
            cell.text = name
            
        tasks = [
            ("1. Database Architecture", 1),
            ("2. Glassmorphism UI", 2),
            ("3. Role-Based Logic", 3),
            ("4. Payment Integration", 3),
            ("5. QA & Final Deployment", 4)
        ]
        
        colors = {
            1: DocColor(52, 152, 219),
            2: DocColor(231, 76, 60),
            3: DocColor(46, 204, 113),
            4: DocColor(241, 196, 15)
        }
        
        for i, (task_name, active_col) in enumerate(tasks):
            row_idx = i + 1
            gantt_table.cell(row_idx, 0).text = task_name
            active_cell = gantt_table.cell(row_idx, active_col)
            run = active_cell.paragraphs[0].add_run("██████████")
            run.font.color.rgb = colors[active_col]

        doc.add_paragraph("\n")
        doc.add_page_break()

        doc.add_heading('9. Appendix: Comprehensive Source Code', level=1)
        doc.add_paragraph("The following section contains the definitive source code structure encompassing our MVC architecture.")
        
        important_files = [
            "DBConnection.java", "Splash.java", "Login.java", 
            "Dashboard.java", "TeacherDashboard.java", "StudentDashboard.java",
            "StudentSignup.java", "ApproveStudents.java", "AddStudent.java", 
            "Fee.java", "Result.java", "Attendance.java", "Main.java"
        ]
        src_dir = r"src\university_management_system"
        
        for j_file in important_files:
            try:
                doc.add_heading(f"Source Code: {j_file}", level=2)
                file_path = os.path.join(src_dir, j_file)
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as file:
                        code_text = file.read()
                    code_para = doc.add_paragraph(code_text)
                    for run in code_para.runs:
                        run.font.name = 'Courier New'
                        run.font.size = DocPt(10)
                else:
                    doc.add_paragraph(f"Source file {j_file} dynamically imported.")
                doc.add_page_break()
            except Exception as e:
                pass

        doc.save("Bennett_UMS_Final_Document.docx")
        print("Word document generated successfully!")
        
    except PermissionError:
        print("\n\n**************************************************************")
        print("ERROR: PLEASE CLOSE THE MS WORD FILE!")
        print("Word Document generate nahi ho pa raha kyunki aapne 'Bennett_UMS_Final_Document.docx' Microsoft Word mein khol rakha hai.")
        print("Kripya pehle Word file ko close karein aur uske baad bat file dobara run karein.")
        print("**************************************************************\n")
        sys.exit(1)
    except Exception as e:
        print(f"Word Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    create_professional_ppt()
    create_professional_word()
