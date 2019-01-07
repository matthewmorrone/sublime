import sublime, sublime_plugin

# self.window.run_command("")

# Multi line find is there, but '.' doesn't match newline characters by default.
# You can either do (.|\n) or prefix the expression with (?s)

def ReplaceAll(edit, view, exp, tar):
	# regions = reversed(view.find_all(exp))
	regions = view.find_all(exp)
	regions.reverse()

	# edit = view.begin_edit()
	for region in regions:
		view.replace(edit, region, tar)
	# view.end_edit(edit)

trailing_white_space = "[\t ]+$"
def TrimTrailing(edit, view):
	ReplaceAll(edit, view, trailing_white_space, "")


def NormalizeLines(edit, view):
	ReplaceAll(edit, view, "\n\n+", "\n\n")
	ReplaceAll(edit, view, ",\n\n", ",\n")
	ReplaceAll(edit, view, "\t ", "\t")

html_comments = "<!--(?s).+?-->"
line_comments = "\n\s*[^:]\/\/.+"
block_comments = "/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/"
both = "(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(\n?\s*[^:]//.*)"

class RemoveLineCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, line_comments, "")
		TrimTrailing(edit, view)
		NormalizeLines(edit, view)
		window.run_command("save")


class RemoveBlockCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, block_comments, "")
		TrimTrailing(edit, view)
		NormalizeLines(edit, view)

		window.run_command("save")

class RemoveHTMLCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, html_comments, "")
		TrimTrailing(edit, view)
		NormalizeLines(edit, view)

		window.run_command("save")


class RemoveCommentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()


		ReplaceAll(edit, view, both, "")

		TrimTrailing(edit, view)
		NormalizeLines(edit, view)


		window.run_command("save")
