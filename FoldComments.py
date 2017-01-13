import sublime, sublime_plugin

class FoldCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    window = sublime.active_window()


    view.fold(view.find_by_selector('comment'))
    
    
    
    # window.run_command("")
    # window.run_command("", {"": "", "": 0})

    # brackets = reversed(view.find_all("{\n"))
    # for region in brackets:
      # view.replace(edit, region, "\n{\n")


class UnfoldCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    window = sublime.active_window()


    view.unfold(view.find_by_selector('comment'))
    # for region in self.view.find_by_selector('comment'):
    #     self.view.unfold(region)

