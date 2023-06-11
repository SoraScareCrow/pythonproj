▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝗗𝗲𝗮𝗿𝗗𝗶𝗮𝗿𝘆 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
Text Editor made by Andrei Lev Vegero

This is a simple text editor implemented using Python and Tkinter.

▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩

## Features

◎ Multiple tabs for editing multiple documents
◎ Undo and redo functionality
◎ Save and open files
◎ Formatting options such as bold, italic, underline
◎ Color chooser for changing text color
◎ Emoji panel for inserting emojis
◎ It saves all progress user left before closing and returns it back

▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
## How to Use

◎ To create a new tab, click on the "+" button in the toolbar.
◎ To close the current tab, click on the "x" button in the toolbar.
◎ To open a file, go to the "File" menu and select "Open".
◎ To save the current tab content to a file, go to the "File" menu and select "Save".
◎ To apply formatting to the selected text, use the style and color buttons in the toolbar.
◎ To insert an emoji, click on the emoji button in the toolbar and select an emoji from the
 panel.

▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
## Requirements

- Python 3.x
- Tkinter

▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩

I got inspired by websites allowing to choose any utf-8 symbol and
allowing to generate text in unusual styles, which I often use.
I always wanted an app which could handle multiple tabs and use all
functionality from websites I mentioned above, because I edit text
a lot and all of my projects I try to make as 'colorful' as possible.

During Implementation of the program I learned how to use doxygen,
how to save files in jason, how to create multiple tabs.

This program can manipulate files, uses functions, modules, exceptions
and documentation.

I only used tkinter and json - I needed first for whole program and
second for saving data before terminating program.

The Hardest part for me was implementing tabs. Because tkinter has no
such functionality. However, using ttk and tinkering a bit on it gave
me possibility to add non-existing functionality. It is a bit buggy,
but suppose to work well enough.

Also, I used emojis to handle more user-friendly interface, and still
make it as minimized as possible.


▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩

                                  ██████████████████
                              ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
                          ████░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
                        ██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██
                      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒██
                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ████▒▒░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
        ████░░▒▒██░░░░██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
      ██▒▒░░▒▒████▒▒░░██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒██░░██▒▒▒▒██▒▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒████▒▒██░░░░██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒████░░░░██▒▒██░░██▒▒██▒▒██
    ██▒▒▒▒██▒▒██▒▒██▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒██▓▓░░░░░░████░░░░██▒▒██▒▒██
      ████▒▒▒▒██▒▒██▒▒██▒▒▒▒██████▒▒▒▒▒▒████░░░░▓▓▓▓░░░░░░░░░░██▒▒██▒▒██
    ▓▓▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒██░░░░██▒▒▒▒██░░██████░░░░▓▓      ▓▓████▒▒██
    ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒██░░░░▓▓░░▒▒████████▓▓██░░░░    ▓▓░░░░████
  ▓▓▒▒▒▒▒▒██▓▓██▒▒▒▒░░██▒▒██░░▓▓▒▒▒▒░░██  ▒▒██  ░░▓▓      ░░▓▓▓▓██
  ██▒▒▒▒░░██▒▒▒▒██░░██▒▒▒▒██░░██▒▒▒▒▒▒██  ▒▒▒▒▒▒          ████░░██
  ██▒▒▒▒░░██▒▒▒▒██░░██▒▒▒▒▒▒████▒▒▒▒▒▒██                    ▒▒  ██
    ████▓▓██▒▒▒▒▓▓████▒▒▒▒▒▒▓▓██▒▒▒▒▒▒██  ░░░░                ████
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██              ░░██  ░░████
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░                  ██▒▒██
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░        ░░░░    ▓▓▓▓▒▒██
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██░░      ░░    ██▒▒▒▒▒▒██
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░░░░░    ████▒▒██▒▒▒▒██
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██████████▒▒▒▒▒▒██▒▒▒▒██
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████░░░░      ████▒▒██▒▒▒▒██
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░            ██▒▒██▒▒▒▒██
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░░░              ██▓▓▒▒▒▒██
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██░░░░                  ██████
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░░░                      ██  ██████
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░░░                      ████    ████
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░░░░░                        ████░░░░▓▓██
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░░░██░░░░                        ████    ██
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░██░░░░████░░░░                        ████  ██
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░░░░░░░████░░░░                        ██  ██
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░  ░░░░░░░░████░░░░                          ██
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░██░░    ░░░░░░░░████░░░░                      ██
            ▓▓▓▓▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██░░██░░      ░░░░░░░░░░▒▒▓▓░░░░░░                ░░██
            ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░██░░░░      ░░░░░░██░░░░██████░░░░              ██
            ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████░░░░██░░██░░░░░░░░░░████      ░░░░░░████░░░░          ██
            ██▒▒▒▒██  ██▒▒▒▒▒▒▒▒▒▒████░░░░██░░██░░▓▓▒▒▓▓▓▓░░░░  ▓▓▓▓  ░░░░░░░░▓▓▓▓░░░░░░░░▓▓
            ██▒▒▒▒██  ██▒▒▒▒▒▒▒▒▒▒▓▓██░░░░████████░░      ▓▓▓▓▓▓░░░░████░░░░██    ██▓▓▓▓▓▓
          ██▒▒▒▒▒▒██    ██▒▒▒▒▒▒▓▓  ██████░░░░░░░░████████░░░░░░░░░░░░░░████
          ██▒▒▒▒██      ██▒▒▒▒▒▒██  ██░░░░████████░░░░░░░░░░░░░░    ░░░░██
          ██▒▒▒▒██      ██▒▒▒▒██      ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░      ░░██
