import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.studio_editable import StudioContainerXBlockMixin

# Make '_' a no-op so we can scrape strings
_ = lambda text: text


class FirepadXBlock(StudioEditableXBlockMixin, XBlock):

    display_name = String(
        display_name=_("Display Name"),
        help=_("Display name for this module"),
        default="Firepad",
        scope=Scope.settings,
    )

    api_key = String(
        display_name=_("API KEY"),
        scope=Scope.settings,
    )

    auth_domain = String(
        display_name=_("AUTH DOMAIN"),
        scope=Scope.settings,
    )

    database_URL = String(
        display_name=_("database URL"),
        scope=Scope.settings,
    )

    editable_fields = ('display_name', 'api_key', 'auth_domain', 'database_URL')
    has_author_view = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/firepad.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/firepad.css"))
        frag.add_css_url("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.17.0/codemirror.css")
        frag.add_css_url("https://cdn.firebase.com/libs/firepad/1.4.0/firepad.css")
        frag.add_javascript(self.resource_string("static/js/src/firepad.js"))
        frag.add_javascript_url('https://www.gstatic.com/firebasejs/3.3.0/firebase.js')
        frag.add_javascript_url('https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.17.0/codemirror.js')
        frag.add_javascript_url('https://cdn.firebase.com/libs/firepad/1.4.0/firepad.min.js')
        api_settings = {'api_key': self.api_key,
                        'auth_domain': self.auth_domain,
                        'database_URL': self.database_URL}
        frag.initialize_js('FirepadXBlock', json_args=api_settings)
        return frag

    def author_view(self, context):
        html = self.resource_string("static/html/author_view.html")
        frag = Fragment(html.format(self=self))
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("FirepadXBlock",
             """<firepad/>
             """),
            ("Multiple FirepadXBlock",
             """<vertical_demo>
                <firepad/>
                <firepad/>
                <firepad/>
                </vertical_demo>
             """),
        ]
