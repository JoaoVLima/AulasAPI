def format_mask(number: int or str,
                mask: str = None,
                mask_char='_'
                ):
    """
    Formats a number with zfill and a pre-defined mask (e.g., CPF) or the one passed (e.g., __/____).

    :param number: int or str, e.g., 123456 or '123456'
    :param mask: str, e.g., '___/____' or 'cpf'
    :param mask_char: str, default '_', the character to be replaced with the number
    :return: str, formatted number, e.g., '012/3456'
    """
    masks = {
        'cpf': '___.___.___-__',
        'rg': '__.___.___-__',
        'cnpj': '__.___.___/____-__',
        'zip': '_____-___',
    }
    try:
        if number and mask:
            mask = masks.get(mask) or mask
            size = mask.count(mask_char)
            number = str(number).zfill(size)

            for digit in number:
                mask = mask.replace(mask_char, digit, 1)

            return mask
        else:
            return number
    except Exception:
        return number


def convert_time(seconds: int = None):
    """
    Converts seconds into minutes or hours.

    :param seconds: int, e.g., 362
    :return: str, formatted time, e.g., '6min 2s'
    """

    if not seconds:
        return '0.00s'
    if seconds > 60:
        minutes = seconds // 60
        seconds %= 60
        if minutes > 60:
            hours = minutes // 60
            minutes %= 60
            time = f'{hours:.0f}h {minutes:.0f}min'
        else:
            time = f'{minutes:.0f}min {seconds:.0f}s'
    else:
        time = f'{seconds:.2f}s'
    return time
