import hashlib
import re


class RegistrationUtils:

    @staticmethod
    def regular_registration(password: str) -> bool:
        """
        Check password for compliance

        Args:
            password (str): user input password, then regular check password

        Returns:
            str: True or False, how will end check
        """        
        regular_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$')
        if re.match(regular_pattern, password) is None:
            return False
        return True

    @staticmethod
    def hash_lib(password: str) -> str:
        """
        function str to hash

        Args:
            password (str): input user

        Returns:
            str: hash sha 256
        """        
        hash: str = f"""sha256:{hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest()}"""
        return hash

# print(RegistrationUtils.regular_registration('Ad1Ad!3'))