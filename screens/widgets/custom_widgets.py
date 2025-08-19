#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Widgets for SappDriver Application
"""

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.card import Card
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.animation import Animation
from kivy.clock import Clock


class CustomButton(Button):
    """
    Enhanced button with modern styling and animations
    """
    
    def __init__(self, **kwargs):
        # Default styling
        default_kwargs = {
            'background_color': (0.3, 0.6, 0.9, 1),
            'color': (1, 1, 1, 1),
            'font_size': 16,
            'bold': True,
            'size_hint_y': None,
            'height': 50
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        
        self.icon = icon
        self.title = title
        self.description = description
        self.status_color = status_color
        
        # Bind for graphics
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        
        # Add content
        self.add_content()
        
        Clock.schedule_once(lambda dt: self.update_graphics(), 0.1)
    
    def update_graphics(self, *args):
        """
        Draw status card background
        """
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.status_color)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15, 15, 15, 15]
            )
    
    def add_content(self):
        """
        Add icon and text content
        """
        # Icon
        icon_label = Label(
            text=self.icon,
            font_size=24,
            size_hint_x=None,
            width=50,
            halign='center'
        )
        
        # Text content
        text_layout = BoxLayout(orientation='vertical', spacing=5)
        
        title_label = CustomLabel(
            text=self.title,
            font_size=16,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=25
        )
        
        desc_label = CustomLabel(
            text=self.description,
            font_size=12,
            color=(0.9, 0.9, 0.9, 1),
            size_hint_y=None,
            height=20
        )
        
        text_layout.add_widget(title_label)
        text_layout.add_widget(desc_label)
        
        self.add_widget(icon_label)
        self.add_widget(text_layout)
        
        # Bind events for animations
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)
        
        # Draw custom background
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.update_graphics()
    
    def update_graphics(self, *args):
        """
        Update button graphics with rounded corners
        """
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15, 15, 15, 15]
            )
    
    def on_button_press(self, *args):
        """
        Animation when button is pressed
        """
        anim = Animation(
            size=(self.width * 0.95, self.height * 0.95),
            duration=0.1
        )
        anim.start(self)
    
    def on_button_release(self, *args):
        """
        Animation when button is released
        """
        anim = Animation(
            size=(self.width / 0.95, self.height / 0.95),
            duration=0.1
        )
        anim.start(self)


class CustomLabel(Label):
    """
    Enhanced label with modern styling
    """
    
    def __init__(self, **kwargs):
        default_kwargs = {
            'color': (0.2, 0.2, 0.2, 1),
            'font_size': 16,
            'text_size': (None, None),
            'halign': 'center',
            'valign': 'middle'
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        self.bind(size=self.update_text_size)
    
    def update_text_size(self, *args):
        """
        Update text size for proper text wrapping
        """
        self.text_size = (self.width, None)


class WelcomeCard(BoxLayout):
    """
    Welcome card widget with gradient background
    """
    
    def __init__(self, title="Welcome", subtitle="", **kwargs):
        default_kwargs = {
            'orientation': 'vertical',
            'padding': 20,
            'spacing': 10
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        
        self.title = title
        self.subtitle = subtitle
        
        # Bind for custom graphics
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        
        # Add content
        self.add_content()
        
        # Initial graphics
        Clock.schedule_once(lambda dt: self.update_graphics(), 0.1)
    
    def update_graphics(self, *args):
        """
        Draw card background with gradient effect
        """
        self.canvas.before.clear()
        with self.canvas.before:
            # Main background
            Color(0.95, 0.95, 0.98, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20, 20, 20, 20]
            )
            
            # Border
            Color(0.8, 0.8, 0.9, 1)
            Line(
                rounded_rectangle=(
                    self.x, self.y, self.width, self.height, 20
                ),
                width=2
            )
    
    def add_content(self):
        """
        Add title and subtitle to the card
        """
        # Title
        title_label = CustomLabel(
            text=self.title,
            font_size=20,
            bold=True,
            color=(0.2, 0.4, 0.8, 1),
            size_hint_y=None,
            height=30
        )
        
        # Subtitle
        subtitle_label = CustomLabel(
            text=self.subtitle,
            font_size=14,
            color=(0.4, 0.4, 0.4, 1),
            size_hint_y=None,
            height=25
        )
        
        self.add_widget(title_label)
        self.add_widget(subtitle_label)


class NavigationBar(BoxLayout):
    """
    Bottom navigation bar with icons and labels
    """
    
    def __init__(self, **kwargs):
        default_kwargs = {
            'orientation': 'horizontal',
            'size_hint_y': None,
            'height': 70,
            'spacing': 5,
            'padding': [10, 5, 10, 5]
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        
        # Navigation items
        self.nav_items = [
            {'text': '🏠\nخانه', 'key': 'home'},
            {'text': '🚗\nسفرها', 'key': 'trips'},
            {'text': '👤\nپروفایل', 'key': 'profile'},
            {'text': '⚙️\nتنظیمات', 'key': 'settings'}
        ]
        
        self.buttons = {}
        self.create_navigation_items()
        
        # Draw background
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        Clock.schedule_once(lambda dt: self.update_graphics(), 0.1)
    
    def update_graphics(self, *args):
        """
        Draw navigation bar background
        """
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.9, 0.9, 0.95, 1)
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20, 20, 0, 0]
            )
    
    def create_navigation_items(self):
        """
        Create navigation buttons
        """
        for item in self.nav_items:
            btn = Button(
                text=item['text'],
                font_size=12,
                background_color=(0, 0, 0, 0),  # Transparent
                color=(0.4, 0.4, 0.4, 1)
            )
            
            self.buttons[item['key']] = btn
            self.add_widget(btn)
    
    def bind_buttons(self, callbacks):
        """
        Bind callbacks to navigation buttons
        
        Args:
            callbacks (dict): Dictionary mapping button keys to callback functions
        """
        for key, callback in callbacks.items():
            if key in self.buttons:
                self.buttons[key].bind(on_release=lambda x, cb=callback: cb())
    
    def set_active(self, active_key):
        """
        Set active navigation item
        
        Args:
            active_key (str): Key of the active navigation item
        """
        for key, btn in self.buttons.items():
            if key == active_key:
                btn.color = (0.2, 0.4, 0.8, 1)  # Active color
            else:
                btn.color = (0.4, 0.4, 0.4, 1)  # Inactive color


class LoadingSpinner(BoxLayout):
    """
    Loading spinner widget with animation
    """
    
    def __init__(self, **kwargs):
        default_kwargs = {
            'size_hint': (None, None),
            'size': (50, 50)
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        
        # Create spinner
        self.spinner_label = Label(
            text='⟳',
            font_size=30,
            color=(0.3, 0.6, 0.9, 1)
        )
        
        self.add_widget(self.spinner_label)
        
        # Start animation
        self.start_spinning()
    
    def start_spinning(self):
        """
        Start the spinning animation
        """
        def rotate():
            anim = Animation(angle=360, duration=1)
            anim += Animation(angle=720, duration=1)
            anim.repeat = True
            anim.start(self.spinner_label)
        
        Clock.schedule_once(lambda dt: rotate(), 0.1)


class StatusCard(BoxLayout):
    """
    Status card for displaying information with icon and text
    """
    
    def __init__(self, icon="ℹ️", title="", description="", status_color=(0.3, 0.6, 0.9, 1), **kwargs):
        default_kwargs = {
            'orientation': 'horizontal',
            'padding': 15,
            'spacing': 15,
            'size_hint_y': None,
            'height': 80
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
