#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Settings Screen - SappDriver Application
"""

from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.logger import Logger
from kivy.animation import Animation

from widgets.custom_widgets import (
    CustomButton, 
    CustomLabel,
    StatusCard
)
from utils.database import DatabaseManager
from utils.helpers import ThemeManager, LanguageManager


class SettingItem(BoxLayout):
    """
    Individual setting item with label and control
    """
    
    def __init__(self, title, subtitle="", control_widget=None, **kwargs):
        default_kwargs = {
            'orientation': 'horizontal',
            'size_hint_y': None,
            'height': 70,
            'padding': [20, 10, 20, 10],
            'spacing': 15
        }
        default_kwargs.update(kwargs)
        
        super().__init__(**default_kwargs)
        
        # Text section
        text_layout = BoxLayout(orientation='vertical', spacing=5)
        
        title_label = CustomLabel(
            text=title,
            font_size=16,
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='right',
            size_hint_y=None,
            height=25
        )
        
        if subtitle:
            subtitle_label = CustomLabel(
                text=subtitle,
                font_size=12,
                color=(0.5, 0.5, 0.5, 1),
                halign='right',
                size_hint_y=None,
                height=20
            )
            text_layout.add_widget(title_label)
            text_layout.add_widget(subtitle_label)
        else:
            text_layout.add_widget(title_label)
        
        # Control widget
        control_container = BoxLayout(
            size_hint_x=None,
            width=100
        )
        
        if control_widget:
            control_container.add_widget(control_widget)
        
        self.add_widget(text_layout)
        self.add_widget(control_container)


class SettingsScreen(Screen):
    """
    Settings Screen Class - Application configuration
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Initialize managers
        self.db_manager = DatabaseManager()
        self.theme_manager = ThemeManager()
        self.language_manager = LanguageManager()
        
        # Settings data
        self.current_settings = {}
        
        self.build_screen()
        self.load_current_settings()
    
    def build_screen(self):
        """
        Build the settings screen layout
        """
        # Main container
        main_layout = BoxLayout(
            orientation='vertical',
            padding=[0, 20, 0, 0]
        )
        
        # Add header
        self.add_header(main_layout)
        
        # Add scrollable content
        self.add_scrollable_content(main_layout)
        
        # Add action buttons
        self.add_action_buttons(main_layout)
        
        self.add_widget(main_layout)
    
    def add_header(self, parent_layout):
        """
        Add header with title and back button
        """
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=60,
            padding=[20, 0, 20, 0]
        )
        
        # Back button
        back_btn = CustomButton(
            text='← بازگشت',
            size_hint_x=None,
            width=100,
            background_color=(0.6, 0.6, 0.6, 1),
            height=40
        )
        back_btn.bind(on_release=self.go_back)
        
        # Title
        title_label = CustomLabel(
            text='تنظیمات',
            font_size=24,
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        
        header_layout.add_widget(back_btn)
        header_layout.add_widget(title_label)
        
        parent_layout.add_widget(header_layout)
    
    def add_scrollable_content(self, parent_layout):
        """
        Add scrollable settings content
        """
        scroll = ScrollView()
        content_layout = BoxLayout(
            orientation='vertical',
            spacing=2,
            size_hint_y=None
        )
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # Add settings sections
        self.add_appearance_settings(content_layout)
        self.add_language_settings(content_layout)
        self.add_notification_settings(content_layout)
        self.add_privacy_settings(content_layout)
        self.add_about_settings(content_layout)
        
        scroll.add_widget(content_layout)
        parent_layout.add_widget(scroll)
    
    def add_appearance_settings(self, parent_layout):
        """
        Add appearance settings section
        """
        # Section header
        section_header = CustomLabel(
            text='🎨 ظاهر و نمایش',
            font_size=18,
            bold=True,
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40,
            halign='right',
            padding=[20, 10, 20, 10]
        )
        parent_layout.add_widget(section_header)
        
        # Theme toggle
        self.theme_switch = Switch(active=False)
        theme_item = SettingItem(
            title='تم تاریک',
            subtitle='استفاده از تم تاریک برای محافظت از چشم',
            control_widget=self.theme_switch
        )
        self.theme_switch.bind(active=self.on_theme_change)
        
        # Font size slider
        self.font_slider = Slider(
            min=12, max=20, value=16, step=1,
            size_hint_x=None, width=80
        )
        font_item = SettingItem(
            title='اندازه فونت',
            subtitle='تغییر اندازه متن در اپلیکیشن',
            control_widget=self.font_slider
        )
        self.font_slider.bind(value=self.on_font_size_change)
        
        parent_layout.add_widget(theme_item)
        parent_layout.add_widget(font_item)
    
    def add_language_settings(self, parent_layout):
        """
        Add language settings section
        """
        # Section header
        section_header = CustomLabel(
            text='🌐 زبان',
            font_size=18,
            bold=True,
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40,
            halign='right',
            padding=[20, 10, 20, 10]
        )
        parent_layout.add_widget(section_header)
        
        # Language spinner
        self.language_spinner = Spinner(
            text='فارسی',
            values=['فارسی', 'English'],
            size_hint_x=None,
            width=100
        )
        lang_item = SettingItem(
            title='زبان اپلیکیشن',
            subtitle='انتخاب زبان رابط کاربری',
            control_widget=self.language_spinner
        )
        self.language_spinner.bind(text=self.on_language_change)
        
        parent_layout.add_widget(lang_item)
    
    def add_notification_settings(self, parent_layout):
        """
        Add notification settings section
        """
        # Section header
        section_header = CustomLabel(
            text='🔔 اعلان‌ها',
            font_size=18,
            bold=True,
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40,
            halign='right',
            padding=[20, 10, 20, 10]
        )
        parent_layout.add_widget(section_header)
        
        # Push notifications
        self.push_notifications_switch = Switch(active=True)
        push_item = SettingItem(
            title='اعلان‌های فوری',
            subtitle='دریافت اعلان‌های مهم',
            control_widget=self.push_notifications_switch
        )
        self.push_notifications_switch.bind(active=self.on_notifications_change)
        
        # Sound
        self.sound_switch = Switch(active=True)
        sound_item = SettingItem(
            title='صدای اعلان',
            subtitle='پخش صدا هنگام دریافت اعلان',
            control_widget=self.sound_switch
        )
        self.sound_switch.bind(active=self.on_sound_change)
        
        parent_layout.add_widget(push_item)
        parent_layout.add_widget(sound_item)
    
    def add_privacy_settings(self, parent_layout):
        """
        Add privacy settings section
        """
        # Section header
        section_header = CustomLabel(
            text='🔒 حریم خصوصی',
            font_size=18,
            bold=True,
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40,
            halign='right',
            padding=[20, 10, 20, 10]
        )
        parent_layout.add_widget(section_header)
        
        # Data collection
        self.data_collection_switch = Switch(active=False)
        data_item = SettingItem(
            title='جمع‌آوری داده‌ها',
            subtitle='اجازه جمع‌آوری داده‌ها برای بهبود خدمات',
            control_widget=self.data_collection_switch
        )
        self.data_collection_switch.bind(active=self.on_data_collection_change)
        
        # Location tracking
        self.location_switch = Switch(active=True)
        location_item = SettingItem(
            title='ردیابی موقعیت',
            subtitle='استفاده از موقعیت جغرافیایی',
            control_widget=self.location_switch
        )
        self.location_switch.bind(active=self.on_location_change)
        
        parent_layout.add_widget(data_item)
        parent_layout.add_widget(location_item)
    
    def add_about_settings(self, parent_layout):
        """
        Add about and help settings section
        """
        # Section header
        section_header = CustomLabel(
            text='ℹ️ درباره برنامه',
            font_size=18,
            bold=True,
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40,
            halign='right',
            padding=[20, 10, 20, 10]
        )
        parent_layout.add_widget(section_header)
        
        # Version info
        version_card = StatusCard(
            icon='📱',
            title='نسخه اپلیکیشن',
            description='1.0.0',
            status_color=(0.5, 0.7, 0.9, 1)
        )
        
        # Help button
        help_btn = CustomButton(
            text='راهنما و پشتیبانی',
            background_color=(0.3, 0.6, 0.9, 1),
            size_hint_y=None,
            height=50
        )
        help_btn.bind(on_release=self.show_help)
        
        # About button  
        about_btn = CustomButton(
            text='درباره توسعه‌دهنده',
            background_color=(0.6, 0.4, 0.8, 1),
            size_hint_y=None,
            height=50
        )
        about_btn.bind(on_release=self.show_about)
        
        parent_layout.add_widget(version_card)
        parent_layout.add_widget(help_btn)
        parent_layout.add_widget(about_btn)
    
    def add_action_buttons(self, parent_layout):
        """
        Add action buttons (save, reset, etc.)
        """
        button_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=60,
            padding=[20, 10, 20, 10],
            spacing=10
        )
        
        # Reset button
        reset_btn = CustomButton(
            text='بازنشانی',
            background_color=(0.8, 0.4, 0.4,
