import omni.ext


class MotionExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[MotionExtension] Extension Startup")

    def on_shutdown(self):
        print("[MotionExtension] Extension Shut Down")
