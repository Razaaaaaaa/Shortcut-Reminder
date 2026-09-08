import threading
from shortcut_reminder import atspi, overlay
from shortcut_reminder.detectors.selection import Selection


def start_atspi():
    atspi.start()


def main():
    root, change_text = overlay.create_overlay()

    selection = Selection()

    def on_event(event):
        result = selection.detect(event)

        if result is None:
            return

        root.after(
            0,
            change_text,
            result,
        )

    for event_type in selection.events_type:
        atspi.subscribe(
            on_event,
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
