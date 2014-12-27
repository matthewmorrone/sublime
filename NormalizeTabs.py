import sublime, sublime_plugin


class NormalizeTabsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    window = sublime.active_window()
    window.run_command("detect_indentation")
    window.run_command("unexpand_tabs")
    window.run_command("set_setting", {"setting": "tab_size", "value": 4})
    window.run_command("detect_indentation")



    window.run_command("save")
    # window.run_command("")

class ConvertToTwoSpaces(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    window = sublime.active_window()
    window.run_command("detect_indentation")
    window.run_command("unexpand_tabs")
    window.run_command("set_setting", {"setting": "tab_size", "value": 2})
    window.run_command("expand_tabs")




    window.run_command("detect_indentation")
    window.run_command("save")

