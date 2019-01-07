import sublime, sublime_plugin
class noEmptyTabs(sublimeplugin.Plugin):
	def onModified(self, view):
		if(view.fileName() == None):
			view_has_content = view.findAll('\S')
			if(len(view_has_content) <= 0):
				view.setScratch(True)
			else:
				view.setScratch(False)

class newPaste(sublime_plugin.WindowCommand):
	def run(self, window, args):
		if(len(window.views()) == 0 and sublime.getClipboard() != ''):
			window.newFile()
			view = window.activeView()
			view.insert(view.size(), sublime.getClipboard())
		else:
			window.runCommand('paste')


# view.set_scratch(True)