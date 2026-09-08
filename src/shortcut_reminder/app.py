import threading
from shortcut_reminder import atspi, overlay
from shortcut_reminder.detectors.selection import Selection
from shortcut_reminder.detectors.navigation import Navigation


def start_atspi():
    atspi.start()

def main():
    root, change_text = overlay.create_overlay()

    selection = Selection()
    navigation = Navigation()

    detectors = [
        selection,
        navigation,
    ]

    def create_on_event(detector):
        def on_event(event):
            result = detector.detect(event)
            root.after(0, change_text, result)

        return on_event
   
    for detector in detectors:
        event_func = create_on_event(detector)
        events_type = detector.events_type
        for event_type in events_type:
            atspi.subscribe(
                event_func,
                event_type,
            )


    pyatspi_thread = threading.Thread(
        target=start_atspi,
        name="pyatspi",
        daemon=True,
    )

    pyatspi_thread.start()

    root.mainloop()


if __name__ == "__main__":
    main()
