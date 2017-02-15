/* Javascript for FirepadXBlock. */
function FirepadXBlock(runtime, element, api_settings) {
    $(function ($) {
        function init() {
            // Initialize Firebase.
            var config = {
              apiKey: api_settings.api_key,
              authDomain: api_settings.auth_domain,
              databaseURL: api_settings.database_URL
            };
            var appFirebase = firebase.initializeApp(config, api_settings.name_app_firebase);

            // Get Firebase Database reference.
            var firepadRef = appFirebase.database().ref();

            // Create CodeMirror (with lineWrapping on).
            var firepadElement = $('.firepad-block', element)[0];
            var codeMirror = CodeMirror(firepadElement, { lineWrapping: true });

            // Create Firepad (with rich text toolbar and shortcuts enabled).
            var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror, {
                richTextShortcuts: true,
                richTextToolbar: true
            });
        }
        if (api_settings.api_key && api_settings.auth_domain && api_settings.database_URL) {
            init();
        }
    });
}
