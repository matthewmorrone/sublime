import sublime, sublime_plugin

class BetterBlockCommentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    window = sublime.active_window()
    window.run_command("expand_selection", {"to" : "line"})
    window.run_command("toggle_comment", { "block": "true" })


