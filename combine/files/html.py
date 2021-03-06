import os

from .core import File
from .utils import create_parent_directory


class HTMLFile(File):
    def get_path_for_output(self):
        if self.name_without_extension == "index":
            return os.path.join(*self.root_parts[:-1], "index.html")

        return os.path.join(*self.root_parts, "index.html")

    def render_to_output(self, output_path, *args, **kwargs):
        target_path = os.path.join(output_path, self.output_relative_path)
        create_parent_directory(target_path)

        template = kwargs["jinja_environment"].get_template(self.content_relative_path)
        with open(target_path, "w+") as f:
            f.write(template.render())
