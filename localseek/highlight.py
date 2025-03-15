import re


class Highlighter:
    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'RESET': '\033[0m'
    }

    @classmethod
    def highlight_text(cls, text, pattern, use_regex=False):
        if not pattern:
            return text

        if use_regex:
            try:
                compiled_pattern = re.compile(pattern, re.IGNORECASE)
                highlighted = compiled_pattern.sub(
                    lambda m: f"{cls.COLORS['YELLOW']}{cls.COLORS['BOLD']}{m.group()}{cls.COLORS['RESET']}",
                    text
                )
                return highlighted
            except re.error:
                return text
        else:
            pattern_lower = pattern.lower()
            text_lower = text.lower()
            highlighted = ""
            i = 0

            while i < len(text):
                match_pos = text_lower.find(pattern_lower, i)
                if match_pos == -1:
                    highlighted += text[i:]
                    break

                highlighted += text[i:match_pos]
                match_end = match_pos + len(pattern)
                highlighted += f"{cls.COLORS['YELLOW']}{cls.COLORS['BOLD']}{text[match_pos:match_end]}{cls.COLORS['RESET']}"
                i = match_end

            return highlighted