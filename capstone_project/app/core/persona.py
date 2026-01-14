def format_tutor_response(answer: str) -> str:
    """
    Applies tutor persona and tone to the raw answer.
    """

    opening = (
        "Let us explore this thoughtfully.\n\n"
    )

    closing = (
        "\n\nIf you would like, we can go deeper into this topic step by step."
    )

    return opening + answer + closing
