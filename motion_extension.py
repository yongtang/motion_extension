import omni.ext
import omni.timeline


class MotionExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[MotionExtension] Extension Started!")

        # Get the timeline instance
        self.timeline = omni.timeline.get_timeline_interface()

        # Subscribe to the playback state change event
        self.playback_event_sub = (
            self.timeline.get_playback_event_stream().create_subscription_to_pop(
                self.on_playback_state_changed, name="MotionExtensionPlaybackState"
            )
        )

    def on_playback_state_changed(self, event):
        """Callback for playback state changes."""
        if event.type == omni.timeline.PlaybackEventType.PLAY:
            # Simulation started
            self.update_sub = (
                self.timeline.get_update_event_stream().create_subscription_to_pop(
                    self.on_simulation_step, name="MotionExtensionUpdate"
                )
            )
        elif event.type == omni.timeline.PlaybackEventType.STOP:
            # Simulation stopped
            if self.update_sub:
                self.update_sub = None

    def on_simulation_step(self, event):
        """This function runs every simulation step."""
        print("Hello World")

    def on_shutdown(self):
        """Called when the extension is disabled."""
        if self.playback_event_sub:
            self.playback_event_sub = None
        if self.update_sub:
            self.update_sub = None
        print("[MotionExtension] Extension Shut Down!")
