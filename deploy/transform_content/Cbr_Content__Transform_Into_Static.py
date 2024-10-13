import cbr_content
from osbot_markdown.markdown.Markdown_Parser import Markdown_Parser

from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Files import files_list, path_combine_safe, file_contents, file_exists, file_create
from osbot_utils.utils.Json import json_file_create


class Cbr_Content__Transform_Into_Static(Type_Safe):
    markdown_parser : Markdown_Parser

    def convert_all_md_files(self):
        for md_file in self.md_files():
            self.md_file__to__json(md_file)

    def md_file__to__json(self, path):
        path_to_md_file  = path_combine_safe(self.path_content_files(), path)
        path_to_md_json  = path_to_md_file + '.json'
        if file_exists(path_to_md_file):
            markdown_text = file_contents(path_to_md_file)
            markdown_json = self.markdown_parser.markdown_to_html_and_metadata(markdown_text)
            json_file_create(markdown_json, path=path_to_md_json, )
            print(f"Created json file for : {path}")

    def md_files(self):
        base_path       = self.path_content_files() + '/'
        paths__md_files = []

        for full_path in files_list(self.path_content_files(), "*.md"):
            relative_path = full_path.replace(base_path, '')                # Remove the base path from the full path
            paths__md_files.append(relative_path)                           # Add the relative path to the list

        return paths__md_files

    def path_content_files(self):
        return cbr_content.path

if __name__ == "__main__":
    Cbr_Content__Transform_Into_Static().convert_all_md_files()