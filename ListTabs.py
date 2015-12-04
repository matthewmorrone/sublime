import sublime, sublime_plugin, os, itertools, sys

class ListTabsCommand(sublime_plugin.WindowCommand):
    """
        Shows a quick panel with all of the open tabs
        grouped by their file extension.

        I personally don't like showing the sidebar or 
        tabs so I use this to navigate open files or get
        a quick overview of what I have open on-demand when
        I need it.

        Open the sublime console and write the following
        to try it out. 
            
            window.run_command("list_tabs")
    """

    def description():
        "Shows all open tabs in a quick panel grouped by file extension"

    def run(self):

        (views, strings) = self.group_by_extension(self.window.views())

        def callback(i):
            if i != -1 and views[i]:
                self.window.focus_view(views[i])

        self.window.show_quick_panel(strings, callback)

    def group_by_extension(self, views):
        """Group the views by extension. This returns a tuple of two arrays, the
             first array contains the relevant views, the second contains the strings
             we want to show in the quick panel."""
        get_key = lambda v: self.get_file_extension(v.file_name())
        grouped = itertools.groupby(views, key = get_key)

        strings = []
        views = []

        for grb in grouped:
            strings.append("%s" % grb[0])
            views.append(None)
            for v in grb[1]:
                strings.append(self.name_for_view(v))
                views.append(v)

        return (views, strings)

    def get_file_extension(self, path):
        """Given a path return the file extension"""
        file_name = path.split(os.sep).pop()
        if file_name.startswith("."):
            return "dotfile"
        elif file_name.find(".") == -1:
            return "No extension"
        else:
            return file_name.split(".").pop()


    def name_for_view(self, v):
        """Given a view, create a string used as display name for that view. """
        if v.file_name() == None:
            return "untitled-" + str(v.id())
        else: 
            return os.path.split(v.file_name())[1]