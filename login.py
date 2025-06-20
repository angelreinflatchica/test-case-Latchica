from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://user.mockplus.com/signin?next=https://www.mockplus.com/blog/post/login-page-examples")
wait = WebDriverWait(driver, 20)

#1st Login
email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".input-text.the-signin-account")))
email.send_keys("angelreinlatchica@gmail.com")
time.sleep(1)

password = driver.find_element(By.ID, "signin-password")
password.send_keys("Pasadonaman123?")
time.sleep(1)

driver.find_element(By.ID, "normal-login").click()
time.sleep(5)

# Nav
avatar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#userInfo .avatar")))
avatar.click()
time.sleep(1.5)

signout_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign out")))
driver.execute_script("arguments[0].style.border='2px solid red'", signout_link)
time.sleep(0.5)

signout_link.click()

wait.until(EC.url_contains("/signin"))
time.sleep(1)

# Login ulit pero wrong password na ilalagay
email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".input-text.the-signin-account")))
email.send_keys("angelreinlatchica@gmail.com")
time.sleep(1)

password = driver.find_element(By.ID, "signin-password")
password.send_keys("Pasado.ba?")
time.sleep(1)

driver.find_element(By.ID, "normal-login").click()
time.sleep(3)

forgot_link = wait.until(EC.element_to_be_clickable((By.ID, "forget-password")))
driver.execute_script("arguments[0].style.border='3px solid red'", forgot_link)
time.sleep(1)

forgot_link.click()

wait.until(EC.url_contains("/forgotpassword"))

# forgot password form naman to
forgot_email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input-text[placeholder='Enter your email']")))
forgot_email.send_keys("angelreinlatchica@gmail.com")
time.sleep(1)

reset_btn = driver.find_element(By.ID, "reset-first-button")
reset_btn.click()
time.sleep(1)

reset_link = input("📧 Check your email and paste the reset link here: ")
driver.get(reset_link)
input("Paused. Press Enter to continue...")

time.sleep(5)

new_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='New password']")))
new_password.send_keys("Pasadonaman1234?")
time.sleep(2)

confirm_password = driver.find_element(By.XPATH, "//input[@placeholder='Confirm new password']")
confirm_password.send_keys("Pasadonaman1234?")
time.sleep(2)

reset_button = driver.find_element(By.ID, "reset-password-button")
driver.execute_script("arguments[0].classList.remove('disabled')", reset_button)
reset_button.click()
time.sleep(5)

print("✅ Password reset completed.")

sign_in_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/signin' and contains(@class, 'button')]")))
sign_in_button.click()

wait.until(EC.url_contains("/signin"))
time.sleep(5)

# Login ulit using new password
email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".input-text.the-signin-account")))
email.send_keys("angelreinlatchica@gmail.com")
time.sleep(1)

password = driver.find_element(By.ID, "signin-password")
password.send_keys("Pasadonaman1234?")
time.sleep(1)

driver.find_element(By.ID, "normal-login").click()

time.sleep(20)
driver.quit()