import os
import time

def take_screenshot(driver, username, prefix="before_submit"):
    # Ensure the screenshots directory exists
    if not os.path.exists("results"):
        os.makedirs("results")

    # Generate a timestamped screenshot filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"results/{username}_{timestamp}_{prefix}.png"

    # Save the screenshot
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved at: {screenshot_name}")
