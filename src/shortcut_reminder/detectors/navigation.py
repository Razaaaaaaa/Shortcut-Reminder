import pyatspi
from .detector import Detector


class Navigation(Detector):

    def __init__(self):
        self.previous_position = 0

    @property
    def events_type(self) -> list[str]:
        return [
            "object:text-caret-moved",
        ]

    def detect(self, event) -> str | None:
        if event.type == "object:text-caret-moved:system":
            return None

        try:
            source = event.source
            accessible_text = source.queryText()

            caret_offset = accessible_text.caretOffset
            character_count = accessible_text.characterCount


            if caret_offset == self.previous_position:
                return None

            previous_position = self.previous_position
            self.previous_position = caret_offset

            full_content = accessible_text.getText(
                0,
                character_count,
            )

            current_line, current_line_start, current_line_end = (
                accessible_text.getStringAtOffset(
                    caret_offset,
                    pyatspi.TEXT_GRANULARITY_LINE,
                )
            )

            previous_line, previous_line_start, previous_line_end = (
                accessible_text.getStringAtOffset(
                    previous_position,
                    pyatspi.TEXT_GRANULARITY_LINE,
                )
            )


            shortcuts = {
            }

            for action, condition in shortcuts.items():
                if condition:
                    return action

        except Exception as e:
            print("Error PyAT-SPI :", e)

        return None
