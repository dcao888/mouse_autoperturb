from datetime import datetime, timedelta
import time 
import logging 
import numpy as np
import pyautogui

class Mouse:

    def __init__(self):
        
        # dimension of screen
        self.screen_size_x = pyautogui.size()[0]
        self.screen_size_y = pyautogui.size()[1]
        self.screen_center = (0.5*self.screen_size_x, 0.5*self.screen_size_y)


    def perturb(self):
        """
        Perturb mouse to a random co-ordinate center around the screen center 
        """

        # random co-ordinates around center
        x_rand = np.random.normal(loc = self.screen_center[0], scale = 1)
        y_rand = np.random.normal(loc = self.screen_center[1], scale = 1)

        # truncate random co-ordinates 
        x = min(max(0, x_rand), self.screen_size_x)
        y = min(max(0, y_rand), self.screen_size_y)
        
        pyautogui.moveTo(x, y)


    def perturb_autopilot(self, period = 5, duration = 60):
        """
        Perturb mouse every 'period' seconds for a total 'duration' seconds 
        """
        end_dttm = datetime.now() + timedelta(seconds = duration)
        
        while datetime.now() < end_dttm:
            self.perturb()
            # snooze to save CPU
            logging.info("zZz...") 
            time.sleep(period)
        


