#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SappDriver - Main Application File
A modern mobile application built with Kivy Framework

Author: Mahdi Hadari
Version: 1.0.0
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Kivy imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.logger import Logger
from kivy.config import Config

# Project imports
from screens.main_screen import MainScreen
from screens.login_screen import LoginScreen
from screens.settings_screen import SettingsScreen
from screens.profile_screen import ProfileScreen
from utils.database import DatabaseManager
from utils.helpers import ThemeManager, LanguageManager

# Configure Kivy before importing other modules
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)


class SappDriverApp(App):
    """
    Main Application Class
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "SappDriver"
        self.icon = "assets/icons/app_icon.png"
        
        # Initialize managers
        self.db_manager = DatabaseManager()
        self.theme_manager = ThemeManager()
        self.language_manager = LanguageManager()
        
        # Screen manager
        self.screen_manager = None
        
    def build(self):
        """
        Build the application
        """
        Logger.info("SappDriver: Building application...")
        
        # Initialize database
        self.db_manager.initialize_database()
        
        # Create screen manager
        self.screen_manager = ScreenManager()
        
        # Add screens
        self.add_screens()
        
        # Load user settings
        self.load_user_settings()
        
        Logger.info("SappDriver: Application built successfully")
        return self.screen_manager
    
    def add_screens(self):
        """
        Add all screens to screen manager
        """
        screens = [
            ("login", LoginScreen(name="login")),
            ("main", MainScreen(name="main")),
            ("settings", SettingsScreen(name="settings")),
            ("profile", ProfileScreen(name="profile")),
        ]
        
        for screen_name, screen_obj in screens:
            self.screen_manager.add_widget(screen_obj)
            Logger.info(f"SappDriver: Added screen '{screen_name}'")
    
    def load_user_settings(self):
        """
        Load user settings from database
        """
        try:
            settings = self.db_manager.get_user_settings()
            
            # Apply theme
            theme = settings.get('theme', 'light')
            self.theme_manager.set_theme(theme)
            
            # Apply language
            language = settings.get('language', 'en')
            self.language_manager.set_language(language)
            
            Logger.info(f"SappDriver: Loaded settings - Theme: {theme}, Language: {language}")
            
        except Exception as e:
            Logger.error(f"SappDriver: Error loading settings: {e}")
    
    def on_start(self):
        """
        Called when the application starts
        """
        Logger.info("SappDriver: Application started")
        
        # Check if user is logged in
        if self.db_manager.is_user_logged_in():
            self.screen_manager.current = "main"
        else:
            self.screen_manager.current = "login"
    
    def on_stop(self):
        """
        Called when the application stops
        """
        Logger.info("SappDriver: Application stopping...")
        
        # Close database connection
        self.db_manager.close_connection()
        
        Logger.info("SappDriver: Application stopped")
    
    def on_pause(self):
        """
        Called when the application is paused (mobile)
        """
        Logger.info("SappDriver: Application paused")
        return True
    
    def on_resume(self):
        """
        Called when the application resumes from pause
        """
        Logger.info("SappDriver: Application resumed")


def main():
    """
    Main function to run the application
    """
    try:
        # Create and run the application
        app = SappDriverApp()
        app.run()
        
    except KeyboardInterrupt:
        Logger.info("SappDriver: Application interrupted by user")
        sys.exit(0)
        
    except Exception as e:
        Logger.error(f"SappDriver: Fatal error - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
