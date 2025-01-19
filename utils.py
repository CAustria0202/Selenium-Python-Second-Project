import os
import time

def take_screenshot(driver, directory="results", filename_prefix="screenshot"):
    """
    Captures a screenshot of the current browser state.

    :param driver: The WebDriver instance.
    :param directory: The directory to save the screenshot. Defaults to "results".
    :param filename_prefix: Prefix for the screenshot filename. Defaults to "screenshot".
    """
    # Ensure the specified directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a timestamped screenshot filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = os.path.join(directory, f"{filename_prefix}_{timestamp}.png")

    # Save the screenshot
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved at: {screenshot_name}")
