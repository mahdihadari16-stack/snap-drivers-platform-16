#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main Screen - SappDriver Application
"""

from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger
from kivy.animation import Animation
from kivy.clock import Clock

from widgets.custom_widgets import (
    CustomButton, 
    CustomLabel, 
    WelcomeCard,
    NavigationBar
)


class MainScreen(Screen):
    """
    Main Screen Class - Home page of the application
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_screen()
        
    def build_screen(self):
        """
        Build the main screen layout
        """
        # Main container
        main_layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15
        )
        
        # Add header
        self.add_header(main_layout)
        
        # Add welcome section
        self.add_welcome_section(main_layout)
        
        # Add main content
        self.add_main_content(main_layout)
        
        # Add navigation bar
        self.add_navigation_bar(main_layout)
        
        self.add_widget(main_layout)
    
    def add_header(self, parent_layout):
        """
        Add header section with app title and user info
        """
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=60
        )
        
        # App title
        title_label = CustomLabel(
            text="SappDriver",
            font_size=24,
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        
        # User profile button
        profile_btn = CustomButton(
            text="Profile",
            size_hint_x=None,
            width=80,
            background_color=(0.3, 0.7, 0.3, 1)
        )
        profile_btn.bind(on_release=self.go_to_profile)
        
        header_layout.add_widget(title_label)
        header_layout.add_widget(profile_btn)
        parent_layout.add_widget(header_layout)
    
    def add_welcome_section(self, parent_layout):
        """
        Add welcome card section
        """
        welcome_card = WelcomeCard(
            title="خوش آمدید!",
            subtitle="به اپلیکیشن SappDriver خوش آمدید",
            size_hint_y=None,
            height=120
        )
        
        parent_layout.add_widget(welcome_card)
    
    def add_main_content(self, parent_layout):
        """
        Add main content with feature buttons
        """
        content_layout = GridLayout(
            cols=2,
            spacing=15,
            size_hint_y=0.6
        )
        
        # Feature buttons
        features = [
            {
                "text": "🚗 شروع سفر",
                "color": (0.2, 0.7, 0.3, 1),
                "action": self.start_trip
            },
            {
                "text": "📍 مکان‌های من", 
                "color": (0.7, 0.3, 0.3, 1),
                "action": self.show_locations
            },
            {
                "text": "📊 آمار سفرها",
                "color": (0.3, 0.3, 0.7, 1),
                "action": self.show_statistics
            },
            {
                "text": "⚙️ تنظیمات",
                "color": (0.6, 0.4, 0.2, 1),
                "action": self.go_to_settings
            }
        ]
        
        for feature in features:
            btn = CustomButton(
                text=feature["text"],
                background_color=feature["color"],
                font_size=16
            )
            btn.bind(on_release=lambda x, action=feature["action"]: action())
            content_layout.add_widget(btn)
        
        parent_layout.add_widget(content_layout)
    
    def add_navigation_bar(self, parent_layout):
        """
        Add bottom navigation bar
        """
        nav_bar = NavigationBar()
        nav_bar.bind_buttons({
            'home': self.stay_on_main,
            'trips': self.show_trips,
            'profile': self.go_to_profile,
            'settings': self.go_to_settings
        })
        
        parent_layout.add_widget(nav_bar)
    
    def on_enter(self):
        """
        Called when screen is entered
        """
        Logger.info("MainScreen: Entered main screen")
        self.animate_entrance()
    
    def animate_entrance(self):
        """
        Animate screen entrance
        """
        # Fade in animation
        self.opacity = 0
        anim = Animation(opacity=1, duration=0.5)
        anim.start(self)
    
    # Button callback methods
    def start_trip(self):
        """Start a new trip"""
        Logger.info("MainScreen: Starting new trip")
        # TODO: Implement trip start functionality
        pass
    
    def show_locations(self):
        """Show saved locations"""
        Logger.info("MainScreen: Showing locations")
        # TODO: Implement locations screen
        pass
    
    def show_statistics(self):
        """Show trip statistics"""
        Logger.info("MainScreen: Showing statistics")
        # TODO: Implement statistics screen
        pass
    
    def show_trips(self):
        """Show trip history"""
        Logger.info("MainScreen: Showing trips")
        # TODO: Implement trips screen
        pass
    
    def go_to_profile(self, *args):
        """Navigate to profile screen"""
        Logger.info("MainScreen: Navigating to profile")
        self.manager.current = "profile"
    
    def go_to_settings(self, *args):
        """Navigate to settings screen"""
        Logger.info("MainScreen: Navigating to settings")
        self.manager.current = "settings"
    
    def stay_on_main(self, *args):
        """Stay on main screen (for nav bar)"""
        pass
