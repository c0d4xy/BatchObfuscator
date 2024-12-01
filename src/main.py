import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Final


class BatchObfuscator:
    """
    A class to handle the obfuscation of batch (.bat) files by adding specific bytes to the beginning of the file.
    """

    __new_bytes: Final[bytes] = b"\xFF\xFE\x0D\x0A"

    def __get_file_path(self) -> str:
        """
        Opens a file dialog for the user to select a file.

        Returns:
            str: The path to the selected file as a string.
        """

        Tk().withdraw()
        file = askopenfilename(defaultextension=".bat")
        return file

    def __batch_file(self, file: str) -> bool:
        """
        Checks if the given file has a '.bat' extension.

        Args:
            file (str): The path to the file to check.

        Returns:
            bool: True if the file is a batch (.bat) file, otherwise False.
        """

        return file.endswith(".bat")

    def modify_file_bytes(self) -> None:
        """
        Modifies the selected batch file by adding predefined bytes at the beginning of the file.

        Raises:
            ValueError: If the selected file is not a '.bat' file.
            Exception: For any errors that occur during file reading or writing.
        """

        file = self.__get_file_path()

        if not self.__batch_file(file=file):
            raise ValueError("Select a valid '.bat' file.")

        directory, filename = os.path.split(file)
        new_filename = os.path.splitext(filename)[0] + "_obfuscated.bat"
        new_file = os.path.join(directory, new_filename)

        try:
            with open(file, "rb") as f:
                original_bytes = f.read()

            with open(new_file, "wb") as f:
                f.write(self.__new_bytes + original_bytes)

        except Exception as e:
            raise Exception(f"Error obfuscating file: {e}")

    @staticmethod
    def start() -> None:
        """
        Starts the batch file obfuscation process.
        """

        try:
            BatchObfuscator().modify_file_bytes()
        except Exception as e:
            print(e)
            return

        print("File obfuscated successfully!")


if __name__ == "__main__":
    BatchObfuscator.start()
