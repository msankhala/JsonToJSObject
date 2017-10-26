import sublime
import sublime_plugin

import re

class JsonToJsObjectCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self._edit = edit
    # In json key/value pair, in values replace all surounding double quotes
    # with single quotes.
    self._replace_all(r': "(.*)"', r": '\1'")
    # In array value replace double quotes with single quotes.
    self._replace_all(r'"(.*)"(,?\n\s*]?)', r"'\1'\2")
    # In json key/value pair, in keys replace all surounding double quotes
    # with single quotes
    self._replace_all(r'(\n\s*)"(.*)"', r'\1\2')
    # Wrap single quotes around keys with colon (:) in their name.
    self._replace_all(r'(\n\s*)([\w\d_\-]*:[\w\d_]*):', r"\1'\2':")

  def _get_file_content(self):
    return self.view.substr(sublime.Region(0, self.view.size()))

  def _update_file(self, contents):
    self.view.replace(self._edit, sublime.Region(0, self.view.size()), contents)

  def _replace_all(self, regex, replacement):
    contents = self._get_file_content()
    regexObj = re.compile(regex, re.UNICODE)
    contents = re.sub(regexObj, replacement, contents)
    self._update_file(contents)
