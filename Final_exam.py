from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost/ocss-master/admin_login.php")
wait = WebDriverWait(driver, 10)

#Login as Admin with Wrong password
email = driver.find_element(By.NAME, "admin_username")
email.send_keys("admin")
time.sleep(1)

password = driver.find_element(By.NAME, "admin_pass")
password.send_keys("admin2")
time.sleep(1)

login_button = driver.find_element(By.NAME, "admin_login")
login_button.click()

# 2nd login with correct password
time.sleep(5)
email = driver.find_element(By.NAME, "admin_username")
email.send_keys("admin")
time.sleep(1)

password = driver.find_element(By.NAME, "admin_pass")
password.send_keys("admin")
time.sleep(1)

login_button = driver.find_element(By.NAME, "admin_login")
login_button.click()
time.sleep(2)

# Sidebar menu
sidenav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
sidenav.click()
time.sleep(3)

# Proceed to Add faculty
add_faculty_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Add Faculty"))
)
add_faculty_link.click()
time.sleep(2)

# Fill out the Faculty form
# emp_num = wait.until(EC.presence_of_element_located((By.NAME, "emp_number"))) #try natin na wag lagyan ang emp num field para ma-catch as error
# emp_num.send_keys("041504")
# time.sleep(1)

name_field = driver.find_element(By.NAME, "fname")
name_field.send_keys("Latchica, Angel Rein F.")
time.sleep(1)

date_field = driver.find_element(By.ID, "date_hired")
date_field.click()
date_field.send_keys("01-04-2025")
time.sleep(1)

status_dropdown = Select(driver.find_element(By.ID, "status"))
status_dropdown.select_by_visible_text("Full-time Faculty")
time.sleep(1)

expertise_field = driver.find_element(By.NAME, "background_field")
expertise_field.send_keys("Technical Support & QA")
time.sleep(1)

address_field = driver.find_element(By.NAME, "address")
address_field.send_keys("Brgy. Sipa II, Padre Burgos, Quezon")
time.sleep(1)

contact_num_field = driver.find_element(By.NAME, "contact_no")
contact_num_field.send_keys("09464739613")
time.sleep(1)

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("angelreingmail.com")
time.sleep(1)

pass_field = driver.find_element(By.NAME, "pass")
pass_field.send_keys("pasadongfinals!")
time.sleep(1)

add_faculty = driver.find_element(By.NAME, "register_faculty")
add_faculty.click()
time.sleep(3)
        
# Check for validation errors
try:
    email_error = driver.find_element(By.ID, "email-error")
    print("Email Error:", email_error.text)
except:
    print("No email error shown.")

try:
    emp_error = driver.find_element(By.ID, "emp_number-error")
    print("Employee Number Error:", emp_error.text)
except:
    print("No employee number error shown.")

try:
    pass_error = driver.find_element(By.ID, "pass-error")
    print("Password Error:", pass_error.text)
except:
    print("No password error shown.")

# Now the addding emp num field
time.sleep(2)
emp_num = wait.until(EC.presence_of_element_located((By.NAME, "emp_number")))
emp_num.send_keys("041504")
time.sleep(1)

add_faculty = driver.find_element(By.NAME, "register_faculty")
add_faculty.click()
time.sleep(3)

# Now with correct email naman
email_field = driver.find_element(By.NAME, "email")
email_field.clear()
email_field.send_keys("angelrein@gmail.com")
time.sleep(1)

add_faculty = driver.find_element(By.NAME, "register_faculty")
add_faculty.click()
time.sleep(3)
print("Form resubmitted with valid employee number and email.")

# Sidebar menu
sidenav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
sidenav.click()
time.sleep(3)

# Proceed to Add Subject
add_subject_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Add Subject"))
)
add_subject_link.click()
time.sleep(2)

sub_code_field = driver.find_element(By.NAME, "subject_code")
sub_code_field.send_keys("CS101")
time.sleep(1)

sub_description_field = driver.find_element(By.NAME, "subject_description")
sub_description_field.send_keys("Introduction to Computer Science")
time.sleep(1)

unit_dropdown = Select(driver.find_element(By.ID, "unit"))
unit_dropdown.select_by_visible_text("3")
time.sleep(1)

lecture_dropdown = Select(driver.find_element(By.ID, "lecture"))
lecture_dropdown.select_by_visible_text("3")
time.sleep(1)

lab_dropdown = Select(driver.find_element(By.ID, "laboratory"))
lab_dropdown.select_by_visible_text("3")
time.sleep(1)

add_sub = driver.find_element(By.NAME, "add")
add_sub.click()
time.sleep(3)

# Sidebar menu
sidenav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
sidenav.click()
time.sleep(3)

# Add room
add_room_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Add Room"))
)
time.sleep(1)
add_room_link.click()
time.sleep(2)

room = driver.find_element(By.NAME, "room")
room.send_keys("105")
time.sleep(1)

add_room = driver.find_element(By.NAME, "add_room")
add_room.click()
time.sleep(3)

# Sidebar menu
sidenav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
sidenav.click()
time.sleep(3)

# Proceed to Create Schedule
create_schedule_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Create Schedule"))
)
time.sleep(1)
create_schedule_link.click()
time.sleep(2)

sub_description_dropdown = Select(driver.find_element(By.ID, "subject_description"))
sub_description_dropdown.select_by_visible_text("Introduction to Computer Science")
time.sleep(1)

days_dropdown = Select(driver.find_element(By.ID, "day_description"))
days_dropdown.select_by_visible_text("S")
time.sleep(1)

time_dropdown = Select(driver.find_element(By.ID, "time_description"))
time_dropdown.select_by_visible_text("5:30-8:30")
time.sleep(1)

room_dropdown = Select(driver.find_element(By.ID, "room_description"))
room_dropdown.select_by_visible_text("108")
time.sleep(1)

prof_dropdown = Select(driver.find_element(By.ID, "fname"))
prof_dropdown.select_by_visible_text("Latchica, Angel Rein F.")
time.sleep(1)

# For handling error
try:
    add_sched = driver.find_element(By.NAME, "add_schedule")
    add_sched.click()
    time.sleep(5)
    print("Schedule submitted successfully.")
except Exception as e:
    print("Failed to submit schedule:", e)
    
    time.sleep(5)

try:
    driver.get("http://localhost/ocss-master/admin.php")
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Admin Dashboard')]")))
    print("📄 Returned to admin.php successfully.")
    time.sleep(3)
except Exception as e:
    print("⚠️ Could not navigate back to admin.php:", e)
    
# Sidebar menu
sidenav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
sidenav.click()
time.sleep(3)

try:
    logout_link = driver.find_element(By.LINK_TEXT, "Log Out")
    logout_link.click()
    print("Logged out successfully.")
    time.sleep(3)
except Exception as e:
    print("Logout failed:", e)

# After Admin logs out, mag reredirect naman sya sa user/faculty Sign in Page
driver.get("http://localhost/ocss-master/index.php")
wait.until(EC.presence_of_element_located((By.NAME, "user_email")))
time.sleep(1)

user_email = driver.find_element(By.NAME, "user_email")
user_email.send_keys("angelrein@gmail.com")
time.sleep(1)

user_password = driver.find_element(By.NAME, "user_pass")
user_password.send_keys("pasadongfinals!")
time.sleep(1)

login_button = driver.find_element(By.NAME, "Login")
login_button.click()
time.sleep(2)

wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Profile")))

profile_link = driver.find_element(By.LINK_TEXT, "Profile")
profile_link.click()
time.sleep(7)

logout_link = driver.find_element(By.XPATH, "//a[@href='user_logout.php']")
logout_link.click()
time.sleep(4)

driver.quit()