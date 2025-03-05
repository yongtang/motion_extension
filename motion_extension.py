import omni.ext
import omni.kit.app


class MotionExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[MotionExtension] Extension Started!")

        # Subscribe to simulation step event
        self.update_sub = (
            omni.kit.app.get_app()
            .get_update_event_stream()
            .create_subscription_to_pop(self.on_simulation_step)
        )

    def on_simulation_step(self, event):
        """This function runs every simulation step."""
        print("Hello World")

    def on_shutdown(self):
        """Called when the extension is disabled."""
        if self.update_sub:
            self.update_sub = None
        print("[MotionExtension] Extension Shut Down!")
