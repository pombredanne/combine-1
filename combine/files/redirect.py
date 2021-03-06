import os

from .html import HTMLFile
from .utils import create_parent_directory


class RedirectFile(HTMLFile):
    def render_to_output(self, output_path, *args, **kwargs):
        target_path = os.path.join(output_path, self.output_relative_path)
        create_parent_directory(target_path)

        redirect_to = open(self.path, "r").read().strip()

        template = kwargs["jinja_environment"].get_template("redirect.template.html")
        with open(target_path, "w+") as f:
            f.write(template.render(redirect_url=redirect_to))
