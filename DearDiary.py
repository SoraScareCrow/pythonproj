import json
import tkinter as tk
from tkinter import filedialog, ttk, colorchooser
import sys
import os

"""
# Text Editor

This is a simple text editor implemented using Python and Tkinter.

## Features

- Multiple tabs for editing multiple documents
- Undo and redo functionality
- Save and open files
- Formatting options such as bold, italic, underline
- Color chooser for changing text color
- Emoji panel for inserting emojis
- It saves all progress user left before closing and returns it back

## How to Use

- To create a new tab, click on the "+" button in the toolbar.
- To close the current tab, click on the "x" button in the toolbar.
- To open a file, go to the "File" menu and select "Open".
- To save the current tab content to a file, go to the "File" menu and select "Save".
- To apply formatting to the selected text, use the style and color buttons in the toolbar.
- To insert an emoji, click on the emoji button in the toolbar and select an emoji from the panel.

## Requirements

- Python 3.x
- Tkinter

"""

class Notepad:
    """@class Notepad @brief This class represents a Notepad in UTF-8 format with additional features like emojis,
    changing text style, and coloring. @details The Notepad includes various functionalities, including a file menu for
    opening and saving files, a tabs menu for managing multiple tabs, an options' menu, and a help menu.

    @note The emoji, text style, and color functionality are available via a hidden side panel that can be toggled on
    and off."""
    def __init__(self, root):
        self.root = root
        self.root.title("UTF-8 Notepad")
        self.root.geometry("925x600")
        self.side_panel = None
        self.side_panel_width = 200

        # Create a main frame for grid layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Tools bar
        self.tool_bar = ttk.Frame(self.main_frame)
        self.tool_bar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Side panel (initially hidden)
        self.side_panel = tk.Canvas(self.main_frame, bg='grey', width=self.side_panel_width)
        self.side_panel_frame = tk.Frame(self.side_panel, bg='grey')
        self.side_panel_frame.bind("<Configure>", self.update_scrollregion)
        self.side_panel_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.side_panel.yview)
        self.side_panel.configure(yscrollcommand=self.side_panel_scrollbar.set)
        self.side_panel_window = self.side_panel.create_window((0, 0), window=self.side_panel_frame, anchor="nw")

        # Tab bar
        self.tab_bar = ttk.Notebook(self.main_frame)
        self.tab_bar.grid(row=1, column=2, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)  # Side Panel
        self.main_frame.columnconfigure(1, weight=0)  # Scrollbar
        self.main_frame.columnconfigure(2, weight=4)  # Tabs bar
        self.main_frame.rowconfigure(1, weight=1)

        # Initially hiding the side panel and its scrollbar
        self.side_panel.grid_forget()
        self.side_panel_scrollbar.grid_forget()

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)

        # Tabs menu
        self.tabs_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tabs", menu=self.tabs_menu)
        self.tabs_menu.add_command(label="New Tab", command=self.new_tab)
        self.tabs_menu.add_command(label="Close Current Tab", command=self.close_current_tab)
        self.tabs_menu.add_command(label="Close All Tabs", command=self.close_all_tabs)

        # Options menu
        self.options_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options_menu)

        # Help menu
        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Readme", command=self.display_readme)

        # Add Tab button
        self.add_tab_btn = tk.Label(self.tool_bar, text="➕", bg="white", relief="solid", bd=1)
        self.add_tab_btn.bind("<Button-1>", lambda e: self.new_tab())
        self.add_tab_btn.pack(side=tk.LEFT)

        # Close Tab button
        self.close_tab_btn = tk.Label(self.tool_bar, text="❌", bg="white", relief="solid", bd=1)
        self.close_tab_btn.bind("<Button-1>", lambda e: self.close_current_tab())
        self.close_tab_btn.pack(side=tk.LEFT)

        # Emoji button
        self.emoji_btn = tk.Label(self.tool_bar, text="🤡", bg="white", relief="solid", bd=1)
        self.emoji_btn.bind("<Button-1>", lambda e: self.toggle_emoji_panel())
        self.emoji_btn.pack(side=tk.LEFT)

        # Style changer button
        self.style_btn = tk.Label(self.tool_bar, text="🖉", bg="white", relief="solid", bd=1)
        self.style_btn.bind("<Button-1>", lambda e: self.change_style())
        self.style_btn.pack(side=tk.LEFT)

        # Color changer button
        self.color_btn = tk.Label(self.tool_bar, text="🖌", bg="white", relief="solid", bd=1)
        self.color_btn.bind("<Button-1>", lambda e: self.toggle_color_chooser())
        self.color_btn.pack(side=tk.LEFT)
        # Load the saved state of all tabs
        self.load_state()
        # Add copy and paste buttons
        self.copy_btn = tk.Label(self.tool_bar, text="⮬💾", bg="white", relief="solid", bd=1)
        self.copy_btn.bind("<Button-1>", self.copy_text)
        self.copy_btn.pack(side=tk.LEFT)

        self.paste_btn = tk.Label(self.tool_bar, text="⮯💾", bg="white", relief="solid", bd=1)
        self.paste_btn.bind("<Button-1>", self.paste_text)
        self.paste_btn.pack(side=tk.LEFT)
        # Ensure the state is saved when the application is closed
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.new_tab()

    def update_scrollregion(self, event=None):
        """
        @brief Updates the scroll region.
        @param event: This is an optional parameter defaulting to None.
        """
        self.side_panel.configure(scrollregion=self.side_panel.bbox("all"))

    def new_tab(self, title=None, content=""):
        """
        @brief Creates a new tab with optional content.
        @param title: Title of the new tab. Default is None, which means a new tab is being created.
        @param content: Content of the new tab. Default is empty string.
        """
        # Create a new tab with a Text widget
        tab = tk.Frame(self.tab_bar)
        text_area = tk.Text(tab, undo=True)
        text_area.pack(expand=1, fill='both')

        # Insert the given content into the text widget
        text_area.insert(tk.END, content)

        # Add the new tab to the tab bar
        # If title is not given, assign a new tab title
        if title is None:
            title = "Tab " + str(len(self.tab_bar.tabs()) + 1)
        self.tab_bar.add(tab, text=title)

    def toggle_side_panel(self):
        """
        @brief Toggles the visibility of the side panel.
        """
        if self.side_panel.winfo_ismapped():
            self.side_panel.grid_forget()
            self.side_panel_scrollbar.grid_forget()
        else:
            self.side_panel.grid(row=1, column=0, sticky="ns")
            self.side_panel_scrollbar.grid(row=1, column=1, sticky="ns")

        # Configure the side panel to not propagate resizing
        self.side_panel.grid_propagate(0)

    def close_current_tab(self):
        """
        @brief Closes the current tab.
        """
        # Close the current tab
        if len(self.tab_bar.tabs()) > 0:
            self.tab_bar.forget(self.tab_bar.select())


    def close_all_tabs(self):
        """
        @brief Closes all tabs.
        """
        # Close all tabs
        for tab in self.tab_bar.tabs():
            self.tab_bar.forget(tab)

    def open_file(self):
        """
        @brief Opens a file from a file dialog and loads its content into a new tab.
        """
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                content = file.read()

            # Create a new tab
            self.new_tab()

            # Get the text widget in the new tab
            current_tab = self.tab_bar.select()
            text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]

            # Insert the file content
            text_widget.insert(tk.END, content)

            # Update the tab title
            self.tab_bar.tab(current_tab, text=os.path.basename(filepath))

    def save_file(self):
        """
        @brief Open a file dialog and save the current tab content to the selected file
        """
        current_tab = self.tab_bar.select()
        text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
        content = text_widget.get(1.0, tk.END)
        filepath = filedialog.asksaveasfilename()

        if filepath:
            # Specify the encoding as UTF-8 when opening the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)

            # Update the tab title
            self.tab_bar.tab(current_tab, text=os.path.basename(filepath))



    def toggle_emoji_panel(self):
        """
        ## @brief Toggles the visibility of the emoji panel.
        """
        # Toggle visibility of the emoji panel
        if self.side_panel.winfo_ismapped():
            self.side_panel.grid_forget()
            self.side_panel_scrollbar.grid_forget()
        else:
            self.side_panel.grid(row=1, column=0, sticky="ns")
            self.side_panel_scrollbar.grid(row=1, column=1, sticky="ns")

        # Clear the side panel frame
        for widget in self.side_panel_frame.winfo_children():
            widget.destroy()

        # Create a function to add a category
        def add_category(name, start, end):
            # Add a category label
            category_label = tk.Label(self.side_panel_frame, text=name, bg="white")
            category_label.pack(fill=tk.X)

            # Add emojis in rows of 4
            for i in range(start, end + 1, 6):
                row_frame = tk.Frame(self.side_panel_frame)
                row_frame.pack(fill=tk.X)
                for j in range(i, min(i + 6, end + 1)):
                    btn = tk.Button(row_frame, text=chr(j), command=lambda j=j: self.insert_emoji(chr(j)))
                    btn.pack(side=tk.LEFT)

        # Add the Emoticons category
        add_category("Block Elements", 0x2580, 0x259F)
        add_category("Geometric Shapes", 0x25A0, 0x25FF)
        add_category("Emoticons", 0x1F600, 0x1F64F)
        self.side_panel.update_idletasks()  # Force update of the GUI
        self.update_scrollregion()



    def insert_emoji(self, emoji):
        """
        ## @brief Inserts the selected emoji into the current tab's text area.
        #  @param emoji: The emoji to be inserted.
        """
        # Insert the selected emoji into the current tab's text area
        current_tab = self.tab_bar.select()
        if current_tab:
            text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
            text_widget.insert(tk.INSERT, emoji)



    def change_style(self):
        """
        ## @brief Changes the current style of the UI.
        """
        style = ttk.Style()
        current_style = style.theme_use()
        if current_style == 'default':
            style.theme_use('clam')
        else:
            style.theme_use('default')

        def update_scrollregion(self, event):
            self.side_panel.configure(scrollregion=self.side_panel.bbox("all"))

        # Clear the side panel
        for widget in self.side_panel.winfo_children():
            widget.destroy()
        self.side_panel_frame = tk.Frame(self.side_panel, bg='grey')
        self.side_panel_frame.bind("<Configure>", self.update_scrollregion)
        self.side_panel_window = self.side_panel.create_window((0, 0), window=self.side_panel_frame, anchor="nw")

        # Create an entry widget and a button for each style
        self.style_entry = tk.Entry(self.side_panel_frame)
        self.style_entry.pack(fill=tk.X)

        upper_styles = ["𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙", "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
                        "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁", "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
                        "𝔸𝔹𝔸𝔻𝔼𝔽𝔾𝔿𝕀𝕁𝕂𝕃𝕄𝕋𝕆𝕁𝕂𝕃𝕄𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫", "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝖀𝖁𝖂𝖃𝖄𝖅",
                        "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹", "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
                        "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵", "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉",
                        "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"]
        lower_styles = ["𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳", "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
                        "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛", "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
                        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫", "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
                        "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃", "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝔀𝓍𝓎𝓏"]
        styles = upper_styles + lower_styles

        for style in styles:
            btn = tk.Button(self.side_panel_frame, text=style[0] + style[1] + style[2],
                            command=lambda style=style: self.display_text_in_style(style))
            btn.pack(fill=tk.X)
        self.side_panel.update_idletasks()  # Force update of the GUI
        self.update_scrollregion()



    def display_text_in_style(self, style):
        """
        ## @brief Displays the text in the provided style.
        #  @param style: The style in which the text should be displayed.
        """
        # Get the input text and create the styled text
        text = self.style_entry.get().upper()
        styled_text = ""
        for char in text:
            if ord("A") <= ord(char) <= ord("Z"):
                styled_text += style[ord(char) - ord("A")]
            else:
                styled_text += char

        # Insert the styled text into the current tab's text area
        current_tab = self.tab_bar.select()
        if current_tab:
            text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
            text_widget.insert(tk.INSERT, styled_text + "\n")



    def toggle_color_chooser(self):
        """
        ## @brief Toggles the visibility of the color chooser.
        """
        # Toggle visibility of the color chooser
        if self.side_panel.winfo_ismapped():
            self.side_panel.pack_forget()
        else:
            self.side_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Clear the side panel
        for widget in self.side_panel.winfo_children():
            widget.destroy()

        # Create color chooser buttons
        fg_color_btn = tk.Button(self.side_panel, text="Foreground", command=self.choose_fg_color)
        bg_color_btn = tk.Button(self.side_panel, text="Background", command=self.choose_bg_color)
        fg_color_btn.pack(fill=tk.X)
        bg_color_btn.pack(fill=tk.X)



    def choose_fg_color(self):
        """
        ## @brief Chooses a foreground color from a color chooser and applies it to the current tab's text area.
        """
        # Open a color chooser and apply the selected color to the current tab's text area as the foreground color
        fg_color = colorchooser.askcolor(title="Choose foreground color")[1]
        current_tab = self.tab_bar.select()
        if current_tab:
            text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
            text_widget.config(fg=fg_color)

    def choose_bg_color(self):

        """
        ## @brief Chooses a background color from a color chooser and applies it to the current tab's text area.
        """
        # Open a color chooser and apply the selected color to the current tab's text area as the background color
        bg_color = colorchooser.askcolor(title="Choose background color")[1]
        current_tab = self.tab_bar.select()
        if current_tab:
            text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
            text_widget.config(bg=bg_color)

    def display_readme(self):
        """
        @brief Displays the contents of the README file.
        """
        # Create a new tab with a Text widget
        tab = tk.Frame(self.tab_bar)
        text_area = tk.Text(tab, undo=True, wrap='word')
        text_area.pack(expand=1, fill='both')
        self.tab_bar.add(tab, text="README")
        with open('README.txt', 'r', encoding='utf-8') as f:
            text_area.insert(1.0, f.read())
        text_area.config(state='disabled')  # make it read-only


    def save_state(self):
        """
        @brief Saves the current state of all tabs into a JSON file.
        """
        state = []
        for tab in self.tab_bar.tabs():
            text_widget = self.tab_bar.nametowidget(tab).winfo_children()[0]
            content = text_widget.get(1.0, tk.END)
            title = self.tab_bar.tab(tab, "text")
            state.append({"title": title, "content": content})

        with open('progress.json', 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=4)

    def load_state(self):
        """
        @brief Loads the saved state of all tabs from a JSON file.
        """
        try:
            with open('progress.json', 'r', encoding='utf-8') as f:
                state = json.load(f)

            for tab_state in state:
                self.new_tab(tab_state["title"], tab_state["content"])
        except FileNotFoundError:
            pass  # No saved state, so just continue

    def on_close(self):
        """
        @brief Saves the current state and closes the application.
        """
        self.save_state()
        self.root.destroy()

    def copy_text(self, event=None):
        """
        @brief Copies the currently selected text to the clipboard.
        @param event: This is an optional parameter defaulting to None.
        """
        current_tab = self.tab_bar.select()
        text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
        try:
            selected_text = text_widget.get("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
        except tk.TclError:
            pass  # No text selected, do nothing

    def paste_text(self, event=None):
        """
        @brief Pastes text from the clipboard into the current position in the Text widget.
        @param event: This is an optional parameter defaulting to None.
        """
        current_tab = self.tab_bar.select()
        text_widget = self.tab_bar.nametowidget(current_tab).winfo_children()[0]
        try:
            text_widget.insert(tk.INSERT, self.root.clipboard_get())
        except tk.TclError:
            pass  # No text in clipboard, do nothing
if __name__ == "__main__":
    root = tk.Tk()

    Notepad(root)

    root.mainloop()
