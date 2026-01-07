import re


class Emails(list):
    """
    A class to store and validate a list of email addresses.
    """

    def __init__(self, emails):
        """
        Initialize the Emails object with a list of email addresses.

        :param emails: list of email addresses
        """
        self.validate(emails)
        # remove duplicates while preserving order
        unique_emails = []
        for email in emails:
            if email not in unique_emails:
                unique_emails.append(email)

        super().__init__(unique_emails)
        self.data = unique_emails

    def validate(self, emails):
        """
        Validate email list:
        - must contain only strings
        - must contain only valid email addresses
        """
        if not all(isinstance(email, str) for email in emails):
            raise ValueError("All emails must be strings")

        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        for email in emails:
            if not re.match(email_pattern, email):
                raise ValueError("Invalid email address")

    def __repr__(self):
        """
        Reproduce the Emails object.
        """
        return f"{self.__class__.__name__}({list(self)})"

    def __str__(self):
        """
        String representation of the Emails object.
        """
        return ", ".join(self)
