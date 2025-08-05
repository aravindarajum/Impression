import os
from datetime import datetime

class ScreenshotUtils:
    @staticmethod
    def capture_screenshot(driver, test_name, status=""):
        """Capture screenshot and return the file path"""
        try:
            # Create Screenshots directory if it doesn't exist
            os.makedirs("Screenshots", exist_ok=True)
            
            # Generate timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Create filename
            if status:
                filename = f"{test_name}_{status}_{timestamp}.png"
            else:
                filename = f"{test_name}_{timestamp}.png"
            
            # Full path
            screenshot_path = os.path.join("Screenshots", filename)
            
            # Capture screenshot
            driver.save_screenshot(screenshot_path)
            
            return screenshot_path
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
            return None