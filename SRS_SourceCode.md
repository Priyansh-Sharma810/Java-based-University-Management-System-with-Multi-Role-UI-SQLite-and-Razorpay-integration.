@
# University Management System - Source Code for SRS

This document contains all the Java source code files for the University Management System. You can take screenshots of the code blocks below for your documentation.
@
## AddCourse.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class AddCourse extends JFrame implements ActionListener {
    
    JTextField tfname, tfduration;
    JButton submit, cancel;
    
    public AddCourse() {
        setSize(500, 400);
        setLocation(500, 200);
        setLayout(null);
        
        JLabel heading = new JLabel("Add New Course");
        heading.setBounds(150, 30, 300, 30);
        heading.setFont(new Font("serif", Font.BOLD, 25));
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(50, 50, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(400, 20, 50, 50);
            add(image);
        } catch (Exception e) {}
        
        JLabel lblname = new JLabel("Course Name");
        lblname.setBounds(50, 100, 150, 30);
        lblname.setFont(new Font("serif", Font.BOLD, 20));
        add(lblname);
        
        tfname = new JTextField();
        tfname.setBounds(250, 100, 150, 30);
        add(tfname);
        
        JLabel lblduration = new JLabel("Duration");
        lblduration.setBounds(50, 160, 150, 30);
        lblduration.setFont(new Font("serif", Font.BOLD, 20));
        add(lblduration);
        
        tfduration = new JTextField();
        tfduration.setBounds(250, 160, 150, 30);
        add(tfduration);
        
        submit = new JButton("Submit");
        submit.setBounds(100, 250, 120, 30);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this);
        submit.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(submit);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(250, 250, 120, 30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(cancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == submit) {
            String name = tfname.getText();
            String duration = tfduration.getText();
            
            try {
                String query = "insert into course(name, duration) values('"+name+"', '"+duration+"')";
                DBConnection con = new DBConnection();
                con.s.executeUpdate(query);
                
                JOptionPane.showMessageDialog(null, "Course Added Successfully");
                setVisible(false);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            setVisible(false);
        }
    }
    
    public static void main(String[] args) {
        new AddCourse();
    }
}
```

## AddStudent.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class AddStudent extends JFrame implements ActionListener {
    
    JTextField tfname, tffname, tfaddress, tfphone, tfemail, tfx, tfxii, tfdob;
    JComboBox<String> cbcourse, cbbranch;
    JButton submit, cancel;
    
    // Simulating a random roll number generator
    long random = Math.abs((new java.util.Random()).nextLong() % 9000L) + 1000L;
    JLabel labelrollno;
    
    public AddStudent() {
        setSize(900, 700);
        setLocation(300, 50);
        setLayout(null);
        
        JLabel heading = new JLabel("New Student Details");
        heading.setBounds(310, 30, 500, 50);
        heading.setFont(new Font("serif", Font.BOLD, 30));
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(80, 80, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(750, 20, 80, 80);
            add(image);
            
            JLabel topname = new JLabel("BENOVEN");
            topname.setBounds(380, 10, 150, 30);
            topname.setFont(new Font("serif", Font.BOLD, 20));
            topname.setForeground(new Color(30, 60, 100));
            add(topname);
        } catch (Exception e) {}
        
        // Name
        JLabel lblname = new JLabel("Name");
        lblname.setBounds(50, 150, 100, 30);
        lblname.setFont(new Font("serif", Font.BOLD, 20));
        add(lblname);
        
        tfname = new JTextField();
        tfname.setBounds(200, 150, 150, 30);
        add(tfname);
        
        // Father Name
        JLabel lblfname = new JLabel("Father's Name");
        lblfname.setBounds(400, 150, 200, 30);
        lblfname.setFont(new Font("serif", Font.BOLD, 20));
        add(lblfname);
        
        tffname = new JTextField();
        tffname.setBounds(600, 150, 150, 30);
        add(tffname);
        
        // Roll No
        JLabel lblrollno = new JLabel("Roll Number");
        lblrollno.setBounds(50, 200, 200, 30);
        lblrollno.setFont(new Font("serif", Font.BOLD, 20));
        add(lblrollno);
        
        labelrollno = new JLabel("1533" + random);
        labelrollno.setBounds(200, 200, 200, 30);
        labelrollno.setFont(new Font("serif", Font.BOLD, 20));
        add(labelrollno);
        
        // DOB
        JLabel lbldob = new JLabel("Date of Birth");
        lbldob.setBounds(400, 200, 200, 30);
        lbldob.setFont(new Font("serif", Font.BOLD, 20));
        add(lbldob);
        
        // To simplify, just using text field instead of calendar component
        JLabel dobHint = new JLabel("(DD/MM/YYYY)");
        dobHint.setBounds(600, 230, 150, 20);
        add(dobHint);
        
        tfdob = new JTextField(); 
        tfdob.setBounds(600, 200, 150, 30);
        add(tfdob);
        
        // Address
        JLabel lbladdress = new JLabel("Address");
        lbladdress.setBounds(50, 250, 200, 30);
        lbladdress.setFont(new Font("serif", Font.BOLD, 20));
        add(lbladdress);
        
        tfaddress = new JTextField();
        tfaddress.setBounds(200, 250, 150, 30);
        add(tfaddress);
        
        // Phone
        JLabel lblphone = new JLabel("Phone");
        lblphone.setBounds(400, 250, 200, 30);
        lblphone.setFont(new Font("serif", Font.BOLD, 20));
        add(lblphone);
        
        tfphone = new JTextField();
        tfphone.setBounds(600, 250, 150, 30);
        add(tfphone);
        
        // Email
        JLabel lblemail = new JLabel("Email Id");
        lblemail.setBounds(50, 300, 200, 30);
        lblemail.setFont(new Font("serif", Font.BOLD, 20));
        add(lblemail);
        
        tfemail = new JTextField();
        tfemail.setBounds(200, 300, 150, 30);
        add(tfemail);
        
        // Class X
        JLabel lblx = new JLabel("Class X %");
        lblx.setBounds(400, 300, 200, 30);
        lblx.setFont(new Font("serif", Font.BOLD, 20));
        add(lblx);
        
        tfx = new JTextField();
        tfx.setBounds(600, 300, 150, 30);
        add(tfx);
        
        // Class XII
        JLabel lblxii = new JLabel("Class XII %");
        lblxii.setBounds(50, 350, 200, 30);
        lblxii.setFont(new Font("serif", Font.BOLD, 20));
        add(lblxii);
        
        tfxii = new JTextField();
        tfxii.setBounds(200, 350, 150, 30);
        add(tfxii);
        
        // Course
        JLabel lblcourse = new JLabel("Course");
        lblcourse.setBounds(400, 350, 200, 30);
        lblcourse.setFont(new Font("serif", Font.BOLD, 20));
        add(lblcourse);
        
        String[] course = {"B.Tech", "BBA", "BCA", "Bsc", "Msc", "MBA", "MCA", "MCom", "MA", "BA"};
        cbcourse = new JComboBox<>(course);
        cbcourse.setBounds(600, 350, 150, 30);
        add(cbcourse);
        
        // Branch
        JLabel lblbranch = new JLabel("Branch");
        lblbranch.setBounds(50, 400, 200, 30);
        lblbranch.setFont(new Font("serif", Font.BOLD, 20));
        add(lblbranch);
        
        String[] branch = {"Computer Science", "Electronics", "Mechanical", "Civil", "IT"};
        cbbranch = new JComboBox<>(branch);
        cbbranch.setBounds(200, 400, 150, 30);
        add(cbbranch);
        
        submit = new JButton("Submit");
        submit.setBounds(250, 550, 120, 30);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this);
        submit.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(submit);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(450, 550, 120, 30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(cancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == submit) {
            String name = tfname.getText();
            String fname = tffname.getText();
            String rollno = labelrollno.getText();
            String dob = tfdob.getText();
            String address = tfaddress.getText();
            String phone = tfphone.getText();
            String email = tfemail.getText();
            String x = tfx.getText();
            String xii = tfxii.getText();
            String course = (String) cbcourse.getSelectedItem();
            String branch = (String) cbbranch.getSelectedItem();
            
            try {
                String query = "insert into student values('"+rollno+"', '"+name+"', '"+fname+"', '"+dob+"', '"+address+"', '"+phone+"', '"+email+"', '"+x+"', '"+xii+"', '"+course+"', '"+branch+"')";
                DBConnection con = new DBConnection();
                con.s.executeUpdate(query);
                
                JOptionPane.showMessageDialog(null, "Student Details Inserted Successfully");
                setVisible(false);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            setVisible(false);
        }
    }

    public static void main(String[] args) {
        new AddStudent();
    }
}
```

## AddTeacher.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class AddTeacher extends JFrame implements ActionListener {
    
    JTextField tfname, tffname, tfaddress, tfphone, tfemail, tfdob;
    JComboBox<String> cbeducation, cbdepartment;
    JButton submit, cancel;
    
    long random = Math.abs((new java.util.Random()).nextLong() % 9000L) + 1000L;
    JLabel labelempid;
    
    public AddTeacher() {
        setSize(900, 700);
        setLocation(300, 50);
        setLayout(null);
        
        JLabel heading = new JLabel("New Teacher Details");
        heading.setBounds(310, 30, 500, 50);
        heading.setFont(new Font("serif", Font.BOLD, 30));
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(80, 80, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(750, 20, 80, 80);
            add(image);
            
            JLabel topname = new JLabel("BENOVEN");
            topname.setBounds(380, 10, 150, 30);
            topname.setFont(new Font("serif", Font.BOLD, 20));
            topname.setForeground(new Color(30, 60, 100));
            add(topname);
        } catch (Exception e) {}
        
        // Name
        JLabel lblname = new JLabel("Name");
        lblname.setBounds(50, 150, 100, 30);
        lblname.setFont(new Font("serif", Font.BOLD, 20));
        add(lblname);
        
        tfname = new JTextField();
        tfname.setBounds(200, 150, 150, 30);
        add(tfname);
        
        // Father Name
        JLabel lblfname = new JLabel("Father's Name");
        lblfname.setBounds(400, 150, 200, 30);
        lblfname.setFont(new Font("serif", Font.BOLD, 20));
        add(lblfname);
        
        tffname = new JTextField();
        tffname.setBounds(600, 150, 150, 30);
        add(tffname);
        
        // Employee ID
        JLabel lblempid = new JLabel("Employee Id");
        lblempid.setBounds(50, 200, 200, 30);
        lblempid.setFont(new Font("serif", Font.BOLD, 20));
        add(lblempid);
        
        labelempid = new JLabel("101" + random);
        labelempid.setBounds(200, 200, 200, 30);
        labelempid.setFont(new Font("serif", Font.BOLD, 20));
        add(labelempid);
        
        // DOB
        JLabel lbldob = new JLabel("Date of Birth");
        lbldob.setBounds(400, 200, 200, 30);
        lbldob.setFont(new Font("serif", Font.BOLD, 20));
        add(lbldob);
        
        JLabel dobHint = new JLabel("(DD/MM/YYYY)");
        dobHint.setBounds(600, 230, 150, 20);
        add(dobHint);
        
        tfdob = new JTextField(); 
        tfdob.setBounds(600, 200, 150, 30);
        add(tfdob);
        
        // Address
        JLabel lbladdress = new JLabel("Address");
        lbladdress.setBounds(50, 250, 200, 30);
        lbladdress.setFont(new Font("serif", Font.BOLD, 20));
        add(lbladdress);
        
        tfaddress = new JTextField();
        tfaddress.setBounds(200, 250, 150, 30);
        add(tfaddress);
        
        // Phone
        JLabel lblphone = new JLabel("Phone");
        lblphone.setBounds(400, 250, 200, 30);
        lblphone.setFont(new Font("serif", Font.BOLD, 20));
        add(lblphone);
        
        tfphone = new JTextField();
        tfphone.setBounds(600, 250, 150, 30);
        add(tfphone);
        
        // Email
        JLabel lblemail = new JLabel("Email Id");
        lblemail.setBounds(50, 300, 200, 30);
        lblemail.setFont(new Font("serif", Font.BOLD, 20));
        add(lblemail);
        
        tfemail = new JTextField();
        tfemail.setBounds(200, 300, 150, 30);
        add(tfemail);
        
        // Education
        JLabel lbleducation = new JLabel("Qualification");
        lbleducation.setBounds(400, 300, 200, 30);
        lbleducation.setFont(new Font("serif", Font.BOLD, 20));
        add(lbleducation);
        
        String[] education = {"B.Tech", "M.Tech", "Ph.D", "Bsc", "Msc", "MBA", "MA", "BA"};
        cbeducation = new JComboBox<>(education);
        cbeducation.setBounds(600, 300, 150, 30);
        add(cbeducation);
        
        // Department
        JLabel lbldepartment = new JLabel("Department");
        lbldepartment.setBounds(50, 350, 200, 30);
        lbldepartment.setFont(new Font("serif", Font.BOLD, 20));
        add(lbldepartment);
        
        String[] department = {"Computer Science", "Electronics", "Mechanical", "Civil", "IT"};
        cbdepartment = new JComboBox<>(department);
        cbdepartment.setBounds(200, 350, 150, 30);
        add(cbdepartment);
        
        submit = new JButton("Submit");
        submit.setBounds(250, 500, 120, 30);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this);
        submit.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(submit);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(450, 500, 120, 30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(cancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == submit) {
            String name = tfname.getText();
            String fname = tffname.getText();
            String empid = labelempid.getText();
            String dob = tfdob.getText();
            String address = tfaddress.getText();
            String phone = tfphone.getText();
            String email = tfemail.getText();
            String education = (String) cbeducation.getSelectedItem();
            String department = (String) cbdepartment.getSelectedItem();
            
            try {
                String query = "insert into teacher values('"+empid+"', '"+name+"', '"+fname+"', '"+dob+"', '"+address+"', '"+phone+"', '"+email+"', '"+education+"', '"+department+"')";
                DBConnection con = new DBConnection();
                con.s.executeUpdate(query);
                
                JOptionPane.showMessageDialog(null, "Teacher Details Inserted Successfully");
                setVisible(false);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            setVisible(false);
        }
    }

    public static void main(String[] args) {
        new AddTeacher();
    }
}
```

## Attendance.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.sql.*;
import java.awt.event.*;

public class Attendance extends JFrame implements ActionListener {
    
    Choice crollno;
    JComboBox<String> cbhalf1, cbhalf2;
    JButton submit, cancel;
    
    public Attendance() {
        setSize(400, 400);
        setLocation(550, 250);
        setLayout(null);
        
        JLabel heading = new JLabel("Student Attendance");
        heading.setBounds(100, 30, 200, 30);
        heading.setFont(new Font("serif", Font.BOLD, 22));
        add(heading);
        
        JLabel lblrollno = new JLabel("Select Roll No");
        lblrollno.setBounds(50, 100, 120, 20);
        lblrollno.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lblrollno);
        
        crollno = new Choice();
        crollno.setBounds(200, 100, 150, 20);
        add(crollno);
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from student");
            while(rs.next()) {
                crollno.add(rs.getString("rollno"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JLabel lbldate = new JLabel("Date");
        lbldate.setBounds(50, 160, 120, 20);
        lbldate.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lbldate);
        
        // Simulating the date using text field
        JTextField tfdate = new JTextField("01/01/2026");
        tfdate.setBounds(200, 160, 150, 20);
        add(tfdate);
        
        JLabel lblhalf1 = new JLabel("First Half");
        lblhalf1.setBounds(50, 220, 120, 20);
        lblhalf1.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lblhalf1);
        
        String[] statuses = {"Present", "Absent", "Leave"};
        cbhalf1 = new JComboBox<>(statuses);
        cbhalf1.setBounds(200, 220, 150, 20);
        add(cbhalf1);
        
        JLabel lblhalf2 = new JLabel("Second Half");
        lblhalf2.setBounds(50, 280, 120, 20);
        lblhalf2.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lblhalf2);
        
        cbhalf2 = new JComboBox<>(statuses);
        cbhalf2.setBounds(200, 280, 150, 20);
        add(cbhalf2);
        
        submit = new JButton("Submit");
        submit.setBounds(80, 340, 100, 25);
        submit.setBackground(Color.BLACK);
        submit.setForeground(Color.WHITE);
        submit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                String rollno = crollno.getSelectedItem();
                String date = tfdate.getText();
                String first_half = (String) cbhalf1.getSelectedItem();
                String second_half = (String) cbhalf2.getSelectedItem();
                
                try {
                    DBConnection c = new DBConnection();
                    String query = "insert into attendance_student(rollno, date, first_half, second_half) values('"+rollno+"', '"+date+"', '"+first_half+"', '"+second_half+"')";
                    c.s.executeUpdate(query);
                    
                    JOptionPane.showMessageDialog(null, "Attendance Confirmed");
                    setVisible(false);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        add(submit);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(220, 340, 100, 25);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                setVisible(false);
            }
        });
        add(cancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {}
    
    public static void main(String[] args) {
        new Attendance();
    }
}
```

## Dashboard.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Dashboard extends JFrame implements ActionListener {

    public Dashboard() {
        // Make dashboard full screen and visually appealing
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        
        // Use absolute layout for custom positioning
        setLayout(null);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        
        // White Header Panel at the top
        JPanel header = new JPanel();
        header.setBackground(Color.WHITE);
        header.setBounds(0, 0, screenSize.width, 80);
        header.setLayout(null);
        
        // Text in the Header
        JLabel text = new JLabel("BENOVEN UNIVERSITY");
        text.setBounds((screenSize.width - 1000) / 2, 10, 1000, 60);
        text.setFont(new Font("serif", Font.BOLD, 55));
        text.setForeground(new Color(30, 60, 100)); // Dark Blue
        text.setHorizontalAlignment(SwingConstants.CENTER);
        header.add(text);
        
        // Logo in the Header
        try {
            ImageIcon logoIcon = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image l2 = logoIcon.getImage().getScaledInstance(70, 70, Image.SCALE_DEFAULT);
            ImageIcon l3 = new ImageIcon(l2);
            JLabel logoImage = new JLabel(l3);
            logoImage.setBounds(screenSize.width - 100, 5, 70, 70); // Right side
            header.add(logoImage);
        } catch (Exception e) {}
        
        add(header);
        
        // Background Image Below Menus
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/university.jpg"));
            Image i2 = i1.getImage().getScaledInstance(screenSize.width, screenSize.height - 110, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(0, 110, screenSize.width, screenSize.height - 110);
            
            // Subtitle Details at the bottom of the screen
            JLabel subtitle = new JLabel("Excellence in Education | Management System Portal");
            subtitle.setBounds((screenSize.width - 1000) / 2, screenSize.height - 250, 1000, 50);
            subtitle.setFont(new Font("Tahoma", Font.BOLD, 22));
            subtitle.setForeground(new Color(220, 220, 220)); // Light Gray/White
            subtitle.setHorizontalAlignment(SwingConstants.CENTER);
            image.add(subtitle);
            
            add(image);
        } catch (Exception e) {}
        
        // Menu Bar placed manually below the header
        JMenuBar mb = new JMenuBar();
        mb.setBounds(0, 80, screenSize.width, 30);
        mb.setBackground(new Color(240, 240, 255));
        
        // 1. New Information
        JMenu newInfo = new JMenu("New Information");
        newInfo.setForeground(Color.BLUE);
        mb.add(newInfo);
        
        JMenuItem facultyInfo = new JMenuItem("Add Teacher");
        facultyInfo.setBackground(Color.WHITE);
        facultyInfo.addActionListener(this);
        newInfo.add(facultyInfo);
        
        JMenuItem studentInfo = new JMenuItem("Add Student");
        studentInfo.setBackground(Color.WHITE);
        studentInfo.addActionListener(this);
        newInfo.add(studentInfo);

        // 2. View Details
        JMenu details = new JMenu("View Details");
        details.setForeground(Color.RED);
        mb.add(details);
        
        JMenuItem facultyDetails = new JMenuItem("View Teacher Details");
        facultyDetails.setBackground(Color.WHITE);
        facultyDetails.addActionListener(this);
        details.add(facultyDetails);
        
        JMenuItem studentDetails = new JMenuItem("View Student Details");
        studentDetails.setBackground(Color.WHITE);
        studentDetails.addActionListener(this);
        details.add(studentDetails);

        // 3. Apply Course
        JMenu course = new JMenu("Course Add");
        course.setForeground(Color.BLUE);
        mb.add(course);
        
        JMenuItem newCourse = new JMenuItem("Add Course");
        newCourse.setBackground(Color.WHITE);
        newCourse.addActionListener(this);
        course.add(newCourse);

        // 4. Update Details
        JMenu updateInfo = new JMenu("Attendance");
        updateInfo.setForeground(Color.RED);
        mb.add(updateInfo);
        
        JMenuItem updateFacultyInfo = new JMenuItem("Attendance Tracking");
        updateFacultyInfo.setBackground(Color.WHITE);
        updateFacultyInfo.addActionListener(this);
        updateInfo.add(updateFacultyInfo);

        // 5. Fees
        JMenu fee = new JMenu("Fee Details");
        fee.setForeground(Color.BLUE);
        mb.add(fee);
        
        JMenuItem feeStructure = new JMenuItem("Fee Payment");
        feeStructure.setBackground(Color.WHITE);
        feeStructure.addActionListener(this);
        fee.add(feeStructure);

        // 6. Examination
        JMenu exam = new JMenu("Examination");
        exam.setForeground(Color.BLUE);
        mb.add(exam);
        
        JMenuItem examDetails = new JMenuItem("Examination Results");
        examDetails.setBackground(Color.WHITE);
        examDetails.addActionListener(this);
        exam.add(examDetails);

        // 7. Utility
        JMenu utility = new JMenu("Utility");
        utility.setForeground(Color.RED);
        mb.add(utility);
        
        JMenuItem notepad = new JMenuItem("Notepad");
        notepad.setBackground(Color.WHITE);
        notepad.addActionListener(this);
        utility.add(notepad);
        
        JMenuItem calc = new JMenuItem("Calculator");
        calc.setBackground(Color.WHITE);
        calc.addActionListener(this);
        utility.add(calc);

        // 8. Exit
        JMenu exit = new JMenu("Exit");
        exit.setForeground(Color.RED);
        mb.add(exit);
        
        JMenuItem ex = new JMenuItem("Exit");
        ex.setBackground(Color.WHITE);
        ex.addActionListener(this);
        exit.add(ex);
        
        // Add the menu bar using our absolute bounds instead of setJMenuBar(mb)
        add(mb);
        
        setVisible(true);
    }

    public void actionPerformed(ActionEvent ae) {
        String msg = ae.getActionCommand();
        
        if (msg.equals("Exit")) {
            setVisible(false);
            System.exit(0);
        } else if (msg.equals("Calculator")) {
            try {
                Runtime.getRuntime().exec("calc.exe");
            } catch (Exception e) {}
        } else if (msg.equals("Notepad")) {
            try {
                Runtime.getRuntime().exec("notepad.exe");
            } catch (Exception e) {}
        } else if (msg.equals("Add Teacher")) {
            new AddTeacher();
        } else if (msg.equals("Add Student")) {
            new AddStudent();
        } else if (msg.equals("View Teacher Details")) {
            new ViewTeacher();
        } else if (msg.equals("View Student Details")) {
            new ViewStudent();
        } else if (msg.equals("Add Course")) {
            new AddCourse();
        } else if (msg.equals("Fee Payment")) {
            new Fee();
        } else if (msg.equals("Attendance Tracking")) {
            new Attendance();
        } else if (msg.equals("Examination Results")) {
            new Result();
        }
    }

    public static void main(String[] args) {
        new Dashboard();
    }
}
```

## DBConnection.java
```java
package university_management_system;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DBConnection {
    Connection c;
    Statement s;

    public DBConnection() {
        try {
            // Register SQLite JDBC Driver
            Class.forName("org.sqlite.JDBC");
            
            // Connect to SQLite DB
            c = DriverManager.getConnection("jdbc:sqlite:university.db");
            s = c.createStatement();
            
            // Initialize database tables if they do not exist
            initTables();
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    private void initTables() {
        try {
            s.execute("CREATE TABLE IF NOT EXISTS login(username VARCHAR(30), password VARCHAR(30))");
            // Check if admin user exists, if not, insert
            java.sql.ResultSet rs = s.executeQuery("SELECT * FROM login WHERE username='admin'");
            if (!rs.next()) {
                s.execute("INSERT INTO login (username, password) VALUES ('admin', 'admin123')");
            }
            rs.close();

            s.execute("CREATE TABLE IF NOT EXISTS student(rollno VARCHAR(20) PRIMARY KEY, name VARCHAR(50), father_name VARCHAR(50), dob VARCHAR(30), address VARCHAR(100), phone VARCHAR(20), email VARCHAR(50), class_x VARCHAR(10), class_xii VARCHAR(10), course VARCHAR(30), branch VARCHAR(30))");
            s.execute("CREATE TABLE IF NOT EXISTS teacher(emp_id VARCHAR(20) PRIMARY KEY, name VARCHAR(50), father_name VARCHAR(50), dob VARCHAR(30), address VARCHAR(100), phone VARCHAR(20), email VARCHAR(50), education VARCHAR(50), department VARCHAR(50))");
            s.execute("CREATE TABLE IF NOT EXISTS course(course_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), duration VARCHAR(20))");
            s.execute("CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY AUTOINCREMENT, rollno VARCHAR(20), course VARCHAR(30), branch VARCHAR(30), semester VARCHAR(20), amount VARCHAR(20))");
            s.execute("CREATE TABLE IF NOT EXISTS attendance_student(id INTEGER PRIMARY KEY AUTOINCREMENT, rollno VARCHAR(20), date VARCHAR(30), first_half VARCHAR(20), second_half VARCHAR(20))");
            s.execute("CREATE TABLE IF NOT EXISTS attendance_teacher(id INTEGER PRIMARY KEY AUTOINCREMENT, emp_id VARCHAR(20), date VARCHAR(30), first_half VARCHAR(20), second_half VARCHAR(20))");
            s.execute("CREATE TABLE IF NOT EXISTS marks(id INTEGER PRIMARY KEY AUTOINCREMENT, rollno VARCHAR(20), semester VARCHAR(20), marks1 VARCHAR(10), marks2 VARCHAR(10), marks3 VARCHAR(10), marks4 VARCHAR(10), marks5 VARCHAR(10))");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

## Fee.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.sql.*;
import java.awt.event.*;

public class Fee extends JFrame implements ActionListener {
    
    Choice crollno;
    JComboBox<String> cbcourse, cbbranch, cbsemester;
    JTextField tfamount;
    JButton pay, cancel;
    
    public Fee() {
        setSize(500, 500);
        setLocation(500, 200);
        setLayout(null);
        
        JLabel heading = new JLabel("Student Fee Payment");
        heading.setBounds(130, 20, 250, 30);
        heading.setFont(new Font("serif", Font.BOLD, 25));
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(60, 60, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(400, 10, 60, 60);
            add(image);
        } catch (Exception e) {}
        
        JLabel lblrollno = new JLabel("Select Roll No");
        lblrollno.setBounds(50, 80, 150, 20);
        lblrollno.setFont(new Font("Tahoma", Font.BOLD, 16));
        add(lblrollno);
        
        crollno = new Choice();
        crollno.setBounds(250, 80, 150, 20);
        add(crollno);
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from student");
            while(rs.next()) {
                crollno.add(rs.getString("rollno"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JLabel lblcourse = new JLabel("Course");
        lblcourse.setBounds(50, 140, 150, 20);
        lblcourse.setFont(new Font("Tahoma", Font.BOLD, 16));
        add(lblcourse);
        
        String[] course = {"B.Tech", "BBA", "BCA", "Bsc", "Msc", "MBA", "MCA", "MCom", "MA", "BA"};
        cbcourse = new JComboBox<>(course);
        cbcourse.setBounds(250, 140, 150, 20);
        add(cbcourse);
        
        JLabel lblbranch = new JLabel("Branch");
        lblbranch.setBounds(50, 200, 150, 20);
        lblbranch.setFont(new Font("Tahoma", Font.BOLD, 16));
        add(lblbranch);
        
        String[] branch = {"Computer Science", "Electronics", "Mechanical", "Civil", "IT"};
        cbbranch = new JComboBox<>(branch);
        cbbranch.setBounds(250, 200, 150, 20);
        add(cbbranch);
        
        JLabel lblsemester = new JLabel("Semester");
        lblsemester.setBounds(50, 260, 150, 20);
        lblsemester.setFont(new Font("Tahoma", Font.BOLD, 16));
        add(lblsemester);
        
        String[] semester = {"Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"};
        cbsemester = new JComboBox<>(semester);
        cbsemester.setBounds(250, 260, 150, 20);
        add(cbsemester);
        
        JLabel lblamount = new JLabel("Total Amount");
        lblamount.setBounds(50, 320, 150, 20);
        lblamount.setFont(new Font("Tahoma", Font.BOLD, 16));
        add(lblamount);
        
        tfamount = new JTextField();
        tfamount.setBounds(250, 320, 150, 20);
        add(tfamount);
        
        pay = new JButton("Pay Fee");
        pay.setBounds(100, 400, 120, 30);
        pay.setBackground(Color.BLACK);
        pay.setForeground(Color.WHITE);
        pay.addActionListener(this);
        pay.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(pay);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(250, 400, 120, 30);
        cancel.setBackground(Color.BLACK);
        cancel.setForeground(Color.WHITE);
        cancel.addActionListener(this);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        add(cancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == pay) {
            String rollno = crollno.getSelectedItem();
            String course = (String) cbcourse.getSelectedItem();
            String branch = (String) cbbranch.getSelectedItem();
            String semester = (String) cbsemester.getSelectedItem();
            String amount = tfamount.getText();
            
            try {
                DBConnection c = new DBConnection();
                String query = "insert into fee (rollno, course, branch, semester, amount) values('"+rollno+"', '"+course+"', '"+branch+"', '"+semester+"', '"+amount+"')";
                c.s.executeUpdate(query);
                
                JOptionPane.showMessageDialog(null, "Fee paid successfully");
                setVisible(false);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            setVisible(false);
        }
    }
    
    public static void main(String[] args) {
        new Fee();
    }
}
```

## Login.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class Login extends JFrame implements ActionListener {
    
    JTextField tfusername;
    JPasswordField tfpassword;
    JButton login, cancel;

    public Login() {
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        
        // Logo at Top Center
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(120, 120, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(240, 20, 120, 120);
            add(image);
        } catch (Exception e) {}
        
        JLabel heading = new JLabel("BENOVEN LOGIN", SwingConstants.CENTER);
        heading.setBounds(150, 150, 300, 30);
        heading.setFont(new Font("Tahoma", Font.BOLD, 22));
        heading.setForeground(new Color(30, 60, 100));
        add(heading);
        
        JLabel lblusername = new JLabel("Username");
        lblusername.setBounds(180, 210, 100, 20);
        lblusername.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lblusername);
        
        tfusername = new JTextField();
        tfusername.setBounds(280, 205, 150, 30);
        tfusername.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(Color.GRAY),
            BorderFactory.createEmptyBorder(5, 5, 5, 5)));
        add(tfusername);
        
        JLabel lblpassword = new JLabel("Password");
        lblpassword.setBounds(180, 260, 100, 20);
        lblpassword.setFont(new Font("Tahoma", Font.BOLD, 14));
        add(lblpassword);
        
        tfpassword = new JPasswordField();
        tfpassword.setBounds(280, 255, 150, 30);
        tfpassword.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(Color.GRAY),
            BorderFactory.createEmptyBorder(5, 5, 5, 5)));
        add(tfpassword);
        
        login = new JButton("Login");
        login.setBounds(200, 320, 100, 35);
        login.setBackground(new Color(40, 100, 200));
        login.setForeground(Color.WHITE);
        login.setFont(new Font("Tahoma", Font.BOLD, 15));
        login.setFocusPainted(false);
        login.addActionListener(this);
        add(login);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(310, 320, 100, 35);
        cancel.setBackground(new Color(200, 40, 40));
        cancel.setForeground(Color.WHITE);
        cancel.setFont(new Font("Tahoma", Font.BOLD, 15));
        cancel.setFocusPainted(false);
        cancel.addActionListener(this);
        add(cancel);
        
        setSize(600, 420);
        setLocation(450, 200);
        setTitle("Benoven Secure Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    // Handle button clicks
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == login) {
            String username = tfusername.getText();
            String password = new String(tfpassword.getPassword());
            
            try {
                DBConnection c = new DBConnection();
                String query = "select * from login where username='"+username+"' and password='"+password+"'";
                ResultSet rs = c.s.executeQuery(query);
                
                if (rs.next()) {
                    setVisible(false);
                    new Dashboard();
                } else {
                    JOptionPane.showMessageDialog(null, "Invalid username or password");
                }
                
                c.s.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else if (ae.getSource() == cancel) {
            setVisible(false);
            System.exit(0);
        }
    }
    
    public static void main(String[] args) {
        new Login();
    }
}
```

## Main.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;

public class Main extends JFrame implements Runnable {
    
    Thread t;
    
    public Main() {
        // Just launch login window directly and exit Main logic
        new Login();
    }
    
    public void run() {}
    
    public static void main(String[] args) {
        new Main();
    }
}
```

## Result.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.sql.*;
import java.awt.event.*;

public class Result extends JFrame implements ActionListener {
    
    JTextField tfmarks1, tfmarks2, tfmarks3, tfmarks4, tfmarks5;
    Choice crollno;
    JComboBox<String> cbsemester;
    JButton btnSubmit, btnCancel;
    
    public Result() {
        setSize(500, 500);
        setLocation(500, 150);
        setLayout(null);
        
        JLabel heading = new JLabel("Enter Student Results");
        heading.setBounds(100, 20, 300, 30);
        heading.setFont(new Font("serif", Font.BOLD, 25));
        add(heading);
        
        JLabel lblrollno = new JLabel("Select Roll No");
        lblrollno.setBounds(50, 80, 150, 20);
        add(lblrollno);
        
        crollno = new Choice();
        crollno.setBounds(200, 80, 150, 20);
        add(crollno);
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from student");
            while(rs.next()) {
                crollno.add(rs.getString("rollno"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JLabel lblsemester = new JLabel("Select Semester");
        lblsemester.setBounds(50, 130, 150, 20);
        add(lblsemester);
        
        String[] semester = {"1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester"};
        cbsemester = new JComboBox<>(semester);
        cbsemester.setBounds(200, 130, 150, 20);
        add(cbsemester);
        
        JLabel lblmarks1 = new JLabel("Subject 1 Marks");
        lblmarks1.setBounds(50, 180, 150, 20);
        add(lblmarks1);
        tfmarks1 = new JTextField();
        tfmarks1.setBounds(200, 180, 150, 20);
        add(tfmarks1);
        
        JLabel lblmarks2 = new JLabel("Subject 2 Marks");
        lblmarks2.setBounds(50, 230, 150, 20);
        add(lblmarks2);
        tfmarks2 = new JTextField();
        tfmarks2.setBounds(200, 230, 150, 20);
        add(tfmarks2);
        
        JLabel lblmarks3 = new JLabel("Subject 3 Marks");
        lblmarks3.setBounds(50, 280, 150, 20);
        add(lblmarks3);
        tfmarks3 = new JTextField();
        tfmarks3.setBounds(200, 280, 150, 20);
        add(tfmarks3);
        
        JLabel lblmarks4 = new JLabel("Subject 4 Marks");
        lblmarks4.setBounds(50, 330, 150, 20);
        add(lblmarks4);
        tfmarks4 = new JTextField();
        tfmarks4.setBounds(200, 330, 150, 20);
        add(tfmarks4);
        
        JLabel lblmarks5 = new JLabel("Subject 5 Marks");
        lblmarks5.setBounds(50, 380, 150, 20);
        add(lblmarks5);
        tfmarks5 = new JTextField();
        tfmarks5.setBounds(200, 380, 150, 20);
        add(tfmarks5);
        
        btnSubmit = new JButton("Submit");
        btnSubmit.setBounds(100, 430, 100, 25);
        btnSubmit.addActionListener(this);
        add(btnSubmit);
        
        btnCancel = new JButton("Cancel");
        btnCancel.setBounds(250, 430, 100, 25);
        btnCancel.addActionListener(this);
        add(btnCancel);
        
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == btnSubmit) {
            try {
                DBConnection c = new DBConnection();
                String query = "insert into marks (rollno, semester, marks1, marks2, marks3, marks4, marks5) values('"+crollno.getSelectedItem()+"', '"+cbsemester.getSelectedItem()+"', '"+tfmarks1.getText()+"', '"+tfmarks2.getText()+"', '"+tfmarks3.getText()+"', '"+tfmarks4.getText()+"', '"+tfmarks5.getText()+"')";
                c.s.executeUpdate(query);
                
                JOptionPane.showMessageDialog(null, "Results Inserted Successfully");
                setVisible(false);
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            setVisible(false);
        }
    }

    public static void main(String[] args) {
        new Result();
    }
}
```

## ViewStudent.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.sql.*;
import java.awt.event.*;

import javax.swing.table.DefaultTableModel;
import java.util.Vector;

public class ViewStudent extends JFrame implements ActionListener {
    
    JTable table;
    Choice crollno;
    JButton search, print, update, add, cancel;
    
    public ViewStudent() {
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        
        JLabel heading = new JLabel("Search by Roll Number");
        heading.setBounds(20, 20, 150, 20);
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(60, 60, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(780, 10, 60, 60);
            add(image);
            
            JLabel topname = new JLabel("BENOVEN");
            topname.setBounds(400, 20, 150, 30);
            topname.setFont(new Font("serif", Font.BOLD, 20));
            topname.setForeground(new Color(30, 60, 100));
            add(topname);
        } catch (Exception e) {}
        
        crollno = new Choice();
        crollno.setBounds(180, 20, 150, 20);
        add(crollno);
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from student");
            while(rs.next()) {
                crollno.add(rs.getString("rollno"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        table = new JTable();
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from student");
            table.setModel(buildTableModel(rs));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JScrollPane jsp = new JScrollPane(table);
        jsp.setBounds(0, 100, 900, 600);
        add(jsp);
        
        search = new JButton("Search");
        search.setBounds(20, 70, 80, 20);
        search.addActionListener(this);
        add(search);
        
        print = new JButton("Print");
        print.setBounds(120, 70, 80, 20);
        print.addActionListener(this);
        add(print);
        
        add = new JButton("Add");
        add.setBounds(220, 70, 80, 20);
        add.addActionListener(this);
        add(add);
        
        update = new JButton("Update");
        update.setBounds(320, 70, 80, 20);
        update.addActionListener(this);
        add(update);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(420, 70, 80, 20);
        cancel.addActionListener(this);
        add(cancel);
        
        setSize(900, 700);
        setLocation(300, 100);
        setVisible(true);
    }
    
    public static DefaultTableModel buildTableModel(ResultSet rs) throws SQLException {
        ResultSetMetaData metaData = rs.getMetaData();

        // names of columns
        Vector<String> columnNames = new Vector<>();
        int columnCount = metaData.getColumnCount();
        for (int column = 1; column <= columnCount; column++) {
            columnNames.add(metaData.getColumnName(column));
        }

        // data of the table
        Vector<Vector<Object>> data = new Vector<>();
        while (rs.next()) {
            Vector<Object> vector = new Vector<>();
            for (int columnIndex = 1; columnIndex <= columnCount; columnIndex++) {
                vector.add(rs.getObject(columnIndex));
            }
            data.add(vector);
        }

        return new DefaultTableModel(data, columnNames);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == search) {
            String query = "select * from student where rollno = '"+crollno.getSelectedItem()+"'";
            try {
                DBConnection c = new DBConnection();
                ResultSet rs = c.s.executeQuery(query);
                table.setModel(buildTableModel(rs));
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else if (ae.getSource() == print) {
            try {
                table.print();
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else if (ae.getSource() == add) {
            setVisible(false);
            new AddStudent();
        } else if (ae.getSource() == update) {
            // Update logic can be complex, simplifying for this version
            JOptionPane.showMessageDialog(null, "Update module click detected. Implement detailed form here.");
        } else {
            setVisible(false);
        }
    }
    
    public static void main(String[] args) {
        new ViewStudent();
    }
}
```

## ViewTeacher.java
```java
package university_management_system;

import javax.swing.*;
import java.awt.*;
import java.sql.*;
import java.awt.event.*;

import javax.swing.table.DefaultTableModel;
import java.util.Vector;

public class ViewTeacher extends JFrame implements ActionListener {
    
    JTable table;
    Choice cempid;
    JButton search, print, update, add, cancel;
    
    public ViewTeacher() {
        getContentPane().setBackground(Color.WHITE);
        setLayout(null);
        
        JLabel heading = new JLabel("Search by Employee Id");
        heading.setBounds(20, 20, 150, 20);
        add(heading);
        
        try {
            ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/benoven_logo.png"));
            Image i2 = i1.getImage().getScaledInstance(60, 60, Image.SCALE_DEFAULT);
            ImageIcon i3 = new ImageIcon(i2);
            JLabel image = new JLabel(i3);
            image.setBounds(780, 10, 60, 60);
            add(image);
            
            JLabel topname = new JLabel("BENOVEN");
            topname.setBounds(400, 20, 150, 30);
            topname.setFont(new Font("serif", Font.BOLD, 20));
            topname.setForeground(new Color(30, 60, 100));
            add(topname);
        } catch (Exception e) {}
        
        cempid = new Choice();
        cempid.setBounds(180, 20, 150, 20);
        add(cempid);
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from teacher");
            while(rs.next()) {
                cempid.add(rs.getString("emp_id"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        table = new JTable();
        
        try {
            DBConnection c = new DBConnection();
            ResultSet rs = c.s.executeQuery("select * from teacher");
            table.setModel(buildTableModel(rs));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JScrollPane jsp = new JScrollPane(table);
        jsp.setBounds(0, 100, 900, 600);
        add(jsp);
        
        search = new JButton("Search");
        search.setBounds(20, 70, 80, 20);
        search.addActionListener(this);
        add(search);
        
        print = new JButton("Print");
        print.setBounds(120, 70, 80, 20);
        print.addActionListener(this);
        add(print);
        
        add = new JButton("Add");
        add.setBounds(220, 70, 80, 20);
        add.addActionListener(this);
        add(add);
        
        update = new JButton("Update");
        update.setBounds(320, 70, 80, 20);
        update.addActionListener(this);
        add(update);
        
        cancel = new JButton("Cancel");
        cancel.setBounds(420, 70, 80, 20);
        cancel.addActionListener(this);
        add(cancel);
        
        setSize(900, 700);
        setLocation(300, 100);
        setVisible(true);
    }
    
    public static DefaultTableModel buildTableModel(ResultSet rs) throws SQLException {
        ResultSetMetaData metaData = rs.getMetaData();

        // names of columns
        Vector<String> columnNames = new Vector<>();
        int columnCount = metaData.getColumnCount();
        for (int column = 1; column <= columnCount; column++) {
            columnNames.add(metaData.getColumnName(column));
        }

        // data of the table
        Vector<Vector<Object>> data = new Vector<>();
        while (rs.next()) {
            Vector<Object> vector = new Vector<>();
            for (int columnIndex = 1; columnIndex <= columnCount; columnIndex++) {
                vector.add(rs.getObject(columnIndex));
            }
            data.add(vector);
        }

        return new DefaultTableModel(data, columnNames);
    }
    
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == search) {
            String query = "select * from teacher where emp_id = '"+cempid.getSelectedItem()+"'";
            try {
                DBConnection c = new DBConnection();
                ResultSet rs = c.s.executeQuery(query);
                table.setModel(buildTableModel(rs));
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else if (ae.getSource() == print) {
            try {
                table.print();
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else if (ae.getSource() == add) {
            setVisible(false);
            new AddTeacher();
        } else if (ae.getSource() == update) {
            JOptionPane.showMessageDialog(null, "Update module click detected. Implement detailed form here.");
        } else {
            setVisible(false);
        }
    }
    
    public static void main(String[] args) {
        new ViewTeacher();
    }
}
```

