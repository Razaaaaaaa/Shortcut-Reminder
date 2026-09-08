import pyatspi
from .detector import Detector

class Selection(Detector):

    @property
    def events_type(self) -> list[str]:
        return [
            "object:text-caret-moved",
            "object:text-selection-changed",
        ]

    def detect(self, event) -> str | None:
        if event.type == "object:text-caret-moved:system":
            return None

        try:
            source = event.source
            accessible_text = source.queryText()

            selection_count = accessible_text.getNSelections()

            if selection_count == 0:
                return None

            if selection_count != 1:
                return None

            selection_start, selection_end = accessible_text.getSelection(0)

            full_content = accessible_text.getText(
                0,
                accessible_text.characterCount
            )

            selection_content = accessible_text.getText(
                selection_start,
                selection_end
            )

            caret_offset = accessible_text.caretOffset

            line_text, line_start, line_end = (
                accessible_text.getStringAtOffset(
                    (
                        selection_end
                        if selection_start == caret_offset
                        else selection_start
                    ),
                    pyatspi.TEXT_GRANULARITY_LINE,
                )
            )

            shortcuts = {
                "CTRL + A": (
                    selection_start == 0
                    and selection_end == accessible_text.characterCount
                ),

                "CTRL + SHIFT + HOME": (
                    caret_offset == 0
                ),

                "CTRL + SHIFT + END": (
                    caret_offset == accessible_text.characterCount
                ),

                "SHIFT + END": (
                    caret_offset == line_end
                ),

                "SHIFT + HOME": (
                    caret_offset == line_start
                ),

                "SHIFT + UP": (
                    caret_offset > line_start
                    and caret_offset > line_end
                ),

                "SHIFT + DOWN": (
                    caret_offset < line_start
                    and caret_offset < line_end
                ),

                "CTRL + SHIFT + LEFT": (
                    (
                        full_content[max(caret_offset - 1, 0)] == " "
                        or " " in selection_content[1:]
                    )
                    and caret_offset == selection_start
                ),

                "CTRL + SHIFT + RIGHT": (
                    (
                        full_content[
                            min(
                                caret_offset,
                                accessible_text.characterCount - 1
                            )
                        ] == " "
                        or " " in selection_content[1:]
                    )
                    and caret_offset == selection_end
                ),

                "SHIFT + RIGHT": (
                    " " not in selection_content[1:]
                    and caret_offset == selection_end
                ),

                "SHIFT + LEFT": (
                    " " not in selection_content[1:]
                    and caret_offset == selection_start
                ),
            }

            for action, condition in shortcuts.items():
                if condition:
                    return action

        except Exception as e:
            print("Error PyAT-SPI :", e)

        return None

